import pickle

# --- IMPORTANT ---
# Replace 'your_model.pkl' with the actual name of your model file.
model_filename = 'DutyCycle_Prediction_model.pkl'

# Load the model from the file
try:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)

    # Extract the coefficients (weights) and the intercept (bias)
    coefficients = model.coef_
    intercept = model.intercept_

    # The coefficients correspond to your input features (irradiance, temperature)
    # in the order they were used during training.
    # We'll assume the first is for irradiance and the second is for temperature.
    m1 = coefficients[0]
    m2 = coefficients[1]
    c = intercept

    print("✅ Model loaded successfully!")
    print("--- Copy these lines into your ESP32 Arduino code ---")
    print(f"const float m1_irradiance = {m1}f;")
    print(f"const float m2_temperature = {m2}f;")
    print(f"const float c_intercept = {c}f;")

except Exception as e:
    print(f"Error loading or processing model: {e}")
    print("Please ensure the file path is correct and it's a scikit-learn model.")