# 🎓 Student Performance Prediction

A Machine Learning web application built using **Python**, **Flask**, and **Scikit-Learn** that predicts a student's Mathematics score based on demographic and academic factors.

---

## 🚀 Project Overview

This project uses Machine Learning algorithms to predict student performance in Mathematics using the following inputs:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The trained model is deployed using Flask and provides predictions through a user-friendly web interface.

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy

### Machine Learning
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

### Frontend
- HTML5
- CSS3
- Bootstrap

### Deployment
- AWS Elastic Beanstalk
- GitHub

---

## 📂 Project Structure

```text
📦 MLProjects
│
├── 📁 artifacts/                     # Trained model artifacts
│   ├── 📄 data.csv
│   ├── 📄 train.csv
│   ├── 📄 test.csv
│   ├── 📄 model.pkl                  # Best trained ML model
│   └── 📄 preprocessor.pkl           # Data preprocessing pipeline
│
├── 📁 notebook/                      # Jupyter notebooks and experiments
│
├── 📁 src/
│   │
│   ├── 📁 components/                # ML pipeline components
│   │   ├── 📄 data_ingestion.py
│   │   ├── 📄 data_transformation.py
│   │   └── 📄 model_trainer.py
│   │
│   ├── 📁 pipeline/                  # Training & prediction pipelines
│   │   ├── 📄 train_pipeline.py
│   │   └── 📄 predict_pipeline.py
│   │
│   ├── 📄 exception.py               # Custom exception handling
│   ├── 📄 logger.py                  # Logging configuration
│   └── 📄 utils.py                   # Utility functions
│
├── 📁 templates/                     # Flask HTML templates
│   ├── 📄 index.html                 # Landing page
│   └── 📄 home.html                  # Prediction page
│
├── 📄 app.py                         # Flask application entry point
├── 📄 application.py                 # AWS Elastic Beanstalk entry point
├── 📄 requirements.txt               # Project dependencies
├── 📄 setup.py                       # Package configuration
├── 📄 README.md                      # Project documentation
│
└── 📁 logs/                          # Application logs (generated)
```

---

## 📊 Dataset Features

### Input Features

| Feature | Description |
|----------|-------------|
| Gender | Male/Female |
| Race/Ethnicity | Group A-E |
| Parental Education | Parent Education Level |
| Lunch | Standard / Free-Reduced |
| Test Preparation | Completed / None |
| Reading Score | Score out of 100 |
| Writing Score | Score out of 100 |

### Target Variable

- Mathematics Score

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Dharmendra-07/MLProjects.git

cd MLProjects
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Application will start on:

```text
http://localhost:5000
```

---

## 🧠 Machine Learning Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Selection
8. Model Serialization
9. Prediction Pipeline
10. Flask Deployment

---

## 📈 Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model is automatically selected and saved as:

```text
artifacts/model.pkl
```

---

## 📷 Application Screens

### Home Page
- Modern Landing Page
- User-friendly Navigation

### Prediction Page
- Student Information Form
- Real-time Maths Score Prediction

---

## 🔥 Future Enhancements

- User Authentication
- Prediction History Tracking
- REST API Support
- Docker Containerization
- CI/CD Pipeline
- Cloud Deployment

---

## 👨‍💻 Author

**Dharmendra Kumar**

Aspiring Data Scientist & Machine Learning Engineer

GitHub:  [https://github.com/Dharmendra-07](https://github.com/Dharmendra-07)

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.