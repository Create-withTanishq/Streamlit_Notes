import streamlit as st

# use of session state
ss = st.session_state

if "counter" not in st.session_state:
    ss.counter = 0

if st.button("Increment Counter"):
    ss.counter += 1
    st.write(f"Counter incremented to {ss.counter}")

if st.button("Reset"):
    ss.counter = 0
    
st.write(f"Counter Value : {ss.counter}")


