import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Student Exam Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Exam Performance Predictor")
st.write("Enter the student details below to predict the Maths Score.")

# ---------------------------
# Input Form
# ---------------------------
with st.form("prediction_form"):

    gender = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    ethnicity = st.selectbox(
        "Race/Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ]
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

    lunch = st.selectbox(
        "Lunch",
        [
            "standard",
            "free/reduced"
        ]
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        [
            "none",
            "completed"
        ]
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=70
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=70
    )

    submit = st.form_submit_button("Predict Maths Score")

# ---------------------------
# Prediction
# ---------------------------
if submit:
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )

        pred_df = data.get_data_as_data_frame()

        pipeline = PredictPipeline()
        prediction = pipeline.predict(pred_df)

        st.success(
            f"Predicted Maths Score: {float(prediction[0]):.3f}"
        )

        with st.expander("Input Data"):
            st.dataframe(pred_df)

    except Exception as e:
        st.error(f"Error: {e}")