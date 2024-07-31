
import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Define input function
def user_input():
    age = st.number_input("Age", min_value=18, max_value=66, value=30)
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    bp_problems = st.selectbox("Blood Pressure Problems", ["No", "Yes"])
    transplants = st.selectbox("Any Transplants", ["No", "Yes"])
    chronic_diseases = st.selectbox("Any Chronic Diseases", ["No", "Yes"])
    height = st.number_input("Height (cm)", min_value=145, max_value=188, value=170)
    weight = st.number_input("Weight (kg)", min_value=51, max_value=132, value=70)
    allergies = st.selectbox("Known Allergies", ["No", "Yes"])
    cancer_history = st.selectbox("History Of Cancer In Family", ["No", "Yes"])
    major_surgeries = st.number_input("Number Of Major Surgeries", min_value=0, max_value=3, value=0)

    # Convert "Yes"/"No" to 1/0
    data = {'Age': age,
            'Diabetes': 1 if diabetes == "Yes" else 0,
            'BloodPressureProblems': 1 if bp_problems == "Yes" else 0,
            'AnyTransplants': 1 if transplants == "Yes" else 0,
            'AnyChronicDiseases': 1 if chronic_diseases == "Yes" else 0,
            'Height': height,
            'Weight': weight,
            'KnownAllergies': 1 if allergies == "Yes" else 0,
            'HistoryOfCancerInFamily': 1 if cancer_history == "Yes" else 0,
            'NumberOfMajorSurgeries': major_surgeries}
    
    return pd.DataFrame(data, index=[0])

# Get user input
input_data = user_input()

# Add a Predict button
if st.button("Predict"):
    # Predict the premium price
    prediction = model.predict(input_data)
    # Display the prediction with increased font size
    st.markdown(
        f"<div style='text-align: center; color: green; font-size: 30px;'><strong>The predicted premium price is: {prediction[0]:.2f}</strong></div>",
        unsafe_allow_html=True
    )

            
