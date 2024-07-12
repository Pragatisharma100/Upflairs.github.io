# MAKING THE FIRST URL
from flask import Flask,render_template,url_for,request
import pandas as pd
app=Flask(__name__) 
# HOME URL  (url "/" or root) ---->http://127.0.0.1:5000
@app.route("/")
def home(): # for home url function name can be any but for further function name of url and func should be same
    # return "My Home Page!!!"
    return render_template("home.html")
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route("/service")
def service():
    return render_template('service.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route('/userdata' , methods=['GET','POST'])
def userdata():
    if request.method == 'POST':
        user_name = request.form['user_name'] 
        user_email = request.form['user_email']
        user_message = request.form['user_message']

        user_data = {'user_name':[user_name],'user_email':[user_email],
        'user_message':[user_message]}
        

        df= pd.DataFrame(user_data)   #single record
        df.to_csv("user_data.csv",index=False)
        return user_data

@app.route('/Quiz' , methods=['GET','POST'])
def Quiz():
    if request.method == 'POST':
        User_Name = request.form['User_Name']
        return render_template("render_data.html",User_Name=User_Name)


if __name__=="__main__":
    app.run(debug=True)