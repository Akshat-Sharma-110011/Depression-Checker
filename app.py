import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# Load the dataset and pipeline
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Streamlit app title with HTML for centering
st.markdown("""
    <h1 style="text-align: center;">Mental Health Assessment Tool</h1>
    """, unsafe_allow_html=True)

# Introduction with a friendly tone
st.write("""
    Welcome to the **Mental Health Assessment Tool**. This tool helps you assess whether you may be at risk of depression based on your lifestyle and mental health factors. 
    Please fill out the form below, and we'll provide you with a prediction. **Note**: This is not a substitute for professional medical advice.
    """)
st.markdown('---')

# Add space
st.markdown("<br><br>", unsafe_allow_html=True)

# Step 1: Personal Information
st.header("Step 1: Personal Information")

Gender = st.selectbox('Gender', list(df['Gender'].unique()), help="Select your gender")
Age = st.slider('Age', 0, 99, help="Your age in years")
City = st.selectbox('City', list(df['City'].unique()), help="Select your city")
Profession = st.selectbox('Profession', list(df['Profession'].unique()), help="Your current profession")

# Add space between questions
st.markdown("<br><br>", unsafe_allow_html=True)

# Step 2: Lifestyle Information
st.header("Step 2: Lifestyle Information")

# Use different sections for clarity
Academic = st.slider('Academic Pressure (0-5)', 0, 5, help="Rate your academic pressure")
Work = st.slider('Work Pressure (0-5)', 0, 5, help="Rate your work pressure")
CGPA = st.slider('CGPA (0.0-10.0)', 0.0, 10.0, step=0.1, help="Your current CGPA")
Study = st.slider('Study Satisfaction (0-5)', 0, 5, help="Rate your satisfaction with your studies")
Work_sat = st.slider('Work Satisfaction (0-5)', 0, 5, help="Rate your satisfaction with your work")
Hours = st.slider('Work Hours (0-16)', 0, 16, help="How many hours do you work each day?")

# Add space after questions
st.markdown("<br><br>", unsafe_allow_html=True)

# Step 3: Health and History Information
st.header("Step 3: Health and History Information")

Sleep = st.selectbox('Sleep Duration', list(df['Sleep Duration'].unique()), help="How many hours do you sleep?")
Diet = st.selectbox('Dietary Habits', list(df['Dietary Habits'].unique()), help="Your dietary habits")
Degree = st.selectbox('Degree', list(df['Degree'].unique()), help="Highest level of education")
Thoughts = st.selectbox('Suicidal Thoughts', list(df['Suicidal Thoughts'].unique()), help="Ever had suicidal thoughts?")
Stress = st.slider('Financial Stress (0-5)', 0, 5, help="Rate your financial stress level")
History = st.selectbox('Is there a history of mental illness in your family?', list(df['Depression History'].unique()))

# Add space before prediction button
st.markdown("<br><br>", unsafe_allow_html=True)

# Add a Clear Button for Reset
if st.button('Clear All'):
    st.experimental_rerun()

# Prediction Button
if st.button('Check for Health'):
    with st.spinner('Calculating your result...'):
        time.sleep(2)  # Simulate processing time

        try:
            # Ensure consistent data types and create the input DataFrame
            query = pd.DataFrame({
                'Gender': [str(Gender)],
                'Age': [int(Age)],
                'City': [str(City)],
                'Profession': [str(Profession)],
                'Academic Pressure': [int(Academic)],
                'Work Pressure': [int(Work)],
                'CGPA': [float(CGPA)],
                'Study Satisfaction': [int(Study)],
                'Work Satisfaction': [int(Work_sat)],
                'Sleep Duration': [str(Sleep)],
                'Dietary Habits': [str(Diet)],
                'Degree': [str(Degree)],
                'Suicidal Thoughts': [str(Thoughts)],
                'Work Hours': [int(Hours)],
                'Financial stress': [int(Stress)],
                'Depression History': [str(History)],
                'Job Satisfaction': [3],  # Example placeholder value for missing column
                'Financial Stress': [3]  # Example placeholder value for missing column
            })

            # Make the prediction
            prediction = pipe.predict(query)[0]

            # Provide personalized feedback
            if prediction == 1:
                st.warning("It looks like you may be at risk of depression. Please consider seeking professional help.")
                st.markdown("""
                    **Additional Resources**:
                    - **Mental Health Helpline**: 📞 **91-22-2772 6771**
                    - **Visit**: [Mental Health India](http://www.mentalhealth.in)
                    - **National Suicide Prevention Lifeline (India)**: 📞 91-20-26473955
                    - **Samaritans India**: [samaritansindia.org](http://www.samaritansindia.org)
                """)
                st.markdown("""
                    **Self-Care Tips**:
                    - Try **deep breathing exercises** or **meditation** for relaxation.
                    - **Talk to someone you trust** – sharing your feelings can help.
                    - **Get active** – Physical activity can improve your mood.
                    - **Seek professional help** if you need support.
                """)
            else:
                st.success("You're doing great! Keep up the positivity! 😊")

            # Show the prediction
            st.title(f"Prediction: {'Depression Detected 😟' if prediction == 1 else 'No Depression 😊'}")

            # Feedback Form
            st.header("Step 4: User Feedback")

            feedback = st.radio(
                "How helpful did you find this tool?",
                ['Very helpful', 'Somewhat helpful', 'Not helpful'],
                help="Select your feedback on the tool"
            )

            comments = st.text_area("Additional comments or suggestions", help="We appreciate your feedback")

            if st.button("Submit Feedback"):
                st.write(f"Thank you for your feedback! You rated it as: {feedback}")
                if comments:
                    st.write(f"Your comments: {comments}")
                else:
                    st.write("No additional comments provided.")

        except ValueError as e:
            st.error(f"An error occurred during prediction: {e}")

# Disclaimer at the end
st.markdown("""
    ---
    **Disclaimer**: This tool is for informational purposes only and is not intended as a medical diagnosis. 
    Please consult a healthcare provider for professional advice.
    """)
