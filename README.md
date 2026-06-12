
## Problem Statement 
Predicting daily mushroom yield (kg) in a climate-controlled polyhouse using real-world sensor 
readings for temperature (°C), relative humidity (%), and CO₂ (ppm). This repository serves as a 
version-controlled data pipeline resilient against model breakdown due to sudden hardware or 
data drift updates. 
## Project Structure 
```text 
├── data/ 
│   ├── processed/        
│   └── raw/              
├── models/               
├── notebooks/            
├── src/ 
# Standardized datasets ready for modeling 
# Raw sensor data uploads (Excluded from Git) 
# Serialized production-ready model files 
# Jupyter notebooks for exploratory data analysis 
│   └── smoke_test.py     # Base validation environment script 
├── .gitignore            
# Explicitly excludes environment and large log assets 
├── README.md             
└── requirements.txt      
# Project roadmap and run protocols 
# Pinned infrastructure dependencies 

## Data Cleaning Strategy Log (Phase 1, Task 2)

**1. Outliers & Anomalies (Threshold Rules)**
Filtered humidity (50-100%), temperature (10-35°C), and CO2 (400-2000 ppm) to remove hard sensor failures (e.g., a dead humidity probe reading 0% or environmental spikes outside biological survival ranges). 

**2. Missing Values (Imputation vs. Row Removal)**
Handled short sensor dropouts (power blips, calibration gaps) using forward-fill (`ffill`) with a strict limit of 2 periods, assuming short-term microclimate stability. Rows completely missing the `yield_kg` target variable were dropped entirely, as we cannot train or evaluate models on missing ground-truth labels.

**3. Duplicates**
Removed exact timestamp duplicates, keeping the `last` entry under the assumption it represents the most recent or corrected system export.


# Data Cleaning Strategy & Log

## Missing Values
* **Initial Report:** Printed and reviewed prior to pipeline execution.
* **Sensor Gaps:** Short gaps (limit=2) in `temperature_c`, `humidity_pct`, and `co2_ppm` were imputed using forward-fill (`ffill`), assuming short-term MCAR dropouts (e.g., power blips).
* **Target Variable:** Rows with missing `yield_kg` after forward-filling were explicitly dropped.

## Outliers & Anomalies
* **Threshold Filters:** Applied explicit bounding rules for an oyster mushroom polyhouse. Readings outside these ranges were treated as sensor failures (e.g., dead probes) rather than rare microclimate events.
* **Ranges:** Humidity (50-100%), Temperature (10-35°C), CO2 (400-2000 ppm). 

## Duplicates
* **Resolution:** Duplicate timestamps, likely caused by double exports, were removed. The `last` recorded reading for any duplicate timestamp was kept.
=======
# Mushroom Yield Prediction Project

## Overview

This project focuses on building a data pipeline and machine learning workflow for predicting mushroom yield using polyhouse sensor data. The dataset contains environmental measurements such as temperature, humidity, and CO₂ concentration collected from cultivation units.

The project is structured to support data ingestion, validation, preprocessing, model training, and deployment-ready model storage.


## cleaning log ## 

loaded clean.py file into src

This script performs data cleaning and preprocessing using several common techniques:
1 Missing value analysis
2 Range-based filtering (data validation)
3 Null target removal
4 Forward-fill imputation
5 Deletion of missing targets
6 Deduplication

Overall Cleaning Strategy

This is a combination of:

1 Data Validation Cleaning
  Filters out out-of-range sensor readings.
2 Missing Value Treatment
  Forward-fill imputation for sensor data.
  Row deletion for missing target values.
3 Data Deduplication
  Removes duplicate timestamps.
4 Quality-Based Filtering
  Retains only records that satisfy predefined oyster polyhouse environmental conditions.

Duplicate records were identified using the timestamp column and removed while retaining the latest occurrence. A total of 0 duplicate records were removed, resulting in a final cleaned dataset containing 365 rows.

02_cleaned.parquet was successfully loaded and validated. The target column (yield_kg) contains 0 missing values, confirming that all records are suitable for downstream analysis and model training.
---

## Project Structure

```text
mushroom-yield-project/
│
├── data/
│   ├── processed/        # Standardized datasets ready for modeling
│   └── raw/              # Raw sensor data uploads (excluded from Git)
│
├── models/               # Serialized production-ready model files
│
├── notebooks/            # Jupyter notebooks for exploratory analysis
│
├── src/
│   └── smoke_test.py     # Base validation environment script
│
├── .gitignore            # Excludes virtual environments and large data files
├── README.md             # Project documentation and workflow guide
└── requirements.txt      # Project dependencies
```

---

## Features

* CSV-based sensor data ingestion
* Data validation and quality checks
* Data preprocessing pipeline
* Exploratory Data Analysis (EDA)
* Machine Learning model training
* Mushroom yield prediction
* Model serialization and storage

---

## Dataset Fields

| Column        | Description                        |
| ------------- | ---------------------------------- |
| timestamp     | Sensor reading timestamp           |
| temperature_c | Temperature in Celsius             |
| humidity_pct  | Relative humidity (%)              |
| co2_ppm       | Carbon dioxide concentration (ppm) |
| yield_kg      | Mushroom yield (kg)                |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MAX-GIT2114/mushroom-yield-project.git
cd mushroom-yield-project
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run Environment Validation

```bash
python src/smoke_test.py
```

### Expected Output

```text
Polyhouse sensor snapshot:
...
Smoke Test Passed!
```

---

## Workflow

1. Store raw sensor files inside `data/raw/`
2. Clean and transform data into `data/processed/`
3. Perform analysis using notebooks
4. Train machine learning models
5. Save trained models in `models/`
6. Evaluate and deploy prediction pipeline

---

## Future Enhancements

* Automated data ingestion
* Feature engineering pipeline
* Hyperparameter tuning
* Streamlit dashboard
* Real-time sensor monitoring
* Cloud deployment


## Project Structure

```text
mushroom-yield-predictor/
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── polyhouse_sensors.csv
│   │
│   ├── interim/
│   │   ├── 01_loaded.csv
│   │   └── 02_cleaned.parquet
│   │
│   └── processed/
│       └── .gitkeep
│
├── docs/
│   └── cleaning_log.md
│
├── models/
│
├── notebooks/
│   ├── .gitkeep
│   └── smoke_test.py
│
├── reports/
│
├── src/
│   ├── generate_data.py
│   ├── ingest.py
│   ├── clean_data.py
│   └── smoke_test.py
│
├── .gitignore
├── README.md
├── requirements.txt
```

## Data Cleaning & Validation

### Steps Performed

* Checked for missing values in all columns.
* Verified that no missing values existed in:

  * timestamp
  * temperature_c
  * humidity_pct
  * co2_ppm
  * yield_kg
* Removed duplicate records if present.
* Applied data validation rules.
* Generated a cleaned dataset for downstream processing.

### Results

* Total clean records: **365**
* Missing values after cleaning: **0** in all columns.

### Output Files

* `data/interim/02_cleaned.parquet`
* `docs/cleaning_log.md`

## Data Quality Analysis

A data quality assessment was performed on the cleaned polyhouse sensor dataset.

### Outputs

* `src/data_quality.py` – Generates the data quality report.
* `reports/data_quality.md` – Contains summary statistics, date range, observation count, and key insights.

### Metrics Evaluated

* Temperature (`temperature_c`)
* Humidity (`humidity_pct`)
* CO₂ (`co2_ppm`)
* Yield (`yield_kg`)

### Key Checks

* Summary statistics (`describe()`)
* Date range and observation count
* Mean vs. median comparison to identify skew
* Data quality insights documented in a readable report


## Project Structure

```text
mushroom-yield-predictor/
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── polyhouse_sensors.csv
│   │
│   ├── interim/
│   │   ├── 01_loaded.csv
│   │   └── 02_cleaned.parquet
│   │
│   └── processed/
│       └── .gitkeep
│
├── docs/
│   └── cleaning_log.md
│
├── models/
│
├── notebooks/
│   ├── .gitkeep
│   └── smoke_test.py
│
├── reports/
│   └── data_quality.md
│
├── src/
│   ├── generate_data.py
│   ├── ingest.py
│   ├── clean_data.py
│   ├── data_quality.py
│   └── smoke_test.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

