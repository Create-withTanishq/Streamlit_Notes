import streamlit as st

ss = st.session_state
if "selected_value" not in ss:
    ss.selected_value = 25

st.button("ok")
st.button("ok", key= "btn2") # imp else same widget id causes issue


min_value = st.slider("select min value" , 0, 50,25)

ss.selected_value = st.slider("select_main_value" ,min_value , 100 ,ss.selected_value)