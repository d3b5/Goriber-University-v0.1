import smtplib, ssl, os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    sender_email = "parkmejihyo@gmail.com"
    password = os.environ["PASSWORD"]  # will fetch from Streamlit secrets
    receiver_email = sender_email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
