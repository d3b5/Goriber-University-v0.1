import streamlit as st
from mail_sender import send_mail

st.subheader('Contact Us:')

with st.form(key='mail_form'):
    user_mail = st.text_input('Enter your mail address',placeholder='mokhless420@hotmail.com')

    raw_message = st.text_area('Enter your message',placeholder='1-2-3 pailam ekta biri')
    message = f"""\
Subject: New mail from {user_mail}

From: {user_mail}
{raw_message}
"""

    button = st.form_submit_button('Submit')

    if button:
        send_mail(message)
        st.info("Your message has been sent.")

st.markdown("<h4 style='text-align: center;'>Want to regret your future life choices and enroll here? Then, Join Us!</h4>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Our Adress:</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>456 Oreo Street, H-Town, Now York-420, Debuland</h6>", unsafe_allow_html=True)
