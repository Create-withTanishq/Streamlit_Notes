import streamlit as st
import os

st.title("This is the Title")
st.header("This is the Heading")
st.subheader("This is the Subheader")

st.text("plain text")

st.markdown("## Markdown ##")

st.caption("This is the Caption")

st.divider()

st.code('''def show(id :int):
            print(id) ''',
        language = "python")

st.divider()

st.subheader("Image Display")
st.image("Basics/static/porsche.jpg")