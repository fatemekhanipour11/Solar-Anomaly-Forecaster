# Smart Energy Grid Guardian

## Anomaly Detection and Predictive Analytics for Solar Power Systems

---

## 📌 Overview

This project provides a robust dual-approach solution for solar power systems:

- An **LSTM Autoencoder** for real-time anomaly detection  
- A **time-series forecasting pipeline** for 24-hour electricity generation prediction  

The system improves grid stability, predictive maintenance, and renewable energy optimization.

---

## 🚀 Key Features

- **Anomaly Detection:**  
  Uses an unsupervised LSTM Autoencoder to learn normal operational patterns and detect sensor failures or grid disturbances using reconstruction error.

- **Generation Forecasting:**  
  Implements a multivariate time-series forecasting pipeline using `sktime`, comparing models such as Random Forest, Gradient Boosting, and Ridge Regression.

- **Seasonal Awareness:**  
  Applies cyclical feature engineering (sin/cos transformations) for hour, day, and month to capture periodic energy production patterns.

- **Robust Evaluation:**  
  Uses expanding window cross-validation and grid search for reliable model selection and hyperparameter tuning.

---

## 🛠 Methodology

1. **Data Preparation**  
   Cleaning, normalization, and creation of cyclical time features (sin/cos encoding for hour, day, and month).

2. **Anomaly Detection**  
   The LSTM Autoencoder is trained on normal data only. Reconstruction error is used to define anomaly thresholds.

3. **Forecasting**  
   Uses `sktime`’s `make_reduction` and `MultiplexForecaster` to evaluate multiple regressors and select the best model based on MAE.

---

## 💡 Impact in Energy Systems

This project acts as an early warning system for solar energy infrastructure:

- **Proactive Maintenance:** Detects anomalies before system failures occur  
- **Cost Optimization:** Reduces unnecessary inspections by isolating real faults  
- **Grid Stability:** Improves renewable integration through accurate forecasting  

---

## 📊 Performance Overview

- **Anomaly Detection:** Successfully isolates abnormal production patterns caused by sensor noise or environmental effects  
- **Forecasting:** Captures daily sinusoidal energy production cycles with high accuracy for 24-hour predictions  

---

## ⚙️ Installation

```bash
pip install pandas numpy scikit-learn tensorflow sktime

## 📝 License

This project is licensed under the **Academic & Research License**.

It is intended solely for educational and research purposes in the field of smart grid systems and renewable energy analytics.

Commercial use, redistribution, or deployment in production environments is not permitted without explicit written permission from the author.