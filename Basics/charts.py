import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Charts")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns= ["A","B","C"]
)

# Area Chart 
st.divider()
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart
st.divider()
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart
st.divider()
st.subheader("Line Chart")
st.line_chart(chart_data)

# Scatter Chart Section
st.divider()
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    "x" : np.random.randn(100),
    "y" : np.random.randn(100),
})

st.scatter_chart(scatter_data)


# Map Plot
st.divider()
st.subheader("Map Chart")

# Random lat/lon near a location (e.g., San Francisco)
map_data = pd.DataFrame({
    "lat": 37.76 + np.random.randn(100) * 0.01,
    "lon": -122.4 + np.random.randn(100) * 0.01
})

st.map(map_data)
