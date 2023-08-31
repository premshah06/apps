import streamlit as st
import pandas as pd
import seaborn as sns

# Set up Streamlit page configuration
st.set_page_config(page_title="Heart Failure Prediction and Information")

# Load the dataset
heart_data = pd.read_csv("heart_failure_clinical_records_dataset.csv")

# Display basic information about the dataset
st.title("Heart Failure Prediction and Information")
st.subheader("Heart Failure Dataset Information")
st.write("This dataset contains clinical records of people and whether they have experienced heart failure.")
st.write("Number of records:", len(heart_data))
st.write("Number of features:", len(heart_data.columns))

# Display the first few rows of the dataset
st.subheader("Sample Data")
st.dataframe(heart_data.head())

# Visualize the distribution of heart failure cases
st.subheader("Heart Failure Cases Distribution")
heart_failure_counts = heart_data["DEATH_EVENT"].value_counts()
st.bar_chart(heart_failure_counts)

# Provide information about heart problems
st.subheader("Understanding Heart Problems")
st.write(
    "Heart problems can occur due to various factors such as high blood pressure, "
    "cholesterol, smoking, obesity, and lack of physical activity. Heart failure is a "
    "serious condition where the heart cannot pump blood effectively, leading to symptoms "
    "like shortness of breath, fatigue, and fluid retention. It's important to maintain a "
    "healthy lifestyle, including a balanced diet and regular exercise, to reduce the risk of heart problems."
)
