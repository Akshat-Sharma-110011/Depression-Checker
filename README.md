# Depression-Checker

# Mental Health Assessment Tool

## Overview

The **Mental Health Assessment Tool** is a web-based application built using **Streamlit** that helps users assess their risk for depression based on lifestyle and mental health factors. The tool uses a machine learning model to predict whether someone may be at risk for depression, providing personalized feedback, self-care tips, and professional resources. It is designed for informational purposes only and is not a substitute for professional medical advice.

## Features

- **User-Friendly Interface**: The app guides users through a form to collect personal, lifestyle, and health-related data.
- **Risk Prediction**: The model predicts whether the user is at risk for depression based on the collected data.
- **Feedback Mechanism**: After making a prediction, users can provide feedback on the tool's usefulness.
- **Resource Links**: Provides links to mental health resources and helplines.
- **Self-Care Tips**: Offers practical tips for improving mental well-being.

## How to Run the App Locally

### Prerequisites

- Python 3.7 or higher
- Required libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mental-health-assessment-tool.git
   cd mental-health-assessment-tool
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open your browser and go to http://localhost:8501 to use the app.

Files
app.py: The main Python script containing the logic for the app.
requirements.txt: A file listing the Python dependencies needed to run the app.
df.pkl: The pickled dataset used for the model's predictions.
pipe.pkl: The pickled machine learning pipeline used for making predictions.
App Description
1. Step 1: Personal Information
Gender
Age
City
Profession
2. Step 2: Lifestyle Information
Academic Pressure
Work Pressure
CGPA
Study Satisfaction
Work Satisfaction
Work Hours
3. Step 3: Health and History Information
Sleep Duration
Dietary Habits
Degree
Suicidal Thoughts
Financial Stress
Depression History
4. Step 4: Feedback
Rate the helpfulness of the tool (Very helpful, Somewhat helpful, Not helpful)
Provide additional comments or suggestions for improving the tool.
Model Details
The model used for predictions is a machine learning model trained on a dataset of lifestyle and mental health factors. The prediction is made based on the user’s input and is processed through a pre-trained pipeline, providing a risk score for depression.

Disclaimer
This tool is for informational purposes only and is not intended as a medical diagnosis. Please consult a healthcare provider for professional advice. If you are in crisis or need immediate help, please contact a mental health professional or call a helpline.

Mental Health Helpline: 📞 91-22-2772 6771
National Suicide Prevention Lifeline (India): 📞 91-20-26473955
Samaritans India: samaritansindia.org
Contributing
We welcome contributions! If you have suggestions for improvements or bug fixes, feel free to create an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using the Mental Health Assessment Tool! 🌱

markdown
Copy code

### Key Sections:
1. **Overview**: Brief description of the project.
2. **Features**: Key features of the tool.
3. **How to Run the App Locally**: Installation and setup instructions.
4. **Files**: Describes the main files in the repo.
5. **App Description**: Overview of the user steps.
6. **Model Details**: Explains the machine learning model used.
7. **Disclaimer**: Reminds users that the tool is not a substitute for medical advice.
8. **Contributing**: Information on how others can contribute.
9. **License**: A placeholder for your project license (you can choose the appropriate one, like MIT or GPL).

