## **Understanding Session State + Callback flow** and **Form handling**:

---

## ✅ **1. Session State with Multi-step UI (Using `on_click` callbacks)**

### 🔹 **Use Case:**

Multi-step forms/pages (e.g., survey wizard, onboarding flow) where UI components **depend on app state**.

### 🔹 **Key Syntax & Concepts:**

| Element                        | Purpose                                                  |
| ------------------------------ | -------------------------------------------------------- |
| `st.session_state.step`        | Tracks which "page" or "step" the user is on             |
| `st.session_state.info`        | Stores user-submitted data across steps                  |
| `st.button(..., on_click=...)` | Triggers a specific callback function when clicked       |
| `args=(...)`                   | Passes values (e.g. from input fields) into the callback |

### 🔹 **Execution Flow:**

1. **Initialize state** (step = 1, info = `{}` if not already there).
2. Based on `ss.step`, display appropriate UI section.
3. Button click triggers a **callback** (`on_click=go_to_partX`) → updates session state.
4. Streamlit **reruns the script**, and new `ss.step` shows the next screen.

### 💡 Tips:

* Always use `st.session_state` for persisting data across reruns.
* `on_click + args` helps separate **logic from UI** — clean code style!

---

## ✅ **2. User Form with `st.form()` and `form_submit_button()`**

### 🔹 **Use Case:**

Standard **HTML-style forms** with a single **submit button** (like user registration, survey submission).

### 🔹 **Key Syntax & Concepts:**

| Element                    | Purpose                                                                        |
| -------------------------- | ------------------------------------------------------------------------------ |
| `with st.form(key=...)`    | Begins a form block. Inputs inside only get executed when "Submit" is clicked. |
| `st.form_submit_button()`  | Submit trigger for the entire form block                                       |
| `form_values["key"] = ...` | Stores each form input under a dictionary for easy access                      |

### 🔹 **Execution Flow:**

1. `st.form()` collects all input fields.
2. When **Submit** is clicked, the entire block **executes at once**.
3. Logic inside the `if submit_button:` block runs (like validation).
4. If inputs are valid → show info, animations, or process.

### 💡 Tips:

* `st.form()` avoids the need for session state unless persistence is required.
* Use `st.warning()` for inline validation messages.
* Great for collecting structured input.

---

## 🧠 Summary Table

| Feature           | Multi-Step Flow (Session State)         | Standard Form (`st.form`)                      |
| ----------------- | --------------------------------------- | ---------------------------------------------- |
| Data persistence  | Across reruns using `st.session_state`  | Inside form block only (unless manually saved) |
| Input reactivity  | Triggered via `st.button(on_click=...)` | One-time trigger on form submit                |
| Best for          | Multi-page flows, wizard UIs            | Single-shot forms                              |
| Code organization | Separated callbacks, cleaner flow       | All logic inline in `if submit_button:` block  |

---

