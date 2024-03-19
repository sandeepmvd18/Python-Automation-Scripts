import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, message, to_email, attachment_path=None):
    sender_email = 'your_email@gmail.com'  
    sender_password ='your_password'  

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Email senr successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()
if __name__ == "__main__":
    subject = "Test Email"
    message = "This is a test email sent from Python."
    to_email = "test@gmail.com"
    send_email(subject, message, to_email)