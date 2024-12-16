import streamlit as st
import pandas as pd
import matplotlib as plt
import joblib
from datetime import datetime
import time

# Load the trained model
model = joblib.load(r"C:\Users\gandhi72\Documents\Solar_ai_code\DutyCycle_Prediction_model.pkl")  # Ensure your model is named correctly

# App title
st.title("Real-Time Duty Cycle Prediction")

# Initialize or load data storage
if "real_time_data" not in st.session_state:
    st.session_state["real_time_data"] = pd.DataFrame(columns=["Time", "Irradiance", "Temperature", "Predicted Duty Cycle"])

# User input with sliders for continuous updates
st.sidebar.header("Input Parameters")
irradiance = st.sidebar.slider("Irradiance (W/m²):", min_value=0, max_value=1200, value=500, step=10)
temperature = st.sidebar.slider("Temperature (°C):", min_value=-10, max_value=50, value=25, step=1)

# Placeholder for real-time graph
st.subheader("Predicted Duty Cycle Over Time")
graph_placeholder = st.empty()

# Continuous prediction and graph update
while True:
    # Get current time
    current_time = datetime.now()

    # Predict the duty cycle
    input_data = pd.DataFrame({"Irradiance": [irradiance], "Temperature": [temperature]})
    predicted_duty_cycle = model.predict(input_data)[0]

    # Add the new data point to the DataFrame in session state
    new_data = {
        "Time": current_time,
        "Irradiance": irradiance,
        "Temperature": temperature,
        "Predicted Duty Cycle": predicted_duty_cycle,
    }
    st.session_state["real_time_data"] = pd.concat(
        [st.session_state["real_time_data"], pd.DataFrame([new_data])], ignore_index=True
    )

    # Plot the graph with all stored data
    fig, ax = plt.subplots()
    ax.plot(
        st.session_state["real_time_data"]["Time"],
        st.session_state["real_time_data"]["Predicted Duty Cycle"],
        marker="o",
        label="Duty Cycle",
    )
    ax.set_xlabel("Time")
    ax.set_ylabel("Predicted Duty Cycle")
    ax.set_title("Real-Time Duty Cycle Prediction")
    ax.legend()
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()

    # Update the graph in the Streamlit app
    graph_placeholder.pyplot(fig)

    # Add a small delay for smooth updates
    time.sleep(2)
