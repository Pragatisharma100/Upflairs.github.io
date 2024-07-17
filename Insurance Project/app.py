from flask import Flask, render_template, url_for,request
import joblib

app = Flask(__name__)

# Loading the joblib model
model = joblib.load("linear_model.lb")
model = joblib.load("randomforest.lb")
model = joblib.load("decisiontree.lb")

@app.route("/")
def home():
    return render_template("home.html")
@app.route('/project')
def contact():
    return render_template('project.html')

@app.route('/insurancedata', methods=['POST'])
def insurancedata():
    if request.method == 'POST':
        # Collecting ftorm data
        age = int(request.form["age"])
        sex=int(request.form["sex"])
        bmi=int(request.form["bmi"])
        children=int(request.form["children"])
        smoker=int(request.form["smoker"])
        healthy_category=int(request.form["healthy_category"])
        region=int(request.form["region"])
        # Preparing data for prediction
        insurance_data = [[age,sex,bmi,children,smoker,healthy_category,region]]
        # Making prediction
        prediction = model.predict(insurance_data)[0]
        # dt = {1:'satisfied',0:'disatisfied'}
        # return str(dt[prediction])
        return prediction

if __name__ == "__main__":
    app.run(debug=True)
