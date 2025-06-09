import pickle 
import pandas as pd
import streamlit as st

with open('model_Final.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

#list key untuk semua input
input_keys = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
              'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Inisialisasi session_state
for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = ''

st.title('Klasifikasi Diabetes🧬')

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('input nilai pregnancies', key='Pregnancies')
    Glucose = st.text_input('input nilai Glucose', key='Glucose')
    BloodPressure = st.text_input('input nilai BloodPressure', key='BloodPressure')
    SkinThickness = st.text_input('input nilai SkinThickness', key='SkinThickness')

with col2:
    Insulin = st.text_input('input nilai Insulin', key='Insulin')
    BMI = st.text_input('input nilai BMI', key='BMI')
    DiabetesPedigreeFunction = st.text_input('input nilai DiabetesPedigreeFunction', key='DiabetesPedigreeFunction')
    Age = st.text_input('input nilai Age', key='Age')

diab_diagnosis = ''

with col1:
    if st.button('test klasifikasi diabetes'):
        try:
            input_data = [[
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]]
            input_df = pd.DataFrame(input_data, columns=input_keys)
            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'pasien terkena diabetes'
            else:
                diab_diagnosis = 'pasien tidak terkena diabetes'
            st.success(diab_diagnosis)

        except ValueError:
            st.error('Mohon masukkan semua nilai input dengan benar (angka).')

with col2:
    if st.button('clear'):
        st.session_state.clear()
        st.rerun()