import pickle
import streamlit as st
import sys
from pathlib import Path
import base64

#!pip freeze > requirements.txt this automatical help to generate the requirements.txt file where all the libraries used in the project are stored.note that the file is generated in the same directory where the project is located.

# Add parent directory to sys.path
dir = Path(__file__).resolve().parent.parent
sys.path.append(str(dir))

model = pickle.load(open('G:/Cardio_app/LGBM_model.pkl', 'rb'))

def main():
    st.set_page_config(page_title="Collins Cardiovascular Disease Prediction App", layout="wide")

    # Display thumbnail image AND base64 help to convert image to string so you import base64 above 

    def display_thumbnail(image_file):
        with open(image_file, "rb") as image:
            encoded_image = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{encoded_image}" alt="Thumbnail" style="width: 400px; height: auto;"/>
            </div>
            """,
            unsafe_allow_html=True
        )

    display_thumbnail('G:/Cardio_app/bg_1.jpg')

    # CSS style for the app
    st.markdown(
        """
        <style>
        .main {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
            color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.title("Collins Cardiovascular Disease Prediction App")
     
     # Create a form container with the unique key 'CVD'to hold the form widgets below
    form = st.form('CVD')

    # Add input widgets to the form
    Age = form.number_input('Age', min_value=1, max_value=100, value=35)
    Height = form.number_input('Height', min_value=40.0, max_value=250.0, value=164.0)
    Weight = form.number_input('Weight', min_value=10.0, max_value=200.0, value=74.0)
    Systolic = form.slider('Systolic', min_value=30, max_value=200, value=120)
    Diastolic = form.slider('Diastolic', min_value=50, max_value=180, value=80)
    Gender = form.selectbox('Gender', ['Male', 'Female'])
    Cholesterol_normal = form.selectbox('Cholesterol Normal', ['Yes', 'No'])
    Cholesterol_very_high = form.selectbox('Cholesterol Very High', ['Yes', 'No'])
    Glucose_normal = form.selectbox('Glucose Normal', ['Yes', 'No'])
    Glucose_very_high = form.selectbox('Glucose Very High', ['Yes', 'No'])
    Smoke = form.selectbox('Smoke', ['Yes', 'No'])
    Alcohol = form.selectbox('Alcohol', ['Yes', 'No'])
    Physical_Activity = form.selectbox('Physical Activity', ['Yes', 'No'])

    # Add a submit button to the form
    if form.form_submit_button('Predict'):
         # Code to execute when the form is submitted
         # Convert non-numeric features to numeric data types
        Gender = 1 if Gender == 'Male' else 0
        Cholesterol_normal = 1 if Cholesterol_normal == 'Yes' else 0
        Cholesterol_very_high = 1 if Cholesterol_very_high == 'Yes' else 0
        Glucose_normal = 1 if Glucose_normal == 'Yes' else 0
        Glucose_very_high = 1 if Glucose_very_high == 'Yes' else 0
        Smoke = 1 if Smoke == 'Yes' else 0
        Alcohol = 1 if Alcohol == 'Yes' else 0
        Physical_Activity = 1 if Physical_Activity == 'Yes' else 0
        # Make predictions using the model
        makepredictions = model.predict([[Age, Height, Weight, Systolic, Diastolic, Gender, Cholesterol_normal, Cholesterol_very_high,
                                          Glucose_normal, Glucose_very_high, Smoke, Alcohol, Physical_Activity]])

        output = round(int(makepredictions[0]))

        st.success("Your predicted Cardiovascular disease status is {}".format(output))

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()