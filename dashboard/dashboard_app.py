import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite DB
conn = sqlite3.connect("backend/receipts.db")
cursor = conn.cursor()

# Title
st.title("📊 Receipt OCR Dashboard")

# Fetch data
def get_receipt_data():
    query = "SELECT * FROM receipts"
    df = pd.read_sql(query, conn)
    return df

df = get_receipt_data()

# Display data
if not df.empty:
    st.write("### All Extracted Receipts")
    st.dataframe(df)

    # Optional: filter/search
    with st.sidebar:
        st.write("🔍 Search Receipts")
        keyword = st.text_input("Search in Merchant or Items:")
        if keyword:
            filtered = df[df.apply(lambda row: keyword.lower() in str(row).lower(), axis=1)]
            st.write(f"Filtered Results for: '{keyword}'")
            st.dataframe(filtered)
else:
    st.warning("No receipts found yet.")
