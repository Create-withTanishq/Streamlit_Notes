**Streamlit Dataframe commands** 
---

```python
import streamlit as st
import pandas as pd

# Title
st.title("Different types of Dataframes : ")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Kittu", "Tanu", "Rohan", "Mohit"],
    "Age": [19, 21, 20, 22],
    "Skills": ["C++", "Python", "Java", "HTML"]
})
```

---

### 📊 1. `st.dataframe(df)`

```python
st.divider()
st.subheader("Dataframe :")
st.dataframe(df)
```

✅ Interactive, scrollable, resizable
🔍 **Best for large datasets**

---

### ✍️ 2. `st.data_editor(df)`

```python
st.divider()
st.subheader("Editable Dataframe : ")
edited_dataframe = st.data_editor(df)
```

✅ Allows user editing (cell-by-cell)
✅ Returns the updated DataFrame
🧠 You can even use it as a form!

---

### 📋 3. `st.table(df)`

```python
st.divider()
st.subheader("Static Table")
st.table(df)
```

✅ Clean, readable table
❌ Not scrollable or interactive
🧩 Use when showing **summary tables**

---

### 📈 4. `st.metric()`

```python
st.divider()
st.subheader("Metrics :")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean(), 1))
```

✅ Good for dashboard KPIs
✅ Use `delta` for showing trend if needed

---

### 🔄 5. JSON & Dict

```python
st.divider()
st.subheader("Json and Dictionary :")

sample_dictionary = {
    "name": "Tanishq",
    "Age": 21
}

st.json(sample_dictionary)  # Pretty collapsible view
st.write("Sample Dictionary", sample_dictionary)  # Table-like view
```

✅ `st.json()` → Pretty, collapsible
✅ `st.write()` → Simple dictionary print (like `print()`)

---

## ✅ Suggestions to Expand

If you're learning more:

| Idea                  | Command                                 |
| --------------------- | --------------------------------------- |
| Upload a CSV file     | `st.file_uploader()` + `pd.read_csv()`  |
| Filter the dataframe  | `st.selectbox()` + `df[df['col']==val]` |
| Plot a chart          | `st.bar_chart(df)` / `st.line_chart()`  |
| Show user-edited rows | `st.write(edited_dataframe)`            |

---

```python
st.write("Sample Dictionary", sample_dictionary)
```

This is perfect — it outputs the dictionary just like `print()` would, but nicely formatted.

---
