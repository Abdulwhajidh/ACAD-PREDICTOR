import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
REGRESSION_FILE = BASE_DIR / "final_regression.joblib"
CLASSIFICATION_FILE = BASE_DIR / "final_classification.joblib"
FEATURES_FILE = BASE_DIR / "model_features.json"
METRICS_FILE = BASE_DIR / "final_model_metrics.json"


st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)


@st.cache_resource
def load_models():
    regression_model = joblib.load(REGRESSION_FILE)
    classification_model = joblib.load(CLASSIFICATION_FILE)
    return regression_model, classification_model


@st.cache_data
def load_project_files():
    with open(FEATURES_FILE, "r", encoding="utf-8") as file:
        feature_columns = json.load(file)

    metrics = {}
    if METRICS_FILE.exists():
        with open(METRICS_FILE, "r", encoding="utf-8") as file:
            metrics = json.load(file)

    return feature_columns, metrics


def validate_inputs(
    attendance,
    study_hours,
    assignment_average,
    previous_exam_score,
    practice_tests
):
    errors = []

    if not 0 <= attendance <= 100:
        errors.append("Attendance must be between 0 and 100.")

    if not 0 <= study_hours <= 60:
        errors.append("Study hours per week must be between 0 and 60.")

    if not 0 <= assignment_average <= 100:
        errors.append("Assignment average must be between 0 and 100.")

    if not 0 <= previous_exam_score <= 100:
        errors.append("Previous exam score must be between 0 and 100.")

    if practice_tests < 0:
        errors.append("Practice tests completed cannot be negative.")

    if int(practice_tests) != practice_tests:
        errors.append("Practice tests completed must be a whole number.")

    return errors


st.title("Student Performance & Academic Support Predictor")
st.write(
    "Enter pre-assessment student information to estimate the final score "
    "and identify possible academic-support needs."
)

st.info(
    "This application uses a synthetic dataset generated with random seed 42. "
    "The results demonstrate a machine-learning workflow and do not establish "
    "real-world effectiveness."
)

try:
    regression_model, classification_model = load_models()
    feature_columns, saved_metrics = load_project_files()
except FileNotFoundError as error:
    st.error(
        "A required model or configuration file is missing. Keep app.py, "
        "both .joblib files, model_features.json, and final_model_metrics.json "
        "in the same folder."
    )
    st.code(str(error))
    st.stop()
except Exception as error:
    st.error("The saved model files could not be loaded.")
    st.code(str(error))
    st.stop()


st.header("Student information")

col1, col2 = st.columns(2)

with col1:
    attendance = st.number_input(
        "Attendance percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

    assignment_average = st.number_input(
        "Assignment average",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )

    practice_tests = st.number_input(
        "Practice tests completed",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )

with col2:
    study_hours = st.number_input(
        "Study hours per week",
        min_value=0.0,
        max_value=60.0,
        value=20.0,
        step=0.5
    )

    previous_exam_score = st.number_input(
        "Previous exam score",
        min_value=0.0,
        max_value=100.0,
        value=65.0,
        step=0.1
    )


st.caption(
    "Observed training ranges: attendance 0–100, study hours 0–60, "
    "assignment average 0–100, previous exam score 0–100, and practice "
    "tests 0–10. Values outside the observed practice-test range may be "
    "accepted but should be interpreted cautiously."
)

if st.button("Generate prediction", type="primary", use_container_width=True):
    errors = validate_inputs(
        attendance,
        study_hours,
        assignment_average,
        previous_exam_score,
        practice_tests
    )

    if errors:
        for error in errors:
            st.error(error)
        st.stop()

    input_data = pd.DataFrame({
        "attendance_pct": [attendance],
        "study_hours_week": [study_hours],
        "assignment_avg": [assignment_average],
        "previous_exam_score": [previous_exam_score],
        "practice_tests_completed": [int(practice_tests)]
    })

    try:
        input_data = input_data[feature_columns]
        predicted_score = float(regression_model.predict(input_data)[0])
        predicted_class = int(classification_model.predict(input_data)[0])
        support_probability = float(
            classification_model.predict_proba(input_data)[0][1]
        )
    except Exception as error:
        st.error("Prediction failed. Check that the feature names match the saved models.")
        st.code(str(error))
        st.stop()

    st.header("Prediction results")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric("Predicted final score", f"{predicted_score:.2f} / 100")

    with result_col2:
        st.metric(
            "Support probability",
            f"{support_probability * 100:.2f}%"
        )

    with result_col3:
        st.metric(
            "Support prediction",
            "Needs support" if predicted_class == 1 else "No support predicted"
        )

    if predicted_class == 1:
        st.warning(
            "The classification model predicts that this student may need "
            "academic support. This is an early-risk signal, not a final decision."
        )
    else:
        st.success(
            "The classification model does not predict a current need for "
            "academic support. Continue monitoring the student."
        )

    if predicted_score < 0 or predicted_score > 100:
        st.warning(
            "The regression prediction is outside the valid 0–100 score range. "
            "It has not been silently clipped."
        )

    st.subheader("Input summary")
    st.dataframe(input_data, use_container_width=True, hide_index=True)


with st.expander("Model information"):
    st.write(
        "The regression model predicts the continuous final score. The "
        "classification model independently predicts the support class and "
        "the probability of class 1. Both models use the same five input features."
    )

    if saved_metrics:
        st.write("Saved final-model evaluation metrics:")
        st.json(saved_metrics)


with st.expander("Limitations and data disclosure"):
    st.markdown(
        """
        - The dataset is synthetic and was generated using random seed 42.
        - `practice_tests_completed` is synthetically generated and does not
          represent verified student activity.
        - The model outputs are educational predictions, not institutional,
          medical, legal, or disciplinary decisions.
        - Synthetic-data performance does not establish real-world effectiveness.
        - A support prediction should be reviewed by a qualified educator or
          coordinator before any intervention is made.
        """
    )
