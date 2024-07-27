# pip freeze > requirements.txt
# to create the virtual environment use command python -m venv email
# email\Scripts\activate
# pip install -r requirements.txt
# git ignore
# secure.py (email password and secure features)
# .env
from flask import Flask, render_template, url_for,request
import joblib

app = Flask(__name__)

# Loading the joblib model
bow_obj = joblib.load("./models/bag_of_words.lb")
model = joblib.load("./models/bernouliNB.lb")   

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/emaildata', methods=['POST'])
def emaildata():
    if request.method == 'POST':
        # Collecting form data
        message = str(request.form['message'])
        
        email_data = [message]
        email_converted=bow_obj.transform(email_data).toarray()
        prediction = model.predict(email_converted)[0]
        label_dict = {'0':'Ham','1':'Spam'}
        print(email_converted)
        # prediction = model.predict(email_data)[0]
        # dt = {1:'spam',0:'ham'}
        # return str(dt[prediction])
        # return message
        return render_template('output.html',output= label_dict[str(prediction)])
if __name__ == "__main__":
    app.run(debug=True)
