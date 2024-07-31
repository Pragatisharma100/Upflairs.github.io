from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
std = joblib.load(r'F:\Upflairs\Farmer Project\models\standard_scaler')
model = joblib.load(r'F:\Upflairs\Farmer Project\models\kmeans_model')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        form_data = [request.form[field] for field in ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']]
        unseen_data = [list(map(float, form_data))]
        converted_data = std.transform(unseen_data)
        prediction = model.predict(converted_data)[0]
        df = pd.read_csv(r'F:\Upflairs\Farmer Project\models\app_data.csv')
        cluster = df[df['cluster'] == prediction]
        labels = list(cluster['Label'].value_counts().keys())
        
        return render_template('result.html', prediction=int(prediction), labels=labels)

if __name__ == '__main__':
    app.run(debug=True)

