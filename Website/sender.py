import smtplib
def user_email(email,password,user_subject,user_message,sender_email):
    # email = "pragatisharmakota@gmail.com"
    # password= "iimz cdwe pvqq yolt"
    text = f"Subject:{user_subject}\n\n{user_message}"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(sender_email,email,text)
    print("email has being send to ",email)
    server.quit()

