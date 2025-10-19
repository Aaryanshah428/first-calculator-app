import streamlit as st
import math

st.set_page_config(page_title = "calculator", page_icon = "🧮", layout = "centered")
st.title("🧮 Tiny Calculator")

a = st.number_input("first number", value = 0.0, step = 1.0)
b = st.number_input("second number", value = 0.0, step = 1.0)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("➕ add"):
        st.success(f"{a} + {b} = {a + b}")
with col2:
    if st.button("➖ Subtract"):
        st.success(f"{a} - {b} = {a - b}")
with col3:
    if st.button("✖ Multiply"):
        st.success(f"{a} × {b} = {a * b}")
with col4:
    if st.button("➗ Divide"):
        if b == 0:
            st.error("cannot divide by zero")
        else:
            st.success(f"{a} ÷ {b} = {a / b}")
with col5:
    if st.button("aᵇ power (a^b)"):
        st.success(f"{a}{ᵇ} = {a**b}")


e = math.e
pi = math.pi
st.divider()
st.subheader("quick functions")
x = st.number_input("x for quick functions", value = 2.0, step = 1.0, key ="x")
st.write("√x =", math.sqrt(x) if x >= 0 else "NaN")
st.write("x² =", x**2)
st.write("ln(x) =", math.log(x) if x > 0 else "NaN")
st.write("x³ =", x**3)
st.write("x! =", math.factorial(int(x)))







