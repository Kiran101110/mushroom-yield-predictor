import streamlit as st
import numpy as np
import pandas as pd

# --------------------------------------------------
# Safe Model Import
# --------------------------------------------------

try:
    from src.predict import predict_yield

except FileNotFoundError:
    st.error(
        "Model artifacts are missing.\n\n"
        "Please run the training pipeline first."
    )
    st.stop()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Mushroom Yield Predictor",
    page_icon="🍄",
    layout="centered"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🍄 Mushroom Yield Predictor")
st.caption("Agritech Environmental Forecasting using Machine Learning")

# --------------------------------------------------
# Input Controls
# --------------------------------------------------

st.header("Sensor Inputs")

col1, col2 = st.columns(2)

with col1:

    temp = st.slider(
        "Temperature (°C)",
        min_value=10.0,
        max_value=35.0,
        value=22.0,
        step=0.1
    )

    humid = st.slider(
        "Humidity (%)",
        min_value=50.0,
        max_value=100.0,
        value=88.0,
        step=0.5
    )

with col2:

    co2 = st.slider(
        "CO₂ (ppm)",
        min_value=400,
        max_value=2000,
        value=900,
        step=10
    )

# --------------------------------------------------
# Sensor Range Warnings
# --------------------------------------------------

if temp < 18 or temp > 26:
    st.warning(
        "⚠ Temperature is outside the common operating range (18–26°C)."
    )

if humid < 80 or humid > 95:
    st.warning(
        "⚠ Humidity is outside the common operating range (80–95%)."
    )

if co2 < 700 or co2 > 1100:
    st.warning(
        "⚠ CO₂ is outside the common operating range (700–1100 ppm)."
    )

# --------------------------------------------------
# Prediction Section
# --------------------------------------------------

st.header("Yield Prediction")

if st.button("Predict Yield"):

    with st.spinner("Generating prediction..."):

        prediction = predict_yield(
            temperature_c=temp,
            humidity_pct=humid,
            co2_ppm=co2
        )

    st.metric(
        label="Estimated Mushroom Yield",
        value=f"{prediction:.2f} kg"
    )

    st.success("Prediction completed successfully.")

# --------------------------------------------------
# Sensitivity Analysis
# --------------------------------------------------

st.header("What-If Analysis")

st.markdown(
    "Humidity is varied while Temperature and CO₂ remain fixed."
)

temp_fixed = 22.0
co2_fixed = 900

humid_range = np.linspace(70, 98, 29)

preds = [
    predict_yield(
        temp_fixed,
        h,
        co2_fixed
    )
    for h in humid_range
]

chart_df = pd.DataFrame({
    "Humidity (%)": humid_range,
    "Predicted Yield (kg)": preds
})

st.line_chart(
    chart_df,
    x="Humidity (%)",
    y="Predicted Yield (kg)"
)

# --------------------------------------------------
# Model Information
# --------------------------------------------------

with st.expander("Model Information"):

    st.markdown("""
### Champion Model
**Tuned Random Forest Regressor**

### Features
- Temperature (°C)
- Humidity (%)
- CO₂ (ppm)

### Target
- Mushroom Yield (kg)

### Validation Strategy
- Chronological 80/20 Train-Test Split
- TimeSeriesSplit Cross Validation

### Performance Metrics
Replace with your actual values:

- Test MAE: X.XX kg
- Test RMSE: X.XX kg
- Test R²: X.XXX

### Project
AI Data Analyst Internship Project
(Zelbytes Private Limited)
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "🍄 Mushroom Yield Predictor | "
    "AI Data Analyst Internship Project | Zelbytes"
)