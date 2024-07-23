from flask import Flask, render_template, url_for,request
import joblib

app = Flask(__name__)

# Loading the joblib model
model = joblib.load("multinomialNB.lb")

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/emaildata', methods=['POST'])
def emaildata():
    if request.method == 'POST':
        # Collecting form data
        Email_classification = request.form['Email_classification']
        
        email_data = [[Email_classification]]
        prediction = model.predict(email_data)[0]
        dt = {1:'spam',0:'ham'}
        return str(dt[prediction])

if __name__ == "__main__":
    app.run(debug=True)
