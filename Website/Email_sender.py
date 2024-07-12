from flask import Flask,render_template,url_for,request
import pandas as pd
import smtplib
from sender import user_email
Email_sender=Flask(__name__) 
@Email_sender.route("/")
def home(): 
    return render_template("sender.html")


@Email_sender.route('/Email_Sender' , methods=['GET','POST'])
def Email_Sender():
    if request.method == 'POST':
       user_email = request.form['user_email']
       user_subject = request.form['user_subject'] 
       user_message = request.form['user_message']
       print(user_email,user_subject,user_message)

    #    Email_Sender = {'user_email':[user_email],'user_subject':[user_subject],
    #    'user_message':[user_message]}
       user_email("pragatisharmakota@gmail.com",'iimz cdwe pvqq yolt',user_subject,user_message,user_email)
       return "your email has being send"

if __name__=="__main__":
    Email_sender.run(debug=True)


  