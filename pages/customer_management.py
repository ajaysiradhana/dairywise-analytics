import streamlit as st
from utils.file_handler import load_customers, save_customers


def show_customer_management():
    st.title("👥 Customer Management")

    with st.form("customer_form"):
        customer_id = st.text_input("Customer ID")
        customer_name = st.text_input("Customer Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Address")

        submitted = st.form_submit_button("Add Customer")

        if submitted:
            if customer_id and customer_name:
                customer = {
                    "Customer ID": customer_id,
                    "Customer Name": customer_name,
                    "Phone Number": phone,
                    "Address": address,
                }

                save_customers(customer)
                st.success("Customer added successfully!")
            else:
                st.error("Customer ID and Customer Name are required.")

    st.subheader("All Customers")
    df = load_customers()
    st.dataframe(df, use_container_width=True)

