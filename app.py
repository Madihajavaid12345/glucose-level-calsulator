import streamlit as st

# Function to calculate estimated HbA1c from average glucose
def calculate_hba1c(average_glucose):
    return (average_glucose + 46.7) / 28.7

# Function to provide health advice based on blood glucose levels
def glucose_health_advice(glucose_level):
    if glucose_level < 70:
        return "Your glucose level is too low. Consider having a snack."
    elif 70 <= glucose_level <= 140:
        return "Your glucose level is normal. Keep up the good work!"
    elif 140 < glucose_level <= 200:
        return "Your glucose level is slightly high. Watch your diet."
    else:
        return "Your glucose level is high. Please consult a doctor."

# Streamlit app structure
st.title("Blood Glucose Level Assessment & HbA1c Estimation")

# User input for glucose level
glucose_level = st.number_input("Enter your blood glucose level (mg/dL)", min_value=0)

if glucose_level:
    # Show the health advice
    advice = glucose_health_advice(glucose_level)
    st.write(advice)

    # Calculate the estimated HbA1c
    estimated_hba1c = calculate_hba1c(glucose_level)
    st.write(f"Your estimated HbA1c is: {estimated_hba1c:.2f}%")

st.write("The HbA1c value estimates your average blood sugar levels over the past 2-3 months. Please consult with a healthcare provider for more personalized advice.")
