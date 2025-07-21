
import streamlit as st
from utils.config import load_config, save_config

st.set_page_config(page_title="VendoWise", layout="wide")
config = load_config()

st.sidebar.image("Iniksa-TM.png", width=150)
st.sidebar.title("Navigation")
st.sidebar.markdown("---")

st.sidebar.header("Threshold Configuration")
with st.sidebar.expander("🔧 Configure Thresholds", expanded=False):
    min_stock_buffer = st.slider("Min Stock Buffer (Days)", 0, 30, config["min_stock_buffer_days"])
    max_delivery_delay = st.slider("Max Acceptable Delivery Delay (Days)", 0, 15, config["delay_days"])
    max_po_delay = st.slider("Max PO Delay", 0, 30, config["max_po_delay"])
    max_location_risk = st.slider("Max Location Risk Score", 0, 10, config["max_location_risk"])
    max_rejection_rate = st.slider("Max Rejection Rate (%)", 0.0, 20.0, config["max_reject"] * 100)
    max_payment_terms = st.slider("Max Payment Terms (Days)", 15, 120, config["max_payment_terms"])

    if st.button("Save Settings"):
        config.update({
            "min_stock_buffer_days": min_stock_buffer,
            "delay_days": max_delivery_delay,
            "max_po_delay": max_po_delay,
            "max_location_risk": max_location_risk,
            "max_reject": max_rejection_rate / 100,
            "max_payment_terms": max_payment_terms
        })
        save_config(config)
        st.success("Settings saved.")