# Exploratory Data Analysis (EDA)

## Objective

The purpose of this analysis is to explore the relationships between environmental sensor measurements and mushroom yield. The analysis helps identify patterns in the data before building machine learning models.

## Dataset Features

The following features were analyzed:

* `temperature_c` – Temperature in degrees Celsius
* `humidity_pct` – Relative humidity percentage
* `co2_ppm` – Carbon dioxide concentration in parts per million
* `yield_kg` – Mushroom yield in kilograms

## Visualizations

### 1. Correlation Heatmap

A Pearson correlation heatmap was generated to visualize the strength and direction of relationships between all numerical features.

Output:

* `reports/figures/corr_heatmap.png`

### 2. Scatter Plots

Scatter plots were created to examine the relationship between yield and each environmental variable:

* Humidity vs Yield
* Temperature vs Yield
* CO₂ vs Yield

Output:

* `reports/figures/scatter_yield.png`

## Tools Used

* Python
* Pandas
* Matplotlib

## Running the Analysis

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run the EDA script:

```bash
python src/eda.py
```

## Generated Files

```text
reports/
├── eda_notes.md
└── figures/
    ├── corr_heatmap.png
    └── scatter_yield.png
```

## Observations

* Correlation analysis helps identify relationships among variables.
* Scatter plots provide a visual understanding of trends between sensor readings and mushroom yield.
* Findings from EDA can guide feature selection and model development.

