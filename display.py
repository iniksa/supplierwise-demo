
from st_aggrid import AgGrid, GridOptionsBuilder
import plotly.express as px
import streamlit as st

def show_aggrid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination()
    gb.configure_default_column(groupable=True)
    grid_options = gb.build()
    AgGrid(df, gridOptions=grid_options, theme='streamlit')

def plot_risk_pie(df):
    df["Risk"] = df["Buffer Breach Risk"].replace({True: "High", False: "Low"})
    fig = px.pie(df, names="Risk", title="📊 Inventory Risk Split", color_discrete_map={"High": "red", "Low": "green"})
    st.plotly_chart(fig, use_container_width=True)

def plot_rejection_bar(df):
    df["rejection_rate (%)"] = (df["rejected_qty"] / df["ordered_qty"]) * 100
    fig = px.bar(df.sort_values("rejection_rate (%)", ascending=False),
                 x="rejection_rate (%)", y="vendor_name",
                 color="rejection_rate (%)",
                 color_continuous_scale=["green", "orange", "red"],
                 title="📉 Vendor Rejection Rate")
    st.plotly_chart(fig, use_container_width=True)
