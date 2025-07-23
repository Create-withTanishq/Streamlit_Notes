import streamlit as st
import pandas as pd

st.title("Different types of Dataframes : ")

df = pd.DataFrame(
    {
        "Name" : ["Kittu" , "Tanu" , "Rohan" , "Mohit"],
        "Age" : [19 , 21 , 20 , 22],
        "Skills" : ["C++" , "Python" , "Java" , "HTML"]
    }
)

# Dataframe section
st.divider()
st.subheader("Dataframe :")
st.dataframe(df)

# editable dataframe
st.divider()
st.subheader("Editable Dataframe : ")
edited_dataframe = st.data_editor(df)

# static table
st.divider()
st.subheader("Static Table")
st.table(df)

# metrics section
st.divider()
st.subheader("Metrics :")
st.metric(label = "Total Rows" , value = len(df))
st.metric(label = "Average Age" , value = round(df["Age"].mean(),1))

# json and dictionary
st.divider()
st.subheader("Json and Dictionary :")
sample_dictionary = {
    "name" : "Tanishq",
    "Age" : 21
}

st.json(sample_dictionary)

st.write("Sample Dictionary", sample_dictionary)
