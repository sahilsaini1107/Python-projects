# ujuhfzdtamajclyv
from email.message import EmailMessage  #this is preinstalled in python
from app2 import password
import ssl
import smtplib 
print("HTTP/1.0 200 OK\n")
import cgi
#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe

form = cgi.FieldStorage()
f_email = form.getvalue("YourEmail")
r_email = form.getvalue("ReceiverEmail")
s = form.getvalue("Subject")
b = form.getvalue("Body")


email_sender = f_email
email_password = password
email_receiver=r_email
subject=s
body=b
print("hiii")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

    