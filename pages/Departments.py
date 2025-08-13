import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Here are all the faculties and department of Goriber University</h1>", unsafe_allow_html=True)

col1, col2,col3 = st.columns(3)
df = pd.read_csv("data.csv")
with col1:
    st.subheader("Faculty of Humanity,Arts,Governing,Urgency (HAGU)")
    st.write("Here are the Faculty of HAGU's offered majors: ")

    for index, row in df[:5].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])
        st.write(row["description"])

with col2:
    st.subheader("Faculty of Science, Technology and Development (STD)")
    st.write("Here are the Faculty of STD's offered majors: ")

    for index, row in df[5:10].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])
        st.write(row["description"])

with col3:
    st.subheader("Faculty of Capital,Hustling,Organization,Risk (CHOR)")
    st.write("Here are the Faculty of CHOR's offered majors: ")

    for index, row in df[10:].iterrows():
        st.subheader(row['subject'])
        st.image("images/" + row["image"])
        st.write(row["description"])
st.write("")

st.markdown("<h4 style='text-align: center;'>Want to regret your future life choices and enroll here? Then, Join Us!</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Our Adress:</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>456 Oreo Street, H-Town, Now York-420, Debuland</h6>", unsafe_allow_html=True)

