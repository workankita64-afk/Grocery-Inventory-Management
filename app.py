import streamlit as st
from utils import predict_restock

st.set_page_config(page_title="Smart Grocery Inventory System", layout="wide")

st.title("🛒 Automatic Grocery Restock Prediction System")
st.write("This system predicts **restock levels automatically** based on past sales, month, and festive periods.")

st.sidebar.header("📊 Input Parameters")

month = st.sidebar.slider("Select Month", 1, 12, 5)
festival = st.sidebar.selectbox("Is it a festive period?", ["No", "Yes"])
sales = st.sidebar.number_input("Enter Current Month Sales (units):", min_value=0, value=500)

if st.sidebar.button("Predict Restock Requirement"):
    result = predict_restock(month, festival, sales)
    st.success(f"Recommended Restock Quantity: **{result} units**")

st.markdown("---")
st.caption("Developed by Ankita Shinde | Major Project 2025")
