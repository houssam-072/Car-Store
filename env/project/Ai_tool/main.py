import os
import joblib
import pandas as pd
def get_car_price(sample_df):
    # Load the model pipeline
    # model_pipeline = joblib.load('model_pipeline.joblib')

    model_path = os.path.join(os.path.dirname(__file__), 'model_pipeline.joblib')
    model_pipeline = joblib.load(model_path)
    expected_columns = ['Car', 'Brand', 'model', 'color', 'Body condition ( New , Perfect , Good , Medium , Bad , So Bad )', 'Mechanics ( New , Perfect , Good , Medium , Bad , So Bad )', 'Fuel']

    missing_columns = [col for col in expected_columns if col not in sample_df.keys()]
    if missing_columns:
        raise ValueError(f"Input data is missing the following required columns: {missing_columns}")

    # Convert input data to a DataFrame
    df = pd.DataFrame([sample_df])
    print('main:', df.columns)

    # Make predictions
    predictions = model_pipeline.predict(df)

    # Extract and return the price
    price = predictions[0]
    return price

# Example usage:
# Define the sample data
# sample_data = {
#     "Car": "corolla",
#     "Brand": "TOYOTA",
#     "model": "xli executive",
#     "milage": 200000,
#     "color": "blue",
#     "Body condition ( New , Perfect , Good , Medium , Bad , So Bad )": "So Bad",
#     "Mechanics ( New , Perfect , Good , Medium , Bad , So Bad )": "Perfect",
#     "Year": 2014,
#     "Fuel": "gasoline"
# }

# price = get_car_price(sample_data)
# print("Predicted price:", price)
