import pandas as pd
from utils.file_handler import load_milk_records, load_payments


def get_customer_bill(customer_id):
    milk_df = load_milk_records()
    payment_df = load_payments()

    milk_df["Customer ID"] = milk_df["Customer ID"].astype(str)
    payment_df["Customer ID"] = payment_df["Customer ID"].astype(str)

    customer_id = str(customer_id)

    customer_milk = milk_df[milk_df["Customer ID"] == customer_id]
    customer_payments = payment_df[payment_df["Customer ID"] == customer_id]

    total_bill = pd.to_numeric(customer_milk["Amount"], errors="coerce").sum()
    total_paid = pd.to_numeric(customer_payments["Paid Amount"], errors="coerce").sum()
    pending = total_bill - total_paid

    return total_bill, total_paid, pending