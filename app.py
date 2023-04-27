from flask import Flask, jsonify, request
import joblib
import numpy as np
import json
import xml.etree.ElementTree as ET
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
model = joblib.load('fare_prediction_linearModel.joblib')
@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/predict_fare', methods=['POST'])
def predict_fare():
    # Check the request type
    content_type = request.content_type
    if content_type == 'application/json':
        # Get the data from the JSON request
        data = request.get_json(force=True)
        trip_miles = float(data['trip_miles'])
        pickup_hour = float(data['pickup_hour'])
        trip_minutes = float(data['trip_minutes'])
    elif content_type == 'application/xml':
        # Get the data from the XML request
        xml_data = request.data
        root = ET.fromstring(xml_data)
        trip_miles = float(root.find('trip_miles').text)
        pickup_hour = float(root.find('pickup_hour').text)
        trip_minutes = float(root.find('trip_minutes').text)
    elif content_type == 'application/x-www-form-urlencoded':
        # Get the data from the HTML form request
        trip_miles = float(request.form['trip_miles'])
        pickup_hour = float(request.form['pickup_hour'])
        trip_minutes = float(request.form['trip_minutes'])
    else:
        return jsonify({'error': 'Invalid content type'})

    # Load the model from the joblib file
    model = joblib.load('fare_prediction_linearModel.joblib')

    # Make a prediction using the model
    prediction = model.predict(np.array([[trip_miles, pickup_hour, trip_minutes]]))

    # Return the prediction as a JSON response
    response = jsonify({'fare_prediction': prediction[0]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)