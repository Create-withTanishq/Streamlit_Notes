import streamlit as st

ss = st.session_state

def go_to_part2(name : str):
    ss.info["name"] = name
    ss.step = 2
    
def go_back_part1():
    ss.step = 1
    
def go_to_part3():
    ss.info["feedback"] = feedback
    ss.step = 3
    

if "step" not in ss:
    ss.step = 1

if "info" not in ss:
    ss.info = {}

if ss.step == 1:
    st.header("Part 1")
    name = st.text_input("Enter your name : ")

    st.button("Next", on_click=go_to_part2 , args=(name,))
    
elif ss.step == 2:
    st.header("Part 2")
    feedback = st.text_input("Enter your feedback")
    st.button("Back" , on_click=go_back_part1 )
    st.button("Submit", on_click=go_to_part3 )
    
elif ss.step == 3:
    st.header("Status : ")
    st.success("Succesffully submitted !!")
    st.write(ss.info)
    st.balloons()
    
    
    


