import streamlit as st
import pandas as pd
from utils.file_handler import load_milk_records


def show_top_suppliers():
    st.title("🏆 Top Suppliers Dashboard")

    df = load_milk_records()

    if df.empty:
        st.warning("No milk records found.")
        return

    df["Milk Quantity"] = pd.to_numeric(df["Milk Quantity"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Fat"] = pd.to_numeric(df["Fat"], errors="coerce")

    st.subheader("🥛 Top 10 Customers by Milk Quantity")

    quantity_df = df.groupby("Customer Name")["Milk Quantity"].sum().reset_index()
    quantity_df = quantity_df.sort_values("Milk Quantity", ascending=False).head(10)

    st.bar_chart(quantity_df.set_index("Customer Name"))

    st.subheader("💰 Top 10 Customers by Revenue")

    revenue_df = df.groupby("Customer Name")["Amount"].sum().reset_index()
    revenue_df = revenue_df.sort_values("Amount", ascending=False).head(10)

    st.bar_chart(revenue_df.set_index("Customer Name"))

    st.subheader("⭐ Highest Average Fat Customers")

    fat_df = df.groupby("Customer Name")["Fat"].mean().reset_index()
    fat_df = fat_df.sort_values("Fat", ascending=False).head(10)

    st.dataframe(fat_df, use_container_width=True)

