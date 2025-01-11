
# 🧠 Mental Health Assessment Tool

## 🌟 Overview

The **Mental Health Assessment Tool** is a web-based application built using **Streamlit** to help users assess their risk for depression. By analyzing lifestyle and mental health factors, it provides:  
- Personalized feedback  
- Self-care tips  
- Professional resources  

**Note:** This tool is designed for informational purposes only and is not a substitute for professional medical advice.

---

## ✨ Features

- **🖥️ User-Friendly Interface**: An intuitive form for entering personal, lifestyle, and health data.  
- **📊 Risk Prediction**: A machine learning model predicts depression risk based on user input.  
- **💬 Feedback Mechanism**: Users can provide feedback on the tool's usefulness.  
- **📚 Resource Links**: Offers helpline numbers and links to mental health resources.  
- **🌿 Self-Care Tips**: Practical advice for improving mental well-being.  

---

## 🚀 How to Run the App Locally

### 📋 Prerequisites

- Python 3.7 or higher  
- Required libraries (listed in `requirements.txt`)  

### 🛠️ Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/mental-health-assessment-tool.git
   cd mental-health-assessment-tool
   ```

2. **(Optional) Create a virtual environment**:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:  
   ```bash
   streamlit run app.py
   ```

5. **Access the app**: Open your browser and navigate to `http://localhost:8501`.  

---

## 📂 Files

- **`app.py`**: Main Python script containing the app's logic.  
- **`requirements.txt`**: Lists all Python dependencies.  
- **`df.pkl`**: Pickled dataset for model predictions.  
- **`pipe.pkl`**: Pickled machine learning pipeline for making predictions.  

---

## 📝 App Description

### 1️⃣ **Step 1: Personal Information**  
- Gender  
- Age  
- City  
- Profession  

### 2️⃣ **Step 2: Lifestyle Information**  
- Academic Pressure  
- Work Pressure  
- CGPA  
- Study Satisfaction  
- Work Satisfaction  
- Work Hours  

### 3️⃣ **Step 3: Health and History Information**  
- Sleep Duration  
- Dietary Habits  
- Degree  
- Suicidal Thoughts  
- Financial Stress  
- Depression History  

### 4️⃣ **Step 4: Feedback**  
- Rate the tool's helpfulness (e.g., Very helpful, Somewhat helpful, Not helpful)  
- Provide comments or suggestions for improvement.  

---

## 🤖 Model Details

The tool leverages a machine learning model trained on a dataset of mental health and lifestyle factors.  
- Input data is processed through a pre-trained pipeline (`pipe.pkl`).  
- The model outputs a risk score for depression, helping users gauge their mental health status.  

---

## ⚠️ Disclaimer

This tool is for **informational purposes only** and does not provide medical diagnoses.  
If you are in crisis or need immediate help, please contact a healthcare professional or helpline.  

### 📞 Helplines:  
- **Mental Health Helpline (India):** 91-22-2772 6771  
- **National Suicide Prevention Lifeline (India):** 91-20-26473955  
- **Samaritans India:** [Visit Website](https://www.samaritansindia.org)  

---

## 🤝 Contributing

We welcome contributions!  
- Found a bug? Create an issue.  
- Have an idea? Submit a pull request.  

Let’s work together to improve mental health accessibility.  

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

Thank you for using the **Mental Health Assessment Tool**! 🌱  
Together, we can create a healthier world. 🌍
