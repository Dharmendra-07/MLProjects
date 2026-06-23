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

MLProjects/

├── artifacts/
│ ├── data.csv
│ ├── train.csv
│ ├── test.csv
│ ├── model.pkl
│ └── preprocessor.pkl
│
├── notebook/
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── pipeline/
│ │ ├── predict_pipeline.py
│ │ └── train_pipeline.py
│ │
│ ├── exception.py
│ ├── logger.py
│ └── utils.py
│
├── templates/
│ ├── index.html
│ └── home.html
│
├── app.py
├── application.py
├── requirements.txt
├── setup.py
└── README.md

---

## 📊 Dataset Features

### Input Features

| Feature | Description |
|----------|-------------|
| Gender | Male/Female |
| Race/Ethnicity | Group A-E |
| Parental Education | Parent education level |
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