import streamlit as st

st.title("Customer Churn Prediction")
st.write("Welcome to the app!")

# Sample input box
user_input = st.text_input("Enter customer name")

# Just a placeholder response
if user_input:
    st.success(f"Prediction for {user_input}: Not Churned ✅")
