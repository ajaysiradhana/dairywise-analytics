import streamlit as st
from utils.file_handler import load_customers, save_payment, load_payments


def show_payments():
    st.title("💰 Payments")

    customers_df = load_customers()

    if customers_df.empty:
        st.warning("Please add customers first.")
        return

    customers_df["Customer ID"] = customers_df["Customer ID"].astype(str)

    customer_options = (
        customers_df["Customer ID"] + " - " + customers_df["Customer Name"]
    ).tolist()

    with st.form("payment_form"):
        selected_customer = st.selectbox("Select Customer", customer_options)
        date = st.date_input("Payment Date")
        paid_amount = st.number_input("Paid Amount", min_value=0.0, step=100.0)
        note = st.text_input("Note")

        submitted = st.form_submit_button("Save Payment")

        if submitted:
            customer_id = selected_customer.split(" - ")[0]
            customer_name = selected_customer.split(" - ")[1]

            payment = {
                "Customer ID": customer_id,
                "Customer Name": customer_name,
                "Date": date,
                "Paid Amount": paid_amount,
                "Note": note,
            }

            save_payment(payment)
            st.success("Payment saved successfully!")

    st.subheader("All Payments")
    payments_df = load_payments()
    st.dataframe(payments_df, use_container_width=True)

