import streamlit as st
import pandas as pd
from utils.file_handler import load_customers, load_milk_records, load_payments


def show_billing():
    st.title("🧾 Billing")

    customers_df = load_customers()
    milk_df = load_milk_records()
    payments_df = load_payments()

    if customers_df.empty:
        st.warning("No customers found.")
        return

    if milk_df.empty:
        st.warning("No milk records found.")
        return

    customers_df["Customer ID"] = customers_df["Customer ID"].astype(str)
    milk_df["Customer ID"] = milk_df["Customer ID"].astype(str)
    payments_df["Customer ID"] = payments_df["Customer ID"].astype(str)

    customer_options = (
        customers_df["Customer ID"] + " - " + customers_df["Customer Name"]
    ).tolist()

    selected_customer = st.selectbox("Select Customer", customer_options)

    customer_id = selected_customer.split(" - ")[0]
    customer_name = selected_customer.split(" - ")[1]

    customer_milk = milk_df[milk_df["Customer ID"] == customer_id]
    customer_payments = payments_df[payments_df["Customer ID"] == customer_id]

    total_milk = pd.to_numeric(customer_milk["Milk Quantity"], errors="coerce").sum()
    total_bill = pd.to_numeric(customer_milk["Amount"], errors="coerce").sum()
    total_paid = pd.to_numeric(customer_payments["Paid Amount"], errors="coerce").sum()
    pending = total_bill - total_paid

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Milk", f"{total_milk:.2f} L")
    col2.metric("Total Bill", f"₹{total_bill:.2f}")
    col3.metric("Paid", f"₹{total_paid:.2f}")
    col4.metric("Pending", f"₹{pending:.2f}")

    st.subheader(f"Milk Records - {customer_name}")
    st.dataframe(customer_milk, use_container_width=True)

    st.subheader(f"Payment Records - {customer_name}")
    st.dataframe(customer_payments, use_container_width=True)

