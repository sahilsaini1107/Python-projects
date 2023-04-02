from flask import Flask,render_template,request
from flask_mail import Mail, Message
from app2 import password


app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sahil.saini.che20@itbhu.ac.in'
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)

@app.route('/form')
def contact():
    return render_template('form.html')


@app.route('/form', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['REmail']
        subject = request.form['Sub']
        message = request.form['Body']
        msg = Message(subject, sender=['sahil.saini.che20@itbhu.ac.in'], recipients=email)
        msg.body = f"From: {name}\nEmail: 'sahil.saini.che20@itbhu.ac.in'\n\n{message}"
        
        mail.send(msg)
        
        return 'Email sent successfully!'
        

app.run(host='localhost', port=5000)