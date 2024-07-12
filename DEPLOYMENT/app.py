from flask import Flask,render_template,url_for,request
import joblib 
import warnings

# loading the joblib model
model=joblib.load("linear_regression_model")
import pandas as pd

app=Flask(__name__) 
@app.route("/")
def home():
    return render_template("index.html")
@app.route('/bikedata' , methods=['GET','POST'])
def bikedata():
    if request.method == 'POST':
        brand_name = int(request.form['brand_name'] )
        ownership = int(request.form['owner'])
        kms_driven = int(request.form['kms_driven'])
        age = int(request.form['age'])
        power = int(request.form['power'])

# x_variables
        # bike_data= {"ownership":ownership,"brand_name":brand_name,"kms_driven":kms_driven,"age":age,"power":power}
        bike_data=[[ownership,brand_name,kms_driven,age,power]]
        prediction=model.predict(bike_data)[0]
    
        # flask,str,list,int,float,tuple,dict
        return str(round(prediction[0],2))
        



if __name__=="__main__":
    app.run(debug=True)


# SINGLE LINEAR REGRESSION
# MULTIPLE LINEAR REGRESSION
# IF NO. OF X_VARIABLE IS MORE THEN 1,THEN IT IS MULTIPLE
# AVERAGE CALCULATED BY MEAN SQUARE METHOD AS IT CALCULATE (ACTUAL PARAMETER-PREDICTION) SQUARE
#  LOGIST REGREESION IS A SUPERVISED (SOLVE CLASSIFICATION TASKS)
# LOGIST REGRESSION V/S LINEAR REGRESSION (THEY ARE SIMILAR IN PERFORMING THE TASKS BUT )
# SIGMOID ACTIVATION FUNCTION (ALWAYS IN RANGE BETWEEN 0-1 VALUE )
# CALCULATING THE LOSS THROUGH LOGLOSS
#  
