
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.config import load_config
from utils.display import show_aggrid, plot_rejection_bar

st.title("🚚 Vendor Dashboard")
config = load_config()

df = pd.read_csv("vendor_data.csv")
df["expected_delivery_date"] = pd.to_datetime(df["expected_delivery_date"])
df["actual_delivery_date"] = pd.to_datetime(df["actual_delivery_date"])
df["delivery_delay"] = (df["actual_delivery_date"] - df["expected_delivery_date"]).dt.days
df["on_time"] = df["delivery_delay"] <= config["max_po_delay"]

tab1, tab2 = st.tabs(["📈 Vendor Delivery", "📉 Rejection Analysis"])

with tab1:
    st.subheader("🚚 Delivery Timeliness")
    show_aggrid(df[["vendor_name", "expected_delivery_date", "actual_delivery_date", "delivery_delay", "on_time"]])

with tab2:
    st.subheader("🔎 Rejection Rates")
    show_aggrid(df[["vendor_name", "item_code", "ordered_qty", "rejected_qty", "freight_cost", "location_risk"]])
    plot_rejection_bar(df)
