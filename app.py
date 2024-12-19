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

