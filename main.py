import streamlit as st
from streamlit_option_menu import option_menu
from diabetes_predict import diabetes_predict
import pandas as pd
from heart_disease_data import heart_disease_data

# page config
st.set_page_config(
    page_title="Diabetes & Heart Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Diabetes",'Heart Disease'],
            icons=['house', "file-earmark-medical",'activity'], menu_icon="heart", default_index=0)

    if selected == "Home":
        st.title("Diabetes and Heart Detection Website")
        st.image("heart.jpg", 
         use_column_width=True,
         caption="Image by John Doe",
         style={"border": "2px solid #000", 
                "border-radius": "10px",
                "box-shadow": "0px 5px 10px rgba(0, 0, 0, 0.2)"})
        st.markdown("""
    <div style="text-align: center;">
        <h2>Welcome to our Diabetes and Heart Prediction Website!</h2>
        <p>In today's world, the prevalence of these conditions has risen significantly, leading to unfortunate outcomes for many individuals. Our mission is to tackle this challenge head-on by empowering you with knowledge about your health.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center;">
        <p>We understand that these diseases can be concerning, but worry not. Our user-friendly platform is designed to provide you with a reliable prediction of your health status based on the symptoms you might be experiencing.</p>
        <p>Instead of wondering and waiting, you can now take a proactive step towards your well-being from the comfort of your home.</p>
    </div>
    """, unsafe_allow_html=True)
        st.markdown(
            """<style>.css-1aumxhk{background-color: #f0f8ff;}</style>""", unsafe_allow_html=True
        )  # Apply custom CSS to the background color
    elif selected == "Diabetes":
        diabetes_predict()
    elif selected == "Heart Disease":
        heart_disease_data()

if __name__ == "__main__":
    main()