## Limitations

* Correlation does not imply causation.
* Pearson correlation only captures linear relationships.
* Outliers may influence correlation values and visual interpretations.

mushroom-yield-predictor/
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── polyhouse_sensors.csv
│   │
│   ├── interim/
│   │   ├── 01_loaded.csv
│   │   └── 02_cleaned.parquet
│   │
│   └── processed/
│       └── .gitkeep
│
├── docs/
│   └── cleaning_log.md
│
├── models/
│
├── notebooks/
│   ├── .gitkeep
│   └── smoke_test.py
│
├── reports/
│   ├── data_quality.md
│   ├── eda_notes.md              ← NEW
│   │
│   └── figures/                  ← NEW
│       ├── corr_heatmap.png      ← NEW
│       └── scatter_yield.png     ← NEW
│
├── src/
│   ├── generate_data.py
│   ├── ingest.py
│   ├── clean_data.py
│   ├── data_quality.py
│   ├── smoke_test.py
│   └── eda.py                    ← NEW
│
├── .gitignore
├── README.md
└── requirements.txt
# # Feature Engineering & Scaling## -day7

## Objective

Prepare machine learning features from the cleaned polyhouse dataset and scale them to a common range using Min-Max Scaling. The resulting feature set will be used for model training in later tasks.

## Input Dataset

Source:

data/interim/02_cleaned.parquet


Target Variable:

yield_kg

## Feature Definitions

### 1. Temperature

Column:

temperature_c

Description:

Average temperature inside the polyhouse in degrees Celsius.

Biological Importance:

Temperature directly affects mushroom growth rate, metabolism, and fruiting body development.

### 2. Humidity

Column:

humidity_pct

Description:

Relative humidity percentage inside the polyhouse.

Biological Importance:

Oyster mushrooms require high humidity for healthy growth and yield production. Low humidity can reduce productivity and affect mushroom quality.

### 3. Carbon Dioxide

Column:

co2_ppm

Description:

Carbon dioxide concentration measured in parts per million (ppm).

Biological Importance:

CO₂ levels influence mushroom respiration and growth conditions. Extremely high or low concentrations may affect yield.

### 4. Temperature–Humidity Interaction Feature

Column:

temp_humid_interaction

Formula:

temp_humid_interaction =
(temperature_c × humidity_pct) / 100

Example:

temperature_c = 25
humidity_pct = 80

temp_humid_interaction =
(25 × 80) / 100
= 20

Biological Importance:

Mushroom growth depends on the combined effect of temperature and humidity rather than either variable independently. This engineered feature helps the model capture interactions between these environmental factors.


## Feature Matrix and Target

Feature Matrix (X):

[
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]


Target Variable (y):

yield_kg

## Scaling Method

Scaler Used:

MinMaxScaler()

Scaling Formula:

x_scaled =
(x - x_min) / (x_max - x_min)

Output Range:

[0, 1]

Purpose:

* Prevents large-scale variables from dominating smaller-scale variables.
* Improves compatibility with many machine learning algorithms.
* Produces comparable feature ranges.

## Saved Outputs

Processed Features:

data/processed/features.parquet


Saved Scaler:

models/minmax_scaler.joblib

## Validation Checks

The following checks are performed after feature engineering:

* Feature and target row counts match.
* No missing values remain after processing.
* All scaled features lie within the range [0, 1].
* Scaler object is successfully saved for future inference.

## Future Improvement

For learning purposes, the scaler is currently fitted on the full cleaned dataset.

## Chronological Train/Test Split

### Objective

To prepare the mushroom yield dataset for machine learning by creating a chronological train/test split while preventing data leakage.

### Methodology

1. Loaded the cleaned dataset from:

   `data/interim/02_cleaned.parquet`

2. Sorted records by timestamp.

3. Applied an 80/20 chronological split:

   * First 80% of records → Training set
   * Last 20% of records → Test set

4. Verified that no test record occurred before the training cutoff date.

5. Applied MinMaxScaler:

   * Fitted only on training data
   * Applied to both training and test data

### Features Used

* temperature_c
* humidity_pct
* co2_ppm

### Target Variable

* yield_kg

### Leakage Prevention

The following assertion verifies that all test observations occur after the training period:

`assert test_start_date > train_end_date`

### Saved Artifacts

#### Model Assets

* models/minmax_scaler_train.joblib

#### Processed Data

* data/processed/train.csv
* data/processed/test.csv

#### NumPy Arrays

* data/processed/X_train.npy
* data/processed/X_test.npy
* data/processed/y_train.npy
* data/processed/y_test.npy

### Output Information Logged

The script logs:

* Train and test row counts
* Train period dates
* Test period dates
* Split cutoff date
* Leakage validation status
* X and y array shapes

### Execution

Run the script using:

`python src/split_test.py`

### Timeline Diagram

The chronological split can be visualized as:

|------------------- Training Set (80%) -------------------|------ Test Set (20%) ------|

2024-01-01                                            2024-10-18              2024-10-19                    2024-12-30
                                                        ↑
                                                   Split Cutoff

This timeline illustrates the separation between training and test windows and confirms that future observations are not used during model training.

### Seasonality Consideration

Because the dataset is split chronologically, the test period represents future observations that the model has not seen during training. If the average value of `yield_kg` in the test period differs significantly from the training period, evaluation metrics may decrease. Such differences can occur due to seasonality, environmental changes, or shifts in growing conditions over time.

This behavior is expected in real-world forecasting scenarios and does not indicate data leakage. Instead, it reflects the model's ability to generalize to future data under changing conditions.


## Baseline Linear Regression

### Objective

Train a baseline Linear Regression model to predict mushroom yield using environmental sensor measurements and evaluate its performance on unseen test data.

### Features

| Feature | Description |
|----------|-------------|
| temperature_c | Temperature inside the polyhouse (°C) |
| humidity_pct | Relative humidity (%) |
| co2_ppm | Carbon dioxide concentration (ppm) |

### Target

| Target | Description |
|----------|-------------|
| yield_kg | Mushroom yield (kg) |

### Methodology

1. Loaded preprocessed train and test datasets.
2. Trained a Linear Regression model using `X_train` and `y_train`.
3. Generated predictions on the test set.
4. Computed evaluation metrics:
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)
   - R² Score
5. Inspected model coefficients to understand feature influence.
6. Saved the trained model and evaluation reports.

### Coefficient Interpretation

Since all features were scaled using MinMaxScaler, coefficient magnitudes can be compared directly.

- Positive coefficient → Higher feature value tends to increase yield.
- Negative coefficient → Higher feature value tends to decrease yield.
- Larger absolute coefficient → Greater influence on model predictions.

### Evaluation Metrics

- **MAE** measures average prediction error in kilograms.
- **RMSE** penalizes larger prediction errors.
- **R²** measures how much variation in yield is explained by the model.

### Saved Artifacts

#### Model

- `models/linear_regression.joblib`

#### Reports

- `reports/metrics_linear.json`
- `reports/metrics_linear.md`

### Execution

```bash
python src/LR_model.py
```

### Baseline Assessment

R² interpretation:

| R² Score | Assessment |
|-----------|------------|
| > 0.70 | Strong baseline |
| 0.50 – 0.70 | Reasonable baseline |
| < 0.50 | Additional feature engineering or advanced models recommended |

### Output

The script prints:

