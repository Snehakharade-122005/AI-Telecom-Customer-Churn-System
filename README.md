# 📊 AI Telecom Customer Churn Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-ANN-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

## 📌 Project Overview

The **AI Telecom Customer Churn Prediction System** is an end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn.

The project integrates:

- 🤖 TensorFlow Artificial Neural Network (ANN)
- ⚡ FastAPI REST API
- 📊 Interactive Streamlit Dashboard
- 🗄️ MySQL Database
- 📈 Business Analytics
- 🔍 Explainable AI (Feature Importance)

This solution helps telecom companies identify high-risk customers and take proactive retention actions.

---

# 🚀 Key Features

### 🔹 Customer Churn Prediction
- Predict customer churn using TensorFlow ANN
- Real-time prediction
- Churn probability score
- Risk level classification

---

### 🔹 AI Recommendation Engine

Provides intelligent recommendations such as:

- Long-term contract offers
- Customer retention strategy
- Technical support recommendation
- Pricing suggestions
- Loyalty program recommendation

---

### 🔹 Explainable AI

Displays the most important features influencing prediction.

Example:

- Contract
- Tenure
- Monthly Charges
- Internet Service
- Tech Support

---

### 🔹 Revenue at Risk

Calculates business revenue that could be lost if the customer churns.

```
Revenue at Risk = Total Charges × Churn Probability
```

---

### 🔹 Customer Management

- View prediction history
- Search customers
- Filter customers
- Export customer records

---

### 🔹 Bulk Prediction

Upload CSV files and predict churn for thousands of customers at once.

Features:

- CSV Upload
- Batch Prediction
- Download Results

---

### 🔹 Analytics Dashboard

Interactive dashboard includes:

- KPI Cards
- Churn Rate
- Revenue at Risk
- Risk Distribution
- Prediction Trend
- Customer Distribution
- Contract Analysis
- Gender Analysis
- Revenue Analysis

---

### 🔹 REST API

FastAPI provides prediction APIs for external applications.

Example Endpoint:

```
POST /predict
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming |
| TensorFlow ANN | Machine Learning |
| FastAPI | REST API |
| Streamlit | Web Application |
| MySQL | Database |
| Pandas | Data Processing |
| Plotly | Interactive Charts |
| Scikit-Learn | Data Preprocessing |

---

# 📂 Project Structure

```
AI-Telecom-Customer-Churn-System/
│
├── 🏠 Home.py
├── app.py
├── api.py
├── database.py
├── model_utils.py
├── shap_explanation.py
├── recommendation.py
├── risk_score.py
├── requirements.txt
│
├── models/
│   ├── customer_churn_ann.keras
│   ├── scaler.pkl
│   └── label_encoders.pkl
│
├── pages/
│   ├── dashboard.py
│   ├── customer_management.py
│   └── bulk_prediction.py
│
└── README.md
```

---

# 📊 Dashboard Preview

The dashboard provides:

- 📈 Business KPIs
- 🥧 Churn Distribution
- 📉 Risk Distribution
- 💰 Revenue Analysis
- 📅 Prediction Trends
- 🔍 Customer Search
- 🚨 High Risk Customers
- 📥 CSV Download

---

🌐 Live Demo

🖥 Streamlit Application (Deployed)

The AI Telecom Customer Churn Prediction System is deployed using Streamlit Cloud.

Live Application:

https://ai-telecom-customer-churn-system-uqstc2ufbfvwahmjv6s5bd.streamlit.app/

⚡ FastAPI API Documentation

Local API Documentation:

http://127.0.0.1:8000/docs


Cloud Services Used:

- Streamlit Cloud → Web Application Deployment
- Railway MySQL → Cloud Database
- GitHub → Version Control and Code Repository

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/Snehakharade-122005/AI-Telecom-Customer-Churn-System.git
```

Open Project

```bash
cd AI-Telecom-Customer-Churn-System
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

### Run Main Application

```bash
streamlit run Home.py
```

### Run FastAPI

```bash
uvicorn api:app --reload
```

### API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📈 Future Enhancements

- User Authentication
- Cloud Deployment
- Docker Support
- Email Notifications
- Model Monitoring
- SHAP Explainability
- Multi-language Support
- Role-Based Dashboard
- Power BI Integration

---

# 👩‍💻 Developer

**Sneha Dilip Kharade**

DMVCT – Data Science Batch

B.Tech Computer Science Engineering

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository on GitHub.

---

# 📜 License

This project is licensed under the MIT License.
