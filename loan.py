import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model=joblib.load('loan.joblib')
Gender=st.number_input('enter gender Male:0,Female:1')
Married=st.number_input('enter martial status Married:1 Unmarried:0')
income=st.number_input('enter applicant income thousands')
la=st.number_input('enter loan amount in thousands')
if st.button('predict approval'):
    prediction=model.predict([[Gender,Married,income,la]])
    if prediction=='y':
        st.text('Loan approved')
    else:
        st.text('Loan Rejected')
