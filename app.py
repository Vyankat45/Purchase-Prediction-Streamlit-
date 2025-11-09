import streamlit as st
import pandas as pd
import pickle

# Load your trained model
model = pickle.load(open("model.pkl", "rb"))

# Set Streamlit page config
st.set_page_config(
    page_title="🛍️ Purchase Prediction App",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9fafc;
            padding: 2rem;
            border-radius: 10px;
        }
        h1 {
            color: #2e86de;
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
        }
        .stButton>button {
            background-color: #2e86de;
            color: white;
            border-radius: 8px;
            height: 3rem;
            width: 100%;
            font-size: 1rem;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #2161a8;
            color: #e3f2fd;
        }
        .result {
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
            padding: 10px;
            border-radius: 8px;
            background-color: #eaf2f8;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>🛍️ Purchase Prediction App</h1>", unsafe_allow_html=True)
st.markdown("### Predict whether a customer will purchase based on demographics")

# User input form
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("👤 Gender", ["Male", "Female"])
        age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1, value=25)

    with col2:
        salary = st.slider("💰 Salary Range", 10000, 200000, 50000, step=1000)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    # Create DataFrame for prediction
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Salary': [salary]
    })

    # Predict
    prediction = model.predict(input_data)[0]

    # Show result in a pop-like box
    if prediction == 1:
        st.markdown(
            f"<div class='result' style='background-color:#d4efdf; color:#1d8348;'>🎉 The person is <b>likely to Purchase!</b></div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='result' style='background-color:#f9e79f; color:#7d6608;'>🙁 The person is <b>not likely to Purchase.</b></div>",
            unsafe_allow_html=True,
        )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ by Vyankat Rathod</p>", unsafe_allow_html=True)
