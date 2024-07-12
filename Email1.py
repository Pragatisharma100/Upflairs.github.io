import smtplib

email=input("sender email:")
receiver_email=input("receiver email:")
subject =input("Subject:")
message=input("Message:")

text = f"Subject:{subject}\n\n{message}"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email,"glsm ocws cexe niot")
server.sendmail(email, receiver_email,text)
print("email has being send to ",receiver_email)
server.quit()