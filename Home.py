import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


#Name and welcome message
col1,empty_col, col2= st.columns([0.8,0.1,0.8])
with col1:
    st.image("images/campus.jpg")
with col2:
    st.header("Goriber University")
    content="""
    Welcome to **Goriber University (GU)**, the pride of Debuland.
    
    GU has been teaching generations how to master everything from **Bhondami** to **Phone e Gan Vore Deya**. Here, education meets questionable life skills. Our students graduate not just with degrees, but with the priceless ability to waste time. Join us, and be another bolod.
    """

    st.markdown(content)

st.subheader("Our Courses:")
st.write("To learn more about our matha-nosto degrees, visit our departments page.")

d1,d2,d3 = st.columns(3)
df = pd.read_csv("data.csv")

with d1:
    for index, row in df[:5].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])
with d2:
    for index, row in df[5:10].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])
with d3:
    for index, row in df[10:].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])

st.markdown("<h4 style='text-align: center;'>Want to regret your future life choices and enroll here? Then, Join Us!</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Our Adress:</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>456 Oreo Street, H-Town, Now York-420, Debuland</h6>", unsafe_allow_html=True)

