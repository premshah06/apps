import streamlit as st
import pandas as pd
import seaborn as sns


def heart_info():
    # Load the dataset
    heart_data = pd.read_csv("heart.csv")

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
    heart_failure_counts = heart_data["HeartDisease"].value_counts()
    heart_failure_counts.index = ["Not detected", "Detected"]  # Rename the indices

    # Adjust the size of the graph
    plt.figure(figsize=(6, 4))

    # Create the bar chart
    st.bar_chart(heart_failure_counts, use_container_width=True)

    # Customize the y-axis intervals and x-axis labels
    plt.yticks(range(0, max(heart_failure_counts) + 1, 200))
    plt.xticks(rotation=45, ha="right")

    # Provide information about heart problems
    st.subheader("Understanding Heart Problems")
    st.write(
        "Heart problems can occur due to various factors such as high blood pressure, "
        "cholesterol, smoking, obesity, and lack of physical activity. Heart failure is a "
        "serious condition where the heart cannot pump blood effectively, leading to symptoms "
        "like shortness of breath, fatigue, and fluid retention. It's important to maintain a "
        "healthy lifestyle, including a balanced diet and regular exercise, to reduce the risk of heart problems."
    )
