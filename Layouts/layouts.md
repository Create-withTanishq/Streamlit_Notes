
---

## ✅ Streamlit Layout Components – Cheat Sheet 🧾

---

### 🔸 1. `st.sidebar`

| Feature      | Description                                    |
| ------------ | ---------------------------------------------- |
| `st.sidebar` | Adds widgets to the **sidebar** for better UX  |
| Use-cases    | Navigation, filters, search, file upload, etc. |

**Syntax:**

```python
st.sidebar.title("Sidebar Title")
st.sidebar.text_input("Enter something")
```

---

### 🔸 2. `st.tabs()`

| Feature     | Description                                       |
| ----------- | ------------------------------------------------- |
| `st.tabs()` | Horizontal tabbed interface                       |
| Use-cases   | Page-style layout, form sections, charts grouping |

**Syntax:**

```python
tabs = {"t1": "Page 1", "t2": "Page 2"}
tab_obj = st.tabs(list(tabs.values()))

with tab_obj[0]: st.write("Page 1 content")
with tab_obj[1]: st.write("Page 2 content")
```

💡 You can also use emojis and markdown-friendly labels here.

---

### 🔸 3. `st.columns()`

| Feature         | Description                                   |
| --------------- | --------------------------------------------- |
| `st.columns(n)` | Horizontally split layout into `n` columns    |
| Use-cases       | Dashboard cards, form fields, metrics display |

**Syntax:**

```python
col1, col2 = st.columns(2)
with col1: st.write("Left")
with col2: st.write("Right")
```

👉 You can control relative width too: `st.columns([2, 1])`

---

### 🔸 4. `st.container()`

| Feature          | Description                                        |
| ---------------- | -------------------------------------------------- |
| `st.container()` | Groups widgets into a scrollable block             |
| Use-cases        | Sectioning, card-style design, grouped input areas |

**Syntax:**

```python
with st.container(border=True):
    st.write("Grouped content here")
```

---

### 🔸 5. `st.empty()`

| Feature      | Description                                  |
| ------------ | -------------------------------------------- |
| `st.empty()` | Creates a placeholder for dynamic UI updates |
| Use-cases    | Live metrics, streaming text, progress bars  |

**Syntax:**

```python
placeholder = st.empty()
placeholder.write("Loading...")

# Later update dynamically
placeholder.write("Done!")
```

💡 Use with `on_click` callbacks or loops.

---

### 🔸 6. `st.expander()`

| Feature         | Description                                   |
| --------------- | --------------------------------------------- |
| `st.expander()` | Expand/collapse section                       |
| Use-cases       | Optional content, instructions, extra details |

**Syntax:**

```python
with st.expander("Click to expand"):
    st.write("Hidden content")
```

---

### 🔸 7. `st.button(help=...)`

| Feature      | Description                                   |
| ------------ | --------------------------------------------- |
| `help` param | Shows tooltip on hover                        |
| Use-cases    | User hints, documentation tips, accessibility |

**Syntax:**

```python
st.button("Hover Me", help="This is a tooltip")
```

---

### 🧠 Bonus: Callbacks with Buttons

**Syntax:**

```python
def my_func():
    st.write("Callback triggered!")

st.button("Click Me", on_click=my_func)
```

---

### 🧩 Common Use-Case Combo

* Use `st.columns()` inside a `st.container()` to simulate **cards in rows**.
* Place filters in `st.sidebar` and results in `st.tabs()` or `st.expander()` for clean UIs.
* Combine `st.empty()` with `st.session_state` for dynamic dashboards or multipage flows.

---
