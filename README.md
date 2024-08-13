# Fare Prediction API

This repository contains a simple Flask-based API for predicting taxi fares based on trip characteristics. The API allows you to send a request with trip details and receive a fare prediction in return.
This API provides a simple way to predict taxi fares based on trip characteristics using linear regression model. It supports multiple input formats and can be easily extended to include additional features or models.
The API will be accessible at locally.

## Getting Started

### Prerequisites

Before you start, ensure you have installed the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### Model File

The API uses a pre-trained machine learning model for fare prediction. Ensure you have the model file `fare_prediction_linearModel.joblib` in the root directory of the project. This file is necessary for the API to function correctly.

## API Endpoints

### 1. Home Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a simple "Hello, world!" message to confirm that the API is running.

### 2. Fare Prediction Endpoint

- **URL:** `/predict_fare`
- **Method:** `POST`
- **Description:** Predicts the fare based on the input data provided in the request.
  
#### Input Formats

The endpoint supports three content types for input data:

1. **JSON** (`application/json`)
    - Example:
    ```json
    {
        "trip_miles": 5.5,
        "pickup_hour": 14,
        "trip_minutes": 15
    }
    ```

2. **XML** (`application/xml`)
    - Example:
    ```xml
    <request>
        <trip_miles>5.5</trip_miles>
        <pickup_hour>14</pickup_hour>
        <trip_minutes>15</trip_minutes>
    </request>
    ```

3. **Form Data** (`application/x-www-form-urlencoded`)
    - Example:
    ```
    trip_miles=5.5&pickup_hour=14&trip_minutes=15
    ```

#### Response

The response will be a JSON object containing the predicted fare:

```json
{
    "fare_prediction": 12.34
}
```

If the content type is invalid, the response will include an error message:

```json
{
    "error": "Invalid content type"
}
```

## Running the Application

To run the application locally, execute the following command:

```bash
python app.py
```

