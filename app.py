import numpy as np
import pandas as pd
import pickle

import streamlit as st

from PIL import Image

pickle_in = open('gnb.pkl',"rb")

classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome to Mental Health App"


def predict_note_authentication(age, gender, family_history, benefits, care_options, anonymity, leave, work_interfere):
    prediction = classifier.predict([[age, gender, family_history, benefits, care_options, anonymity, leave, work_interfere]])
    print(prediction)
    return prediction

def main():
    st.title("ML Mini-Project")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Mental Health Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.slider("age")

    gender_mapping = {'Female': 0, 'Male': 1, 'Trans': 2}
    selected_gender = st.selectbox("gender",('Female', 'Male', 'Trans'),index=None)
    if selected_gender != None:
        gender = gender_mapping[selected_gender]

    family_history_mapping = {'No': 0, 'Yes': 1}
    selected_family_history = st.radio("Do you have a family history of mental illness?", ('No', 'Yes'),index=None)
    if selected_family_history != None:
        family_history = family_history_mapping[selected_family_history]

    benefits_mapping = {"Don't know": 0, 'No': 1, 'Yes': 2}
    selected_benefits = st.radio("Does your employer provide mental health benefits?", ("Don't know", 'No', 'Yes'),index=None)
    if selected_benefits is not None:
        benefits = benefits_mapping[selected_benefits]

    care_options_mapping = {'No': 0, 'Not sure': 1, 'Yes': 2}
    selected_care_options = st.radio("Do you know the options for mental health care your employer provides?", ('No', 'Not sure', 'Yes'),index=None)
    if selected_care_options is not None:
        care_options = care_options_mapping[selected_care_options]

    anonymity_mapping = {"Don't know": 0, 'No': 1, 'Yes': 2}
    selected_anonymity = st.radio(" Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?", ( 'No', "Don't know", 'Yes'),index=None)
    if selected_anonymity is not None:
        anonymity = anonymity_mapping[selected_anonymity]

    leave_mapping = {"Don't know": 0, 'Somewhat difficult': 1, 'Somewhat easy': 2, 'Very difficult': 3, 'Very easy': 4}
    selected_leave = st.select_slider("How easy is it for you to take medical leave for a mental health condition?",options=['Very difficult','Somewhat difficult',"Don't know",  'Somewhat easy', 'Very easy'])
    if selected_leave is not None:
        leave = leave_mapping[selected_leave]

    work_interfere_mapping = {"Don't know": 0, 'Never': 1, 'Often': 2, 'Rarely': 3, 'Sometimes': 4}
    selected_work_interfere = st.select_slider(" If you have a mental health condition, do you feel that it interferes with your work?",options=[ 'Never', 'Rarely',"Don't know",  'Sometimes','Often'])
    if selected_work_interfere is not None:
        work_interfere = work_interfere_mapping[selected_work_interfere]

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age, gender, family_history, benefits, care_options, anonymity, leave, work_interfere)
        if(result==1):
            st.error('You Need to seek Help.')
        else:
            st.success('You Seem Fine ;)')
    st.text("Mental Health is as important as Physical Health.")
    st.caption(
        "Get 24x7 x 365 free counselling for depression, anxiety and other mental health- concerns. Call or whatsApp at +919999666555.")
    if st.button("About"):
        st.text("Machine Learning Mini-Project")
        st.text("Team Members:")
        st.caption("Atharva Nawadkar")
        st.caption("Anjali Parwani")
        st.caption("Abhishek Pattanayak")


if __name__ == '__main__':
    main()
