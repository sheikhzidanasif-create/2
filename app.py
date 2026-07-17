
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("%%writefile /content/app.py

import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("/content/student_model.pkl")

st.title("🎓 Student Performance Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.slider("Study Hours", 0, 12, 5)

gender = 1 if gender == "Male" else 0

if st.button("Predict"):
    data = np.array([[gender, study_hours]])
    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])
Agar VS Code use kar rahe ho")

st.title("🎓 Student Performance Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.slider("Study Hours", 0, 12, 5)

gender = 1 if gender == "Male" else 0

if st.button("Predict"):
    data = np.array([[gender, study_hours]])
    prediction = model.predict(data)

    st.write("Prediction:", prediction[0])


                    from google.colab import files
files.download('/content/app.py')
