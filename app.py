import streamlit as st
from utils.file_handler import ensure_data_files

from pages.customer_management import show_customer_management
from pages.milk_collection import show_milk_collection
from pages.billing import show_billing
from pages.payments import show_payments
from pages.analytics import show_analytics
from pages.top_suppliers import show_top_suppliers

st.set_page_config(page_title="DairyWise Analytics", layout="wide")

ensure_data_files()

st.sidebar.title("🐄 DairyWise Analytics")

page = st.sidebar.radio(
    "Select Page",
    [
        "Customer Management",
        "Milk Collection",
        "Billing",
        "Payments",
        "Analytics",
        "Top Suppliers",
    ],
)

if page == "Customer Management":
    show_customer_management()
elif page == "Milk Collection":
    show_milk_collection()
elif page == "Billing":
    show_billing()
elif page == "Payments":
    show_payments()
elif page == "Analytics":
    show_analytics()
elif page == "Top Suppliers":
    show_top_suppliers()