- MAE
- RMSE
- R² Score
- Feature coefficients
- Saved artifact locations

The resulting model serves as a baseline benchmark for future machine learning experiments on mushroom yield prediction.


## Linear Regression Diagnostics

### Objective

Evaluate the baseline Linear Regression model using residual analysis to identify bias, heteroscedasticity, or nonlinear patterns not captured by the model.

### Residual Definition

Residuals were calculated as:

```text
Residual = Actual Yield − Predicted Yield
```

Interpretation:

- Positive residual → Model underpredicted yield.
- Negative residual → Model overpredicted yield.
- Residual close to zero → Accurate prediction.

### Methodology

1. Loaded the trained Linear Regression model.
2. Loaded `X_test` and `y_test`.
3. Generated test predictions.
4. Computed residuals:

```python
residuals = y_test - pred_test
```

5. Saved residual values for inspection.
6. Created diagnostic plots to evaluate model behavior.

### Diagnostic Plots

#### 1. Residuals vs Predicted Yield

Purpose:

- Detect systematic prediction bias.
- Check whether residuals are centered around zero.
- Identify heteroscedasticity (changing variance).

Output:

```text
reports/figures/residuals_vs_predicted.png
```

#### 2. Residuals vs Humidity

Purpose:

- Determine whether humidity effects are fully captured by the linear model.
- Detect nonlinear relationships.

Output:

```text
reports/figures/residuals_vs_humidity.png
```

#### 3. Residuals vs Temperature

Purpose:

- Evaluate model performance across temperature levels.
- Identify potential curvature or missing interactions.

Output:

```text
reports/figures/residuals_vs_temperature.png
```

### Saved Artifacts

#### Residual Dataset

```text
data/processed/residuals_linear.csv
```

Columns:

| Column | Description |
|----------|-------------|
| actual_yield | Actual observed yield |
| predicted_yield | Model prediction |
| residual | Actual − Predicted |

#### Diagnostic Figures

```text
reports/figures/residuals_vs_predicted.png
reports/figures/residuals_vs_humidity.png
reports/figures/residuals_vs_temperature.png
```

### Diagnostic Interpretation Guide

#### Good Signs

- Residuals randomly scattered around zero.
- No obvious trend or curve.
- Similar spread across all predictions.

#### Potential Problems

- Funnel-shaped pattern → Heteroscedasticity.
- Curved pattern → Nonlinear relationship.
- Large clusters away from zero → Systematic bias.

### Recommendation

If residuals appear randomly distributed around zero, the Linear Regression model is an acceptable baseline.

If clear patterns remain:

- Add engineered features.
- Explore interaction terms.
- Evaluate nonlinear models such as:
  - Random Forest Regression
  - Gradient Boosting Regression
  - XGBoost

### Execution

```bash
python src/Residual_Analysis.py
```

### Output Summary

The script:

- Loads the trained model.
- Predicts test-set yield.
- Calculates residuals.
- Saves residual values.
- Generates diagnostic plots.
- Prints residual samples and file locations.

This diagnostic phase validates the quality of the baseline Linear Regression model before moving to more advanced machine learning approaches.

## Random Forest Regression

### Objective

Train a Random Forest Regressor and compare its performance against the Linear Regression baseline.

### Features

- temperature_c
- humidity_pct
- co2_ppm

### Evaluation Metrics

- MAE
- RMSE
- R²

### Feature Importance

Random Forest estimates feature importance using decision tree splits.

Output:

- reports/figures/rf_importance.png

### Saved Artifacts

- models/random_forest.joblib
- reports/metrics_random_forest.json
- reports/random_forest_comparison.md

### Execution

```bash
python src/Random_Forest.py
```



## Time Series Cross Validation

### Objective

Evaluate model stability using TimeSeriesSplit cross-validation on training data.

### Method

- TimeSeriesSplit with 5 folds.
- Only training data used.
- No test data included during cross-validation.

### Models Evaluated

- Linear Regression
- Random Forest Regressor

### Metric

Mean Absolute Error (MAE)

### Outputs

- reports/cv_results.md

### Execution

```bash
python src/cv_reports.py
```

### Interpretation

- Lower MAE indicates better predictive accuracy.
- Lower standard deviation indicates more consistent performance across folds.
- CV results are compared against hold-out test metrics to identify potential overfitting.