**Streamlit text commands** 
---

### ✅ Basic Text Elements in Streamlit

| Purpose             | Command                                                 | Description                                 |
| ------------------- | ------------------------------------------------------- | ------------------------------------------- |
| **Title (biggest)** | `st.title("My App Title")`                              | Adds a large title at the top               |
| **Header**          | `st.header("This is a header")`                         | A bit smaller than title                    |
| **Subheader**       | `st.subheader("This is a subheader")`                   | Smaller than header                         |
| **Normal Text**     | `st.text("Plain text here")`                            | Displays fixed-width (monospace) plain text |
| **Markdown Text**   | `st.markdown("**Bold** _Italic_")`                      | Use Markdown syntax for formatting          |
| **Caption**         | `st.caption("This is a caption")`                       | Very small, lighter-colored text            |
| **Code Block**      | `st.code("print('Hello World')", language="python")`    | Syntax highlighted code block               |
| **LaTeX Math**      | `st.latex(r"E=mc^2")`                                   | Render math expressions using LaTeX         |
| **HTML (optional)** | `st.markdown("<h1>Hello</h1>", unsafe_allow_html=True)` | Use with caution. Not all HTML works.       |

---

### 📌 Markdown Examples

```python
st.markdown("# This is H1")
st.markdown("## This is H2")
st.markdown("### This is H3")
st.markdown("- Bullet list item")
st.markdown("1. Numbered list item")
st.markdown("> Blockquote")
st.markdown("**Bold** and *Italic* text")
```

---

### 💡 Bonus Tips

* Use `st.write()` for dynamic printing — it accepts strings, Markdown, and even dataframes.

```python
st.write("You can print **Markdown** here too!")
```

---

