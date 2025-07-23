**Streamlit Chart commands** 
---

## ✅ Full Charting Script with Notes

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Streamlit Charts")

# Sample Data for Area, Bar, and Line Charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
```

---

### 📈 Area Chart

```python
st.divider()
st.subheader("📉 Area Chart")
st.area_chart(chart_data)
```

📝 **Use When**:

* Showing **accumulated values**
* Comparing **trends over time**

---

### 📊 Bar Chart

```python
st.divider()
st.subheader("📊 Bar Chart")
st.bar_chart(chart_data)
```

📝 **Use When**:

* Comparing **individual categories**
* Good for **discrete values** (like counts or scores)

---

### 📈 Line Chart

```python
st.divider()
st.subheader("📈 Line Chart")
st.line_chart(chart_data)
```

📝 **Use When**:

* Showing **trends over time**
* Ideal for **continuous data**

---

### ⚪ Scatter Chart

```python
st.divider()
st.subheader("⚪ Scatter Chart")

scatter_data = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})

st.scatter_chart(scatter_data)
```

📝 **Use When**:

* Showing **correlation** or **distribution**
* Detecting **clusters or outliers**

---

### 🗺️ Map Chart

```python
st.divider()
st.subheader("🗺️ Map Chart")

# Random lat/lon near a location (e.g., San Francisco)
map_data = pd.DataFrame({
    "lat": 37.76 + np.random.randn(100) * 0.01,
    "lon": -122.4 + np.random.randn(100) * 0.01
})

st.map(map_data)
```

📝 **Use When**:

* You have **latitude/longitude** data
* Useful for **geospatial visualizations**

---

### 📐 Custom Plot with Matplotlib (`st.pyplot()`)

```python
st.divider()
st.subheader("📐 Matplotlib Chart")

fig, ax = plt.subplots()
ax.plot(chart_data["A"], label="Series A", color="purple", marker="o")
ax.set_title("Custom Line Plot (Matplotlib)")
ax.set_xlabel("Index")
ax.set_ylabel("Values")
ax.legend()

st.pyplot(fig)
```

📝 **Use When**:

* You want **full control** over styling
* You need to use **advanced charts** not supported natively by Streamlit

---

## ✅ Summary Table: When to Use Each Chart

| Chart Type      | Use Case                              | Function             |
| --------------- | ------------------------------------- | -------------------- |
| Area Chart      | Stacked trend, accumulated values     | `st.area_chart()`    |
| Bar Chart       | Compare categories or frequencies     | `st.bar_chart()`     |
| Line Chart      | Trends over time (continuous data)    | `st.line_chart()`    |
| Scatter Chart   | Relationships between two variables   | `st.scatter_chart()` |
| Map             | Show geolocation-based points         | `st.map()`           |
| Matplotlib Plot | Custom styling, advanced plot control | `st.pyplot()`        |

---

