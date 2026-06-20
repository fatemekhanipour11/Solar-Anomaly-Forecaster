\# Smart Energy Grid Guardian

\## Anomaly Detection and Predictive Analytics for Solar Power Systems



This project provides a robust, dual-approach solution for solar power management: an \*\*LSTM Autoencoder\*\* for real-time anomaly detection and a \*\*Reduction-based Forecaster\*\* for 24-hour electricity generation prediction. The system is designed to enhance grid stability and optimize resource allocation, specifically addressing challenges in the energy sector.



\---



\## 🚀 Key Features



\* \*\*Anomaly Detection:\*\* Uses an Unsupervised \*\*LSTM Autoencoder\*\* to learn normal operational patterns and identify sensor failures or grid disturbances by analyzing reconstruction errors.

\* \*\*Generation Forecasting:\*\* Implements a multivariate time-series forecasting pipeline using `sktime`, comparing various regressors (Random Forest, Gradient Boosting, Ridge) to predict electricity generation.

\* \*\*Seasonal Awareness:\*\* Integrates \*\*Cyclical Feature Engineering\*\* (Sin/Cos transformations of time data) to effectively handle seasonal and daily production cycles, reducing bias in anomaly detection.

\* \*\*Robust Evaluation:\*\* Employs Expanding Window Cross-Validation and Grid Search to ensure model reliability and optimal hyperparameter selection.



\---



\## 🛠 Methodology



1\.  \*\*Data Preparation:\*\* Cleaning, normalization, and generating cyclical time features (`sin`/`cos` for hour, day, and month) to improve temporal awareness.

2\.  \*\*Anomaly Detection:\*\* Training on normal historical data to establish a reconstruction threshold. Sequences with high reconstruction error are flagged as anomalies. 

3\.  \*\*Forecasting:\*\* Utilizing `sktime`'s `make\_reduction` and `MultiplexForecaster` to dynamically select the best-performing model based on Mean Absolute Error (MAE). 



\---



\## 💡 Impact in the Energy Crisis



This project acts as an \*\*Early Warning System\*\* for solar energy infrastructure:

\* \*\*Proactive Maintenance:\*\* Identifies subtle anomalies before they escalate into widespread grid outages.

\* \*\*Resource Optimization:\*\* Enables maintenance teams to focus only on genuine system faults, saving time and costs.

\* \*\*Grid Stability:\*\* Improved forecasting allows for better integration of renewable energy into the grid, minimizing the need for emergency power cut-offs.



\---



\## 📊 Performance Overview



\* \*\*Anomaly Detection:\*\* Effectively isolates abnormal production patterns caused by sensor degradation or unmodeled environmental factors.

\* \*\*Forecasting:\*\* The model captures the sinusoidal daily cycle with high fidelity, providing reliable 24-hour projections for grid management.



\---



\## ⚙️ Prerequisites \& Installation



To run this project, ensure you have Python installed and the following dependencies:



```bash

pip install pandas numpy scikit-learn tensorflow sktime





\## 📝 License

This project is licensed under the \*\*Academic \& Research License\*\*. 

It is intended solely for educational, academic, and research purposes regarding smart grid sustainability. 

Any commercial use or redistribution requires explicit permission from the author.

