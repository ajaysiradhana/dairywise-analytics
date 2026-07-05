import streamlit as st
import pandas as pd
from utils.file_handler import load_customers, save_milk_record, load_milk_records
from utils.pricing import get_rate_by_fat


def show_milk_collection():
    st.title("🥛 Milk Collection")

    customers_df = load_customers()

    if customers_df.empty:
        st.warning("Please add customers first.")
        return

    customers_df["Customer ID"] = customers_df["Customer ID"].astype(str)

    customer_options = (
        customers_df["Customer ID"] + " - " + customers_df["Customer Name"]
    ).tolist()

    with st.form("milk_collection_form"):
        selected_customer = st.selectbox("Select Customer", customer_options)

        date = st.date_input("Date")
        shift = st.selectbox("Shift", ["Morning", "Evening"])
        milk_type = st.selectbox("Milk Type", ["Buffalo", "Cow"])
        quantity = st.number_input("Milk Quantity", min_value=0.0, step=0.5)
        fat = st.number_input("Fat %", min_value=0.0, step=0.1)
        snf = st.number_input("SNF %", min_value=0.0, step=0.1)

        submitted = st.form_submit_button("Save Milk Record")

        if submitted:
            customer_id = selected_customer.split(" - ")[0]
            customer_name = selected_customer.split(" - ")[1]

            rate = get_rate_by_fat(fat)
            amount = quantity * rate

            record = {
                "Customer ID": customer_id,
                "Customer Name": customer_name,
                "Date": date,
                "Shift": shift,
                "Milk Type": milk_type,
                "Milk Quantity": quantity,
                "Fat": fat,
                "SNF": snf,
                "Rate": rate,
                "Amount": amount,
            }

            save_milk_record(record)
            st.success(f"Milk record saved! Amount: ₹{amount:.2f}")

    st.subheader("Milk Records")
    records_df = load_milk_records()
    st.dataframe(records_df, use_container_width=True)

