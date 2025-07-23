import streamlit as st
from datetime import datetime

# setting date variables
min_date = datetime(1990,1,1)
max_date = datetime.now()

st.title("User Information Form")

form_values = {
    "name" : None,
    "height" : None,
    "age" : None,
    "dob" : None,
    "gender" : None,
    }

with st.form(key = "user_info_form"):
    
    form_values["name"] = st.text_input("Enter your Name : ")
    form_values["age"] = st.number_input("Enter your Age : ")
    form_values["height"] = st.number_input("Enter your Height (cm) : ")
    form_values["gender"] = st.selectbox("Gnder", ["Male" , "Female"])
    
    form_values["dob"] = st.date_input("Enter your birth date : " ,max_value= max_date , min_value= min_date)
    
    
    submit_button = st.form_submit_button("Submit")
    if submit_button :
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields !")
        else:
            st.balloons()
            st.subheader("Info")
            for (key, value) in form_values.items():
                st.write(f" {key} : {value}")
    

