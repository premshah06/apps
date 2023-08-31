import streamlit as st
from streamlit_option_menu import option_menu
from diabetes_predict import diabetes_predict
import pandas as pd
from heart_disease_data import heart_disease_data

# page config
st.set_page_config(
    page_title="My App",
    page_icon=":smiley:",
    layout="wide", # wide or center
    initial_sidebar_state="expanded",
)

def main():
    

# Print the value of my_variable
     
    # streamit option menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Diabetes",'Heart Disease'], 
            icons=['house', "file-earmark-medical",'activity'], menu_icon="cast", default_index=0)
    
    if selected == "Home":
        st.title("Diabetes and Heart detection website")
        st.write("""Welcome to our Diabetes and Heart Disease Prediction Website! In today's world, the prevalence of these conditions has risen significantly, leading to unfortunate outcomes for many individuals. Our mission is to tackle this challenge head-on by empowering you with knowledge about your health.

We understand that these diseases can be concerning, but worry not. Our user-friendly platform is designed to provide you with a reliable prediction of your health status based on the symptoms you might be experiencing. Instead of wondering and waiting, you can now take a proactive step towards your well-being from the comfort of your home.

Our cutting-edge prediction model has been meticulously developed to ensure accuracy. By inputting your symptoms into our interactive system, you'll receive a personalized assessment of your condition's likelihood. This doesn't replace professional medical advice, but it does serve as a valuable tool to help you make informed decisions about your health.

Your health matters, and we're here to assist you on your journey to a healthier life. Together, let's empower ourselves with knowledge, take charge of our well-being, and work towards a future where preventable diseases no longer claim lives. Start your prediction now and take a step towards a healthier future!""")
        # diabetes_dataset = pd.read_csv("./diabetes-dataset-cleaned.csv")
        # diabetes_dataset = diabetes_dataset.drop(columns = 'Pdiabetes', axis=1)
        # diabetes_dataset=diabetes_dataset.dropna(axis=0)
        # accuracy = sendaccuracy(diabetes_dataset)
        # st.write("Accuracy of the model is: ", round((accuracy*100),2))
    elif selected == "Diabetes":
        diabetes_predict()
    elif selected == "Heart Disease":
        heart_disease_data()
    # elif selected == "Settings":
        # st.title("Settin

if __name__ == "__main__":
    main()
