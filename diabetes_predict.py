import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def diabetes_predict():
    st.title("Diabetes Risk Prediction")

    # Load the diabetes dataset
    diabetes_dataset = pd.read_csv("diabetes-dataset-Cleaned.csv")
    diabetes_dataset = diabetes_dataset.drop(columns='Pdiabetes', axis=1)
    diabetes_dataset = diabetes_dataset.dropna(axis=0)

    # Create placeholders and selectboxes with hints for user input

    # Age
    Age_select = st.selectbox("Age", ['Select', 'Less than 40', '40-49', '50-59', 'Greater than 60'], index=0, help="Select your age group.")

    # Gender
    Gender_select = st.selectbox("Gender", ['Select', 'Male', 'Female'], index=0, help="Select your gender.")

    # Family Diabetes History
    Family_Diabetes_select = st.selectbox("Family Diabetes History", ['Select', 'No', 'Yes'], index=0, help="Does your family have a history of diabetes?")

    # High Blood Pressure
    highBP_select = st.selectbox("High Blood Pressure", ['Select', 'No', 'Yes'], index=0, help="Do you have high blood pressure?")

    # Physical Activity Level
    PhysicallyActive_select = st.selectbox("Physical Activity Level", ['Select', 'Not at all', 'Less than Half hr.', 'More than Half hr.', '1 hr. or more'], index=0, help="Select your physical activity level.")

    # BMI
    BMI = st.number_input("BMI", min_value=0.0, max_value=100.0, value=0.0, help="Enter your Body Mass Index (BMI).")

    # Smoking
    Smoking_select = st.selectbox("Smoking", ['Select', 'No', 'Yes'], index=0, help="Do you smoke?")

    # Alcohol Consumption
    Alcohol_select = st.selectbox("Alcohol Consumption", ['Select', 'No', 'Yes'], index=0, help="Do you consume alcohol?")

    # Sleep
    Sleep = st.number_input("Sleep (hours)", min_value=0, max_value=12, value=0, help="Enter your daily sleep duration in hours.")

    # Sound Sleep
    SoundSleep = st.number_input("Sound Sleep (hours)", min_value=0, max_value=12, value=0, help="Enter your daily sound sleep duration in hours.")

    # Regular Medicine
    RegularMedicine_select = st.selectbox("Regular Medicine", ['Select', 'No', 'Yes'], index=0, help="Do you take regular medication?")

    # Junk Food Consumption
    JunkFood_select = st.selectbox("Junk Food Consumption", ['Select', 'Occasional', 'Often', 'Very Often'], index=0, help="How often do you consume junk food?")

    # Stress Level
    Stress_select = st.selectbox("Stress Level", ['Select', 'Not at all', 'Sometimes', 'Very Often', 'Always'], index=0, help="Select your stress level.")

    # Blood Pressure Level
    BPLevel_select = st.selectbox("Blood Pressure Level", ['Select', 'Normal', 'Low', 'High'], index=0, help="Select your blood pressure level.")

    # Pregnancies
    Pregancies = st.number_input("Pregnancies (0-3)", min_value=0, max_value=3, value=0, help="Enter the number of pregnancies (0-3) for females.")

    # Urination Frequency
    UriationFreq_select = st.selectbox("Urination Frequency", ['Select', 'Not much', 'Very often'], index=0, help="Select your urination frequency.")

    # Check if the user has provided all inputs
    if st.button("Predict"):
        if (
            Age_select == 'Select' or
            Gender_select == 'Select' or
            Family_Diabetes_select == 'Select' or
            highBP_select == 'Select' or
            PhysicallyActive_select == 'Select' or
            Smoking_select == 'Select' or
            Alcohol_select == 'Select' or
            RegularMedicine_select == 'Select' or
            JunkFood_select == 'Select' or
            Stress_select == 'Select' or
            BPLevel_select == 'Select' or
            UriationFreq_select == 'Select'
        ):
            st.error("Please select values for all input fields.")
        else:
            # Map selectbox values to numerical values
            Age = {'Less than 40': 0, '40-49': 1, '50-59': 2, 'Greater than 60': 3}[Age_select]
            Gender = {'Male': 0, 'Female': 1}[Gender_select]
            Family_Diabetes = {'No': 0, 'Yes': 1}[Family_Diabetes_select]
            highBP = {'No': 0, 'Yes': 1}[highBP_select]
            PhysicallyActive = {'Not at all': 0, 'Less than Half hr.': 1, 'More than Half hr.': 2, '1 hr. or more': 3}[PhysicallyActive_select]
            Smoking = {'No': 0, 'Yes': 1}[Smoking_select]
            Alcohol = {'No': 0, 'Yes': 1}[Alcohol_select]
            RegularMedicine = {'No': 0, 'Yes': 1}[RegularMedicine_select]
            JunkFood = {'Occasional': 0, 'Often': 1, 'Very Often': 2}[JunkFood_select]
            Stress = {'Not at all': 0, 'Sometimes': 1, 'Very Often': 2, 'Always': 3}[Stress_select]
            BPLevel = {'Normal': 0, 'Low': 1, 'High': 2}[BPLevel_select]
            UriationFreq = {'Not much': 0, 'Very often': 1}[UriationFreq_select]

            # Create a feature array
            input_data = np.array([Age, Gender, Family_Diabetes, highBP, PhysicallyActive, BMI, Smoking, Alcohol, Sleep, SoundSleep, RegularMedicine, JunkFood, Stress, BPLevel, Pregancies, UriationFreq]).reshape(1, -1)

            # Load the trained model and scaler
            classifier = svm.SVC(kernel='linear')
            scaler = StandardScaler()
            X = diabetes_dataset.drop(columns='Diabetic', axis=1)
            Y = diabetes_dataset['Diabetic']
            scaler.fit(X)

            # Standardize the input data
            input_data_std = scaler.transform(input_data)

            # Fit the model and make a prediction
            classifier.fit(X, Y)
            prediction = classifier.predict(input_data_std)

            # Display the prediction
            if prediction[0] == 0:
                st.success("You are not diabetic.")
                st.balloons()
            else:
                st.error("You are diabetic.")

if __name__ == "__main__":
    diabetes_predict()
