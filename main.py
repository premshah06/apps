import streamlit as st
from streamlit_option_menu import option_menu
from diabetes_predict import diabetes_predict
import pandas as pd
from heart_disease_data import heart_disease_data
from heart_info import heart_info

# page config
st.set_page_config(
    page_title="Diabetes & Heart Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home","Diabetes","Heart Problems","Heart Disease"],
            icons=['house','person','activity','heart'], menu_icon="heart", default_index=0)

    if selected == "Home":
        st.markdown("""
        <style>
            body {
                background-image: url('https://img.freepik.com/premium-vector/vector-illustration-flat-colored-icons-with-long-shadows-abstract-medicine-background-with-medical-health-healthcare-doctor-pills-cross-symbols-design-elements-mobile-web-applications_724904-812.jpg?w=2000');
                background-size: cover;
                background-position: center;
                height: 100vh;
            }
        </style>
        """, unsafe_allow_html=True)

        st.title("Welcome to our Diabetes and Heart Prediction Website!")

        st.markdown("""
        <div style="display: flex; align-items: center;">
        <div style="flex: 1;">
                    <br>
                    <br>
            <p style="font-size: 18px; font-weight: bold; text-align: justify;">
                In today's world, the prevalence of these conditions has risen significantly, leading to unfortunate outcomes for many individuals.
                Our mission is to tackle this challenge head-on by empowering you with knowledge about your health.
            </p>
            <p style="font-size: 18px; font-weight: bold; text-align: justify;">
                We understand that these diseases can be concerning, but worry not. Our user-friendly platform is designed to provide you with a reliable prediction of your health status based on the symptoms you might be experiencing.<br><br>
                Instead of wondering and waiting, you can now take a proactive step towards your well-being from the comfort of your home.
            </p>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="https://img.freepik.com/premium-vector/vector-illustration-flat-colored-icons-with-long-shadows-abstract-medicine-background-with-medical-health-healthcare-doctor-pills-cross-symbols-design-elements-mobile-web-applications_724904-812.jpg?w=2000" alt="Attractive Image" style="max-width: 50%; border-radius: 10px;">
        </div>
        </div>
        """, unsafe_allow_html=True)
        
    elif selected == "Diabetes":
       diabetes_predict()
    elif selected == "Heart Disease":
        heart_disease_data()
    elif selected == "Heart Problems":
        heart_info()
        

if __name__ == "__main__":
    main()
