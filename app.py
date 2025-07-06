# import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

# load the model and structure 
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Let's creat an user interface
st.title("water pollutants predictor")
st.title("predict the water pollutants based on year and station ID")

# user input
year_input = st.number_input("Enter year")
station_id = st.text("Enter Station ID")