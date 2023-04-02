import smtplib #simple mail transfer protocol
from config import password
import speech_recognition as sr
import pyttsx3 
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('haa bolna kya hai...') 
            voice = listener.listen(source,5,3)  
            info = listener.recognize_google(voice)
            print(info) 
            return info.lower()
    except:
        pass


def send_email(receiver , subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  #transport layer security
    server.login('sahil.saini.che20@itbhu.ac.in', password)
    email = EmailMessage()
    email['From'] = 'sahil.saini.che20@itbhu.ac.in'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    # server.sendmail('sahil.saini.che20@itbhu.ac.in','pisemi8107@marikuza.com','message')
    server.send_message(email)
    server.close()


email_list = {
    'go' : 'pisemi8107@marikuza.com',
    'play': 'sofota2257@duiter.com'
}


# def get_email_info():
#     talk('kisko bhej na hai voto tell kro') 
#     name = get_info()
#     receiver = email_list[name]
#     talk('kaam kya hai bta')
#     subject = get_info()
#     talk('pura bta')
#     message = get_info()
#     send_email(receiver, subject, message)
#     talk('bhej diya hai bhai abb jeene de meko chill kr ')
#     talk('or bhejna rhega to btana')
#     send_more = get_info()
#     if 'yes' in send_more:
#         get_email_info()
def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    print(subject)
    talk('Tell me the text in your email')
    message = get_info()
    print(message)
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()    