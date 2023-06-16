from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import folium

app = Flask(__name__)

# Load the saved model and scaler
loaded_model = joblib.load('crime_model.pkl')
scaler = joblib.load('scaler.pkl')

def crime_prediction(date_str, latitude, longitude):
    

    # Convert the input date into year, month, and day
    date = pd.to_datetime(date_str)
    year = date.year
    month = date.month
    day = date.day

    # Create a dataframe with the input features
    input_df = pd.DataFrame({
        'year': [year],
        'month': [month],
        'day': [day],
        'hour': [0],
        'minute': [0],
        'latitude': [float(latitude)],
        'longitude': [float(longitude)]
    })

    # Scale the input features using the loaded scaler
    input_scaled = scaler.transform(input_df)

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(input_scaled)

    return str(prediction[0])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['date']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    prediction = crime_prediction(date, latitude, longitude)

    return render_template('analysis.html', prediction=prediction)


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/hotspots')
def hotspots():
    return redirect(url_for('static', filename='crime_hotspots_map.html'))


if __name__ == '__main__':
    app.run(debug=True)
