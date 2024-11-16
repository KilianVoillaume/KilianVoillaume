import streamlit as st
import numpy as np

def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculate the monthly payment for a student loan.
    :param principal: Loan amount
    :param annual_rate: Annual interest rate (in percentage)
    :param years: Loan repayment period in years
    :return: Monthly payment and total repayment amount
    """
    monthly_rate = annual_rate / 100 / 12
    n_payments = years * 12
    if monthly_rate > 0:
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -n_payments)
    else:
        monthly_payment = principal / n_payments
    total_payment = monthly_payment * n_payments
    return monthly_payment, total_payment

# Streamlit UI
st.title("🎓 Student Loan Payment Calculator")

st.sidebar.header("Input Parameters")
principal = st.sidebar.number_input("Loan Amount ($)", min_value=0.0, value=10000.0, step=100.0)
annual_rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1)
years = st.sidebar.slider("Repayment Period (Years)", min_value=1, max_value=30, value=10)

monthly_payment, total_payment = calculate_monthly_payment(principal, annual_rate, years)

st.write(f"### Results for a Loan Amount of ${principal:,.2f}")
st.write(f"#### Annual Interest Rate: {annual_rate}%")
st.write(f"#### Repayment Period: {years} years")
st.write(f"- Monthly Payment: **${monthly_payment:,.2f}**")
st.write(f"- Total Payment: **${total_payment:,.2f}**")

# Visualization
import matplotlib.pyplot as plt

months = np.arange(1, years * 12 + 1)
balance = [principal * ((1 + annual_rate / 100 / 12) ** i - 1) / ((1 + annual_rate / 100 / 12) ** (years * 12) - 1) for i in months]

fig, ax = plt.subplots()
ax.plot(months, balance, label="Remaining Balance")
ax.set_xlabel("Months")
ax.set_ylabel("Loan Balance ($)")
ax.set_title("Loan Balance Over Time")
ax.legend()

st.pyplot(fig)
