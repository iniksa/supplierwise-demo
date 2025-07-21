
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.config import load_config
from utils.display import show_aggrid, plot_risk_pie

st.title("📦 Inventory Dashboard")
config = load_config()

df = pd.read_csv("inventory_data.csv")
df["Next PO Delivery Date"] = pd.to_datetime(df["Next PO Delivery Date"], errors="coerce")
df["Expected Days Left"] = df["Current Stock (Qty)"] / df["Daily Avg Consumption"].replace(0, np.nan)
df["Buffer Breach Risk"] = df["Expected Days Left"] < config["min_stock_buffer_days"]
df["Expected Delay (days)"] = (df["Next PO Delivery Date"] - pd.Timestamp(datetime.today())).dt.days.fillna(0)

col1, col2, col3 = st.columns(3)
col1.metric("Total SKUs", len(df))
col2.metric("High Risk Items", df["Buffer Breach Risk"].sum())
col3.metric("Avg Stock Days", f"{df['Expected Days Left'].mean():.1f}")

st.subheader("📋 Inventory Data")
show_aggrid(df)

st.subheader("📈 Inventory Risk Chart")
plot_risk_pie(df)
