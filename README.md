# Solar AI - AI-Enhanced Solar Power Harvesting with Dynamic MPPT Control

## Overview

**Solar AI** is an integrated machine learning solution for optimizing solar power harvesting through dynamic Maximum Power Point Tracking (MPPT) with AI-assisted duty cycle prediction. This project combines predictive analytics with real-time monitoring to maximize solar energy efficiency and enable predictive maintenance of solar panels.

### Key Features

- **Real-Time Duty Cycle Prediction**: ML-based prediction of optimal duty cycles based on irradiance and temperature
- **MPPT Optimization**: Dynamic Maximum Power Point Tracking for maximum power extraction
- **Predictive Maintenance**: Model degradation forecasting and end-of-life estimation
- **Live Dashboard**: Real-time monitoring of solar generation, consumption, battery SOC, and grid export
- **Data Processing**: Comprehensive data pipelines for solar panel performance analysis
- **Interactive Streamlit UI**: User-friendly interface for monitoring and predictions

## Project Structure

```
Solar_ai_code/
├── Streamlit_app.py                          # Main Streamlit application (real-time duty cycle prediction)
├── training_code.ipynb                       # Jupyter notebook for model training and data exploration
├── requirements.txt                          # Python dependencies
├── DutyCycle_Prediction_model.pkl           # Pre-trained duty cycle prediction model
│
├── Data Files:
│   ├── MPPT_Dataset.csv                     # Raw MPPT training dataset
│   ├── MPPT_Dataset.xlsx                    # MPPT data in Excel format
│   ├── MTTP_data_values.csv                 # MPPT test/validation data
│   ├── MTTP_data_values.xlsx                # MPPT test data in Excel format
│   ├── solar_panel_data_with_duty_cycle.csv         # Solar panel data with computed duty cycles
│   ├── solar_panel_data_with_surface_area_and_duty_cycle.csv  # Enhanced panel data
│   └── solar_panel_decay_data.csv           # Synthetic degradation data for maintenance modeling
│
├── Documentation:
│   ├── AI-Enhanced Solar Power Harvesting with Dynamic MPPT Control.pptx  # Project presentation
│   └── Ai_Training_Model.jpg                # Architecture/model diagram
│
└── Configuration:
    └── .devcontainer/                       # Development container setup
```

## Datasets

### MPPT Datasets
- **MPPT_Dataset**: Primary training dataset containing MPPT operating points
- **MTTP_data_values**: Validation/test dataset for model evaluation

### Solar Panel Data
- **solar_panel_data_with_duty_cycle.csv**: Processed data with computed duty cycle values
- **solar_panel_data_with_surface_area_and_duty_cycle.csv**: Extended dataset including surface area metrics
- **solar_panel_decay_data.csv**: Synthetic degradation patterns for predictive maintenance

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Streamlit
- scikit-learn, pandas, numpy, matplotlib

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaarthickeyan/solar_prediction.git
   cd solar_prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**
   ```bash
   streamlit run Streamlit_app.py
   ```

4. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`

### For Development

- Open `training_code.ipynb` in Jupyter to explore model training and data analysis
- Use the pre-trained model (`DutyCycle_Prediction_model.pkl`) for immediate predictions
- Modify and retrain models as needed with your own datasets

## Usage

### Real-Time Duty Cycle Prediction (Streamlit App)

The main Streamlit application provides:

- **Interactive Sliders**: Adjust irradiance (0-1200 W/m²) and temperature (-10 to 50°C)
- **Live Prediction**: Real-time duty cycle calculations based on input parameters
- **Visual Graph**: Historical plot of predicted duty cycles over time
- **Data Export**: Store and analyze prediction results

**Example Usage:**
```bash
streamlit run Streamlit_app.py
```

Then adjust parameters in the sidebar to see real-time predictions.

### Model Training (Jupyter Notebook)

The `training_code.ipynb` notebook covers:

1. Data generation and preprocessing
2. Feature engineering (irradiance, temperature, cell count, decay)
3. Model training using Random Forest Regressor
4. Model evaluation with MAE and R² metrics
5. Export trained models for production use

## Model Details

### Duty Cycle Prediction Model

**Input Features:**
- Irradiance (W/m²): 200-1000 range
- Temperature (°C): -10 to 50 range
- Number of cells (optional): 30, 60, 90 cell configurations
- Power deviation and decay metrics

**Output:**
- Optimal duty cycle for MPPT control

**Model Type:** Random Forest Regressor (trained on synthetic and real MPPT data)

**Performance Metrics:**
- Evaluated using Mean Absolute Error (MAE)
- R² score for model fit quality

### Panel Degradation Model

For predictive maintenance:
- Tracks power decay over time
- Forecasts panel end-of-life based on degradation trends
- Supports preventive maintenance planning

## Key Files Description

| File | Purpose |
|------|---------|
| `Streamlit_app.py` | Main UI for real-time duty cycle prediction with Streamlit framework |
| `training_code.ipynb` | Jupyter notebook with model training pipeline and data exploration |
| `DutyCycle_Prediction_model.pkl` | Pre-trained ML model for duty cycle prediction (serialized with joblib) |
| `requirements.txt` | Python dependencies list |
| `*_data.csv` | Training and validation datasets for model development |
| `AI-Enhanced Solar...pptx` | Project presentation with technical details |

## Dependencies

```
numpy          - Numerical computations
pandas         - Data manipulation and analysis
matplotlib     - Data visualization
streamlit      - Web application framework
joblib         - Model serialization and loading
scikit-learn   - Machine learning algorithms
```

See `requirements.txt` for pinned versions.

## Technical Architecture

### Data Pipeline
```
Raw Data (CSV) → Processing → Feature Engineering → Model Training → Predictions
```

### MPPT Control Loop
```
Sensor Input → Duty Cycle Prediction → DC-DC Converter Control → Power Extraction
                    (ML Model)
```

### Monitoring & Maintenance
```
Panel Performance → Degradation Analysis → Trend Forecasting → Maintenance Alerts
```

## Performance Optimization

The system optimizes:

1. **Power Extraction**: Dynamic duty cycle adjustment for maximum power point tracking
2. **Response Time**: Real-time predictions to track changing solar conditions
3. **Efficiency**: Reduced losses through optimal switching frequency and voltage control
4. **Longevity**: Predictive maintenance prevents failures and extends panel life

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] MQTT integration for IoT sensor data ingestion
- [ ] Multi-panel system modeling and control
- [ ] Battery storage optimization
- [ ] Grid integration and demand response
- [ ] Web-based dashboard with cloud deployment
- [ ] Real-time monitoring with historical data storage
- [ ] Advanced degradation models (soiling, microcracking detection)
- [ ] Hardware integration (microcontroller firmware)

## License

This project is part of Solar AI research. Specify your license here (e.g., MIT, GPL, etc.)

## Contact & Support

**Project Owner**: kaarthickeyan

For questions, issues, or collaboration:
- Open an issue on GitHub
- Review the project presentation for detailed technical information
- Check the training notebook for implementation details

## References

- Maximum Power Point Tracking (MPPT) Theory
- Solar Panel Degradation Models
- Machine Learning for Power Electronics
- Renewable Energy Optimization

---

**Last Updated**: November 2025  
**Status**: Active Development
