# 🎓 ACAD-PREDICTOR
### Student Performance & Academic Support Predictor

An AI-powered Machine Learning application designed to estimate students' academic performance and identify students who may benefit from additional academic support.

**Developed by:** Abdul Whajidh  
**Organization:** Career Solutions  
**Domain:** Machine Learning  
**Project Duration:** 10 Working Days

---

## 📌 Overview

ACAD-PREDICTOR is a machine learning-based academic decision-support system that predicts a student's potential final examination score and identifies whether the student may require additional academic support.

The system analyzes five important academic indicators to generate two independent predictions:

1. **Academic Score Prediction:** Estimates the student's final examination score on a scale of 0–100.
2. **Academic Support Prediction:** Identifies whether the student may require additional academic assistance.

The application provides an interactive interface built using Streamlit, allowing users to enter academic information and receive predictions instantly.

## 🎯 Problem Statement

Identifying students who may struggle academically before their final examinations is an important challenge for educational institutions.

Traditional approaches often depend on manual evaluation and final examination results, making early intervention difficult.

ACAD-PREDICTOR addresses this challenge by using machine learning to analyze available academic indicators and provide early insights that can help educators identify students who may benefit from additional support.

## ✨ Key Features

- **Final Score Prediction:** Estimates academic performance using machine learning.
- **Academic Support Identification:** Predicts potential academic support requirements.
- **Dual Prediction Models:** Uses separate regression and classification models.
- **Interactive Dashboard:** Simple and user-friendly Streamlit interface.
- **Real-Time Inference:** Generates predictions without retraining the models.
- **Input Validation:** Validates academic information before generating predictions.
- **Model Persistence:** Stores trained machine learning pipelines using Joblib.
- **Performance Evaluation:** Displays model evaluation metrics.
- **Responsible AI:** Designed as a decision-support tool rather than an automated decision-making system.

## ⚙️ Academic Parameters

The system uses five input parameters:

| Parameter | Description |
|---|---|
| Attendance Percentage | Student's attendance percentage |
| Weekly Study Hours | Average hours spent studying per week |
| Assignment Average | Average assignment performance |
| Previous Exam Score | Score obtained in previous examinations |
| Practice Tests Completed | Number of completed practice tests |

These parameters are used to generate the final academic predictions.

## 🧠 Machine Learning Methodology

The project implements two independent machine learning tasks.

### 1. Regression – Final Score Prediction

**Selected Algorithm:** Random Forest Regressor

Predicts the estimated final examination score on a scale of 0–100.

Model configuration:
- Number of estimators: 100
- Maximum depth: 10
- Minimum samples per leaf: 2
- Random state: 42

### 2. Classification – Academic Support Prediction

**Selected Algorithm:** Logistic Regression

Predicts whether a student may require academic support.

Output:
- 0 – Support not currently predicted.
- 1 – May require academic support.

The application also displays the estimated support probability.

### Algorithms Evaluated

The following algorithm families were considered:

- Linear Regression
- Logistic Regression
- Decision Tree
- Random Forest

The final regression and classification models were selected independently based on their respective validation results.

## 📊 Model Performance

The final models were evaluated using an 80/20 stratified train-test split.

**Regression Performance**

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 3.9383 |
| Root Mean Squared Error (RMSE) | 4.9630 |
| R² Score | 0.9576 |

**Classification Performance**

| Metric | Result |
|---|---:|
| Accuracy | 99.25% |
| Precision | 99.75% |
| Recall | 98.75% |
| F1-Score | 99.25% |
| ROC-AUC | 0.9998 |

**Important:** These results were obtained using a synthetic dataset. They demonstrate the functionality and reproducibility of the implemented machine learning workflow and do not establish real-world effectiveness.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning algorithms |
| Joblib | Model persistence |
| Streamlit | Interactive web application |
| Matplotlib / Seaborn | Data visualization |

## 📂 Project Structure

```text
ACAD-PREDICTOR/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── regression_model.joblib
│   └── classification_model.joblib
│
├── model_features.json
├── final_model_metrics.json
│
├── dataset/
│   └── synthetic_student_data.csv
│
├── README.md
└── .gitignore
```

*Note: This is a suggested organizational structure. Adjust the filenames and folders to match the actual repository.*

## 🚀 Installation and Setup

Follow these steps to run ACAD-PREDICTOR locally.

### Prerequisites

- Python 3.9 or later
- pip package manager
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Abdulwhajidh/ACAD-PREDICTOR.git
```

### Step 2: Navigate to the Project Directory

```bash
cd ACAD-PREDICTOR
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your default browser.

## 🔍 Application Workflow

The application follows a simple four-step process:

1. **Enter Inputs:** Provide the student's academic information.
2. **Validate Inputs:** Verify that the entered values are within acceptable ranges.
3. **Generate Predictions:** Execute both saved machine learning pipelines.
4. **Display Results:** Show the estimated final score and academic support probability.

## ⚠️ Dataset and Responsible AI Disclaimer

This project uses a synthetic dataset containing 4,000 records generated with random seed 42.

The dataset was created for educational and experimental purposes because verified anonymized historical student records were unavailable.

Therefore:

- Model performance should not be interpreted as real-world accuracy.
- Predictions should not be used as the sole basis for academic decisions.
- Academic support recommendations require human review.
- Real-world deployment requires validation using appropriate anonymized historical data.
- Privacy, fairness and responsible data handling must be considered before institutional deployment.

**ACAD-PREDICTOR is an academic decision-support prototype, not a replacement for educators or institutional decision-making.**

## 🔮 Future Enhancements

- Integration with real-world anonymized academic datasets.
- Advanced model explainability.
- Student-wise performance analytics.
- Historical academic performance tracking.
- Cohort-level performance visualization.
- Fairness evaluation across different student groups.
- Integration with institutional academic management systems.
- Improved intervention recommendations.

## 👨‍💻 Author

**Abdul Whajidh**

Machine Learning Intern | Computer Science Engineering Student

Developed as an internship project at **Career Solutions**.

## 📜 License

This project is intended for educational and research purposes. A formal open-source license can be added separately if required.
 
---

⭐ If you find this project interesting, consider giving this repository a star!
