from flask import Flask ,render_template,url_for,request
import pandas as pd
portfolio=Flask(__name__)
@portfolio.route("/")
def home():
    # return "My Home page!!!!"
    return render_template("portfolio.html")
@portfolio.route('/education')
def education():
    return render_template("education.html")
@portfolio.route('/experience')
def experience():
    return render_template("experience.html")
@portfolio.route('/project')
def project():
    return render_template("project.html")
@portfolio.route('/skills')
def skills():
    return render_template("skills.html")
@portfolio.route('/contact_me')
def contact_me():
    return render_template("contact_me.html")
@portfolio.route('/profile')
def profile():
    return render_template("profile.html")
@portfolio.route('/userdata' , methods=['GET','POST'])
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

if __name__=="__main__":
    portfolio.run(debug=True)


      