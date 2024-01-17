import streamlit as st
import joblib

model = joblib.load("heart_ml.h5")

st.title("Heart Disease Prediction App")
st.header('This app predicts if a perspm has heart disease')




age = st.number_input('Enter your Age')
sex = st.radio('sex',(0,1))
cp = st.radio('chest pain type',(0,1,2,3))
tres = st.number_input("Resting blood pressure:")
chol = st.number_input('serum cholestrol in mg/dl:')
fbs = st.radio('Fasting blood sugar',(0,1))
res = st.number_input('Resting electorcardiographic results:')
tha = st.number_input('Maximun heart rate achied')
exa = st.radio ('Excercise iduced angina:', (0,1))
old = st.number_input('oldpeak')
slope = st.number_input('he slope of the peak excercise ST segmen:')
ca = st.radio('number of major vessels',(0,1,23))
thal =st.radio('thal',(0,1,2,3))

if st.button("Predict"):
    st.success("Thanks")
    prediction = model.predict([[age,sex,cp,tres,chol,fbs,res,tha,exa,old,slope,ca,thal]])
    st.success(prediction)