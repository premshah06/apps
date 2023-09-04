import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Function to create a hoverable info box
def create_info_box(text):
    st.write('<div class="info-box">' + text + '</div>', unsafe_allow_html=True)

# Add CSS styling
st.markdown(
    """
    <style>
    .info-box {
        position: absolute;
        background-color: #f9f9f9;
        color: #333;
        padding: 5px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 12px;
        max-width: 300px;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the heart disease data
heart_data = pd.read_csv("heart_disease_data.csv")

def heart_disease_data():
    st.title("Heart Disease Prediction")
    
    criteria_info = {
        'Age': 'Enter your age in years.',
        'Sex': 'Select your gender.',
        'Chest Pain': 'Choose the type of chest pain you are experiencing.',
        'Resting Blood Pressure': 'Enter your resting blood pressure.',
        'Serum Cholestoral': 'Enter your serum cholestoral level.',
        'Fasting Blood Sugar': 'Select if your fasting blood sugar is above 120 mg/dl.',
        'Resting Electrocardiographic Results': 'Choose your resting electrocardiographic results.',
        'Maximum Heart Rate Achieved': 'Enter your maximum heart rate achieved.',
        'Exercise Induced Angina': 'Select if you have exercise-induced angina.',
        'ST Depression Induced by Exercise': 'Enter the ST depression induced by exercise relative to rest.',
        'Slope of the Peak Exercise ST Segment': 'Choose the slope of the peak exercise ST segment.',
        'Number of Major Vessels': 'Enter the number of major vessels colored by flourosopy.',
        'Thalassemia': 'Choose your thalassemia category.',
    }

    st.write(
        "Fill in the following details to predict whether you have heart disease or not."
    )

    age = st.number_input("Age", min_value=0, max_value=100, value=0, help=criteria_info.get('Age', ''))
    
    gender = st.selectbox("Sex", options=['male', 'female'], help=criteria_info.get('Sex', ''))
    

    cp = st.number_input("Chest Pain", min_value=0, max_value=4, value=0, help=criteria_info.get('Chest Pain', ''))
    

    trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, value=0, help=criteria_info.get('Resting Blood Pressure', ''))
    

    chol = st.number_input("Serum Cholestoral", min_value=0, max_value=600, value=0, help=criteria_info.get('Serum Cholestoral', ''))


    fbs = st.number_input("Fasting Blood Sugar", min_value=0, max_value=1, value=0, help=criteria_info.get('Fasting Blood Sugar', ''))


    restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2, value=0, help=criteria_info.get('Resting Electrocardiographic Results', ''))
    

    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=200, value=0, help=criteria_info.get('Maximum Heart Rate Achieved', ''))
    

    exang = st.number_input("Exercise Induced Angina", min_value=0, max_value=1, value=0, help=criteria_info.get('Exercise Induced Angina', ''))
    

    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.2, value=0.0, help=criteria_info.get('ST Depression Induced by Exercise', ''))
    

    slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2, value=0, help=criteria_info.get('Slope of the Peak Exercise ST Segment', ''))
    

    ca = st.number_input("Number of Major Vessels", min_value=0, max_value=4, value=0, help=criteria_info.get('Number of Major Vessels', ''))
    

    thal = st.number_input("Thalassemia", min_value=0, max_value=3, value=0, help=criteria_info.get('Thalassemia', ''))
    

    
    input_data = np.array([age, gender == 'female', cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1).astype(float)

    
    model = LogisticRegression()
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=10)
    model.fit(X_train, Y_train)

    
    prediction = model.predict(input_data)

    
    if st.button("Predict"):
        if prediction[0] == 0:
            st.success('The person does not have heart disease.')
            st.balloons()
        else:
            st.error('The person has heart disease.')


if __name__ == "__main__":
    heart_disease_data()
