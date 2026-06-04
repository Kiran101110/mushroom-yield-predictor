
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







