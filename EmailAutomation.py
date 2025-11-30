import smtplib
import ssl
from email.message import EmailMessage

EMAIL= "rajshukla117100@gmail.com"
APP_PASSWORD= "tksx ogqo yzdx kijq"
RECEIVER= "rajshukla118100@gmail.com"

msg = EmailMessage()

msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hell Python............"

msg.set_content("This email was shared by python code........")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)