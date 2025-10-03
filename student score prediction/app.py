import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
pipeline = joblib.load("best_pipeline.joblib")

# Page configuration
st.set_page_config(
    page_title="🎓 Student Performance Predictor",
    page_icon="📊",
    layout="wide"
)

# --- Header ---
st.markdown("""
    <div style='background-color:#4CAF50;padding:10px;border-radius:10px'>
        <h1 style='color:white;text-align:center;'>🎓 Student Performance Prediction App</h1>
    </div>
""", unsafe_allow_html=True)

st.write("Fill in the student's details below to predict their academic performance.")

st.markdown("---")

# --- Inputs in two columns for better UI ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🧒 Age", min_value=10, max_value=30, value=18)
    gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])
    study_hours_per_day = st.slider("📚 Study Hours per Day", 0, 12, 4)
    social_media_hours = st.slider("📱 Social Media Hours per Day", 0, 12, 2)
    netflix_hours = st.slider("🎬 Netflix/OTT Hours per Day", 0, 12, 1)
    part_time_job = st.selectbox("💼 Part-time Job", ["Yes", "No"])
    attendance_percentage = st.slider("📈 Attendance Percentage", 0, 100, 85)

with col2:
    sleep_hours = st.slider("💤 Sleep Hours per Day", 0, 12, 7)
    diet_quality = st.selectbox("🥗 Diet Quality", ["Poor", "Fair", "Good"])
    exercise_frequency = st.slider("🏃 Exercise Frequency (0=Never, 6=Daily)", 0, 6, 2)
    parental_education_level = st.selectbox("🎓 Parental Education Level", ["High School", "Bachelor", "Master"])
    internet_quality = st.selectbox("🌐 Internet Quality", ["Poor", "Average", "Good"])
    mental_health_rating = st.slider("🧠 Mental Health Rating (1=Low, 10=High)", 1, 10, 5)
    extracurricular_participation = st.selectbox("🎨 Extracurricular Participation", ["Yes", "No"])

st.markdown("---")

# --- Prediction button ---
if st.button("Predict Performance"):
    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "study_hours_per_day": [study_hours_per_day],
        "social_media_hours": [social_media_hours],
        "netflix_hours": [netflix_hours],
        "part_time_job": [part_time_job],
        "attendance_percentage": [attendance_percentage],
        "sleep_hours": [sleep_hours],
        "diet_quality": [diet_quality],
        "exercise_frequency": [exercise_frequency],
        "parental_education_level": [parental_education_level],
        "internet_quality": [internet_quality],
        "mental_health_rating": [mental_health_rating],
        "extracurricular_participation": [extracurricular_participation]
    })

    prediction = pipeline.predict(input_data)[0]
    prediction = max(0, min(100, prediction))
    
    st.markdown(f"""
        <div style='background-color:#2196F3;padding:15px;border-radius:10px'>
            <h2 style='color:white;text-align:center;'>🎯 Predicted Academic Score: {prediction:.2f}</h2>
        </div>
    """, unsafe_allow_html=True)



