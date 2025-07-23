import streamlit as st
import time

@st.cache_data
def expensive_computation(x):
    time.sleep(3)  # Simulates a heavy task
    return x * 10

st.title("Caching Example")

num = st.number_input("Enter a number:")
result = expensive_computation(num)

st.write(f"Result after expensive computation: {result}")
