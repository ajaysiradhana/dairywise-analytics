import os
import pandas as pd

DATA_DIR = "data"

CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.csv")
MILK_FILE = os.path.join(DATA_DIR, "milk_records.csv")
PAYMENTS_FILE = os.path.join(DATA_DIR, "payments.csv")


def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(CUSTOMERS_FILE):
        pd.DataFrame(
            columns=["Customer ID", "Customer Name", "Phone Number", "Address"]
        ).to_csv(CUSTOMERS_FILE, index=False)

    if not os.path.exists(MILK_FILE):
        pd.DataFrame(
            columns=[
                "Customer ID",
                "Customer Name",
                "Date",
                "Shift",
                "Milk Type",
                "Milk Quantity",
                "Fat",
                "SNF",
                "Rate",
                "Amount",
            ]
        ).to_csv(MILK_FILE, index=False)

    if not os.path.exists(PAYMENTS_FILE):
        pd.DataFrame(
            columns=["Customer ID", "Customer Name", "Date", "Paid Amount", "Note"]
        ).to_csv(PAYMENTS_FILE, index=False)


def load_customers():
    ensure_data_files()
    return pd.read_csv(CUSTOMERS_FILE)


def save_customers(customer):
    df = load_customers()
    df = pd.concat([df, pd.DataFrame([customer])], ignore_index=True)
    df.to_csv(CUSTOMERS_FILE, index=False)


def load_milk_records():
    ensure_data_files()
    return pd.read_csv(MILK_FILE)


def save_milk_record(record):
    df = load_milk_records()
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    df.to_csv(MILK_FILE, index=False)


def load_payments():
    ensure_data_files()
    return pd.read_csv(PAYMENTS_FILE)


def save_payment(payment):
    df = load_payments()
    df = pd.concat([df, pd.DataFrame([payment])], ignore_index=True)
    df.to_csv(PAYMENTS_FILE, index=False)