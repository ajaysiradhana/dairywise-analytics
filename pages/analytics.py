import streamlit as st
import pandas as pd
from utils.file_handler import load_milk_records, load_payments, load_customers


def show_analytics():
    st.title("📊 Analytics Dashboard")

    customers_df = load_customers()
    milk_df = load_milk_records()
    payments_df = load_payments()

    total_customers = len(customers_df)
    total_milk = 0
    total_revenue = 0
    total_paid = 0

    if not milk_df.empty:
        milk_df["Milk Quantity"] = pd.to_numeric(
            milk_df["Milk Quantity"], errors="coerce"
        )
        milk_df["Amount"] = pd.to_numeric(milk_df["Amount"], errors="coerce")

        total_milk = milk_df["Milk Quantity"].sum()
        total_revenue = milk_df["Amount"].sum()

    if not payments_df.empty:
        payments_df["Paid Amount"] = pd.to_numeric(
            payments_df["Paid Amount"], errors="coerce"
        )
        total_paid = payments_df["Paid Amount"].sum()

    pending = total_revenue - total_paid

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Customers", total_customers)
    col2.metric("Total Milk", f"{total_milk:.2f} L")
    col3.metric("Total Revenue", f"₹{total_revenue:.2f}")
    col4.metric("Pending Amount", f"₹{pending:.2f}")

    if milk_df.empty:
        st.warning("No milk records available for charts.")
        return

    st.subheader("Daily Milk Collection")

    daily_df = milk_df.groupby("Date")["Milk Quantity"].sum().reset_index()
    st.line_chart(daily_df.set_index("Date"))

    st.subheader("Revenue by Milk Type")

    milk_type_df = milk_df.groupby("Milk Type")["Amount"].sum().reset_index()
    st.bar_chart(milk_type_df.set_index("Milk Type"))
