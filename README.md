# 🎓 Student Performance Prediction

A Machine Learning web application built with **Python**, **Scikit-learn**, and **Streamlit** that predicts a student's mathematics score based on demographic, educational, and personal attributes.

## 🌐 Live Demo

**🚀 Streamlit App:** https://mlprojects-toy9uq6ngfedc5kzymjsbi.streamlit.app/

---

# 📌 Project Overview

Student Performance Prediction is an End-to-End Machine Learning project that demonstrates the complete ML lifecycle, including:

- Data Ingestion
- Data Transformation
- Feature Engineering
- Model Training
- Model Evaluation
- Model Serialization
- Model Deployment using Streamlit

The application predicts a student's mathematics score based on several input features such as gender, parental education, lunch type, test preparation course, reading score, and writing score.

---

# 🚀 Features

- 📊 Real-time Mathematics Score Prediction
- 🎨 Interactive Streamlit User Interface
- ⚡ Fast and Lightweight
- 🤖 End-to-End Machine Learning Pipeline
- 📦 Serialized Model & Preprocessor
- ☁️ Deployed on Streamlit Community Cloud

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- CatBoost
- XGBoost
- NumPy
- Pandas
- SciPy

## Web Framework

- Streamlit

## Model Serialization

- Joblib
- Dill

## Development Tools

- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
MLProjects/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── data.csv
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── streamlit_app.py
├── requirements.txt
├── setup.py
├── README.md
└── artifacts/
```

---

# 📊 Input Features

The model takes the following inputs:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

---

# 🎯 Output

The application predicts the student's:

- **Mathematics Score**

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/MLProjects.git
```

## 2. Navigate to the Project Directory

```bash
cd MLProjects
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the Application

```bash
streamlit run streamlit_app.py
```

---

# 🌍 Live Deployment

The project is deployed on **Streamlit Community Cloud**.

🔗 **Live Demo:**

https://mlprojects-toy9uq6ngfedc5kzymjsbi.streamlit.app/

---

# 📈 Machine Learning Workflow

1. Data Collection
2. Data Ingestion
3. Data Preprocessing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Streamlit Deployment

---

# 📸 Application Screenshot

> Add screenshots inside an `images/` folder.

Example:

```text
images/home.png
images/prediction.png
```

Then display them:

```markdown
![Home Page](images/home.png)

![Prediction Page](images/prediction.png)
```

---

# 🔮 Future Improvements

- User Authentication
- Prediction History
- Database Integration
- REST API using Flask/FastAPI
- Docker Support
- CI/CD Pipeline
- AWS/Azure/GCP Deployment
- Explainable AI (SHAP)

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Dharmendra Kumar**

GitHub: https://github.com/YOUR_GITHUB_USERNAME

LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE

---

## ⭐ If you like this project

Please consider giving this repository a **Star ⭐** on GitHub.

It helps others discover the project and motivates future improvements.

---

## 🙏 Thank You

Thank you for visiting this repository! Feel free to explore the project, provide feedback, or contribute to its development.