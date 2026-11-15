# ACAD-PREDICTOR

**Student Performance & Academic Support Predictor**

ACAD-PREDICTOR is a small machine learning app that does two things: it estimates a student's final exam score (out of 100), and it flags whether that student might need extra academic support.

I built it as my internship project at Career Solutions (Machine Learning domain) over 10 working days. The interface is a Streamlit app, so you type in a few numbers and get results straight away.

**Author:** Abdul Whajidh

---

## Why I built this

By the time final exam results come out, it's usually too late to help a student who was struggling. Most schools and colleges still rely on manual checks or on the results themselves, which makes early help hard.

This project tries a different angle: take a few academic indicators that are already available during the semester and use them to give teachers an early signal. It's meant to help a teacher notice who might need a conversation, not to make the decision for them.

## What it does

- Predicts a final score from 0 to 100
- Predicts whether a student may need academic support, and shows the probability
- Uses two separate models, a regression model for the score and a classification model for support
- Checks that your inputs are in a sensible range before predicting
- Runs predictions instantly from saved models, with no retraining needed
- Shows the evaluation metrics for both models

## The five inputs

| Input | What it means |
|---|---|
| Attendance Percentage | How much of the time the student attends class |
| Weekly Study Hours | Average hours studied per week |
| Assignment Average | Average performance across assignments |
| Previous Exam Score | Score from earlier examinations |
| Practice Tests Completed | How many practice tests the student has done |

## How the models work

I treated this as two independent problems.

**1. Final score (regression)**
I used a Random Forest Regressor with these settings: 100 estimators, max depth of 10, minimum 2 samples per leaf, random state 42.

**2. Academic support (classification)**
I used Logistic Regression. It outputs 0 if support isn't currently predicted and 1 if the student may need support. The app also shows the estimated probability.

I tried Linear Regression, Logistic Regression, Decision Tree and Random Forest. I picked the final regression and classification models separately, based on how each did on validation.

## Results

I evaluated the final models on an 80/20 stratified train-test split.

**Regression**

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 3.9383 |
| Root Mean Squared Error (RMSE) | 4.9630 |
| R² Score | 0.9576 |

**Classification**

| Metric | Result |
|---|---:|
| Accuracy | 99.25% |
| Precision | 99.75% |
| Recall | 98.75% |
| F1-Score | 99.25% |
| ROC-AUC | 0.9998 |

**Please read this before getting excited about the numbers:** the data is synthetic. These results show that the pipeline works and can be reproduced. They say nothing about how well it would do on real students.

## Tech stack

- **Python** for everything
- **Pandas** and **NumPy** for data handling and numerical work
- **Scikit-learn** for the models
- **Joblib** to save and load the trained pipelines
- **Streamlit** for the web app
- **Matplotlib** and **Seaborn** for charts

## Project structure

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

This is the layout I'd suggest. Adjust the names to match your own copy of the repo.

## Running it locally

You'll need Python 3.9 or later, pip, and Git.

1. Clone the repo:
   ```bash
   git clone https://github.com/Abdulwhajidh/ACAD-PREDICTOR.git
   ```
2. Move into the folder:
   ```bash
   cd ACAD-PREDICTOR
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
   On Windows, activate it with:
   ```bash
   .venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python -m streamlit run app.py
   ```

It should open in your browser automatically.

## How the app flows

1. You enter the student's academic details.
2. The app checks that the values are within acceptable ranges.
3. Both saved models run on those inputs.
4. You see the estimated final score and the support probability.

## About the data (important)

The dataset is synthetic: 4,000 records generated with random seed 42. I made it because I didn't have access to verified, anonymized student records.

Because of that:

- Don't read the model scores as real-world accuracy.
- Don't use the predictions as the only basis for any academic decision.
- Any support recommendation should be reviewed by a person.
- Before real deployment, the models would need to be validated on proper anonymized historical data.
- Privacy, fairness and responsible data handling need to be sorted out first.

ACAD-PREDICTOR is a prototype that supports decisions. It is not a replacement for teachers or institutions.

## What I'd like to add next

- Training on real anonymized academic data
- Better explanations for why a prediction came out the way it did
- Performance analytics for individual students
- Tracking performance over time
- Cohort-level visualizations
- Fairness checks across different student groups
- Integration with institutional academic management systems
- Better suggestions for how to help flagged students

## License

This project is for educational and research purposes. A formal open-source license can be added later if needed.

---

If you found this interesting, a star on the repo would mean a lot.
