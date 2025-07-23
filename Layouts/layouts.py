
import streamlit as st

# sidebar layout
st.sidebar.title("Sidebar")
st.sidebar.write("this will be used for sliders , buttons etc")
st.sidebar.text_input("Enter reviews : ")


# callback function
def update_placeholder():
    placeholder.write("Placeholder Updated !!")


# tabs layout
tabs = { "tab0" : "Page 1" , "tab1" : "Page 2" , "tab2" : "Page 3"}
tab = st.tabs(list(tabs.values()))

with tab[0]:
    st.write(f"This is {tabs['tab0']}")

with tab[1]:
     st.write(f"This is {tabs['tab1']}")

with tab[2]:
     st.write(f"This is {tabs['tab2']}")
    
    
#columns layout

col1, col2 , col3 = st.columns(3)
with col1:
    st.subheader("Column 1 ")
    st.write("Column 1 content ")
    
with col2:
    st.subheader("Column 2 ")
    st.write("Column 2 content ")

with col3:
    st.subheader("Column 3 ")
    st.write("Column 3 content ")
    
    
# contanier
with st.container(border = True):
    st.write("This is the container")
    st.write("Space for content to be written")

# placeholder : Dynamic content can be written 
placeholder = st.empty()
placeholder.write("Content inside is DYNAMIC and can be change on the go")

st.button("Update Placeholder" , on_click= update_placeholder)


# Explander
with st.expander("Expand for more details >"):
    st.write("This the palce for expanded data 1")
    with st.container(border=True):
        st.write("Container inside expandable widget ... COOL!!")    
        

# Popover(Tooltip)
st.write("hover over the button !!")
st.button("Hover Button", help = "This is the tooltip for the button")
