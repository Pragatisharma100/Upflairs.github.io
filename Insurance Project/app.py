from flask import Flask, render_template, url_for,request
import joblib
import sqlite3
# # Loading the joblib model
# model = joblib.load("linear_model.lb")
model = joblib.load("randomforest.lb")
# model = joblib.load("decisiontree.lb")

app = Flask(__name__)
data_insert_query = """
insert into project (age,sex,bmi,children,region,smoker,healthy_category,prediction)
values(?,?,?,?,?,?,?,?)
"""


@app.route("/")
def home():
    return render_template("home.html")
@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/insurancedata', methods=['GET','POST'])
def insurancedata():
    if request.method == 'POST':
        # Collecting ftorm data
        age = int(request.form["age"])
        sex=int(request.form["sex"])
        bmi=int(request.form["bmi"])
        children=int(request.form["children"])
        smoker=int(request.form["smoker"])
        healthy_category=int(request.form["healthy_category"])
        region=(request.form["region"])
        region_northeast =0
        region_northwest =0
        region_southeast=0
        region_southwest=0
        if region =="ne":
            region_northeast =1
        elif region =="nw":
            region_northwest =1
        elif region=="se":
            region_southeast=1
        else:
             region_southwest=1

        # Preparing data for prediction
        insurance_data = [[age,sex,bmi,children,smoker,healthy_category,region_northeast,region_northwest,region_southeast,region_southwest]]
        # Making prediction
        prediction = str(model.predict(insurance_data)[0])
        print(prediction)
        conn = sqlite3.connect('insurance.db')
        cur = conn.cursor()
        Data = (age,sex,bmi,children,region,smoker,healthy_category,prediction)
        cur.execute(data_insert_query,Data)
        print("Your data is inserted into database : ",Data)
        conn.commit()
        cur.close()
        conn.close()
        return render_template('final.html',output=prediction)

        # return str([prediction])
        # return prediction
        # return insurance_data
if __name__ == "__main__":
    app.run(debug=True)
