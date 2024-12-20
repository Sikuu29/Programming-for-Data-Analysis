import streamlit as st
from nbconvert import HTMLExporter
import nbformat
import pickle
import pandas as pd

# Sidebar for navigation
st.sidebar.markdown(
    "<h1 style='color: darkblue;'>Navigation</h1>",
    unsafe_allow_html=True
)
page = st.sidebar.radio("Go to", ["Data Overview", "EDA", "Model"])

# EDA Page
if page == "EDA":
    st.markdown(
        "<h1 style='color: darkgreen;'>Exploratory Data Analysis</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='color: gray;'>Analyze the trends in air quality parameters.</p>",
        unsafe_allow_html=True
    )

    st.markdown("### PM2.5")
    st.image('pm2.5.png')
    st.markdown("### PM10")
    st.image('PM10.png')
    st.markdown("### DEWP")
    st.image('dewp.png')
    st.markdown("### Station")
    st.image('station.png')
    st.markdown("### TEMP")
    st.image('temp.png')
    st.markdown("### CO")
    st.image('co.png')
    st.markdown("### NO2")
    st.image('no2.png')
    st.markdown("### O3")
    st.image('o3.png')
    st.markdown("### SO2")
    st.image('so2.png')
# Model Page
elif page == "Model":
    st.markdown(
        "<h1 style='color: purple;'>Model Prediction Page</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='color: darkred;'>Select features and predict air quality parameters.</p>",
        unsafe_allow_html=True
    )

    def predict(model, input_data):
        prediction = model.predict(input_data)
        return prediction[0]

    # User Inputs for AQI Prediction
    st.markdown("<h3 style='color: teal;'>Input Features</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        month = st.selectbox("Month", list(range(1, 13)))
        day = st.slider("Day", 1, 31)
        hour = st.slider("Hour", 0, 24)
    with col2:
        O3 = st.number_input("O3", min_value=0.2, max_value=1071.0, step=0.1)
        DEWP = st.number_input("Dew Point (DEWP)", min_value=-43.4, max_value=29.1)
        RAIN = st.number_input("Rain", min_value=0.0, max_value=72.5, step=0.1)
        wd = st.selectbox("Wind Direction (wd)", list(range(1, 16)))
        WSPM = st.number_input("Wind Speed (WSPM)", min_value=0.0, max_value=13.2, step=0.1)

    input_data = pd.DataFrame({
        'month': [month],
        'day': [day],
        'hour': [hour],
        'O3': [O3],
        'DEWP': [DEWP],
        'RAIN': [RAIN],
        'wd': [wd],
        'WSPM': [WSPM],
    })

    model_choice = st.selectbox(
        "Select Model for Prediction",
        ("Random Forest Regressor", "KNN Regressor", "Linear Regressor", "Decision Tree Regressor")
    )

    predi = 0.90
    if model_choice == "Random Forest Regressor":
        forest = pickle.load(open('forest.pkl', 'rb'))
        predi = predict(forest, input_data)
    elif model_choice == "KNN Regressor":
        knn = pickle.load(open('knn.pkl', 'rb'))
        predi = predict(knn, input_data)
    elif model_choice == "Linear Regressor":
        lr = pickle.load(open('lr.pkl', 'rb'))
        predi = predict(lr, input_data)
    elif model_choice == "Decision Tree Regressor":
        dtc = pickle.load(open('tree.pkl', 'rb'))
        predi = predict(dtc, input_data)

    st.markdown(
        f"<h3 style='color: darkblue;'>Predicted Temperature: <span style='color: orange;'>{round(predi, 2)}</span></h3>",
        unsafe_allow_html=True
    )

# Data Overview Page
if page == "Data Overview":
    st.markdown(
        "<h1 style='color: maroon;'>Data Overview</h1>",
        unsafe_allow_html=True
    )
    st.write("### Information about the dataset")
    st.write("View the notebook below:")

    def notebook_to_html(notebook_path):
        with open(notebook_path, "r", encoding="utf-8") as file:
            notebook_content = nbformat.read(file, as_version=4)
        html_exporter = HTMLExporter()
        body, _ = html_exporter.from_notebook_node(notebook_content)
        return body

    try:
        notebook_html = notebook_to_html(r"C:\Program Files\JetBrains\PyCharm 2024.3.1\sikas_project\Sikas_project_final.ipynb")
        st.components.v1.html(notebook_html, height=800, width=1000, scrolling=True)
    except Exception as e:
        st.error(f"Error displaying the notebook: {e}")

