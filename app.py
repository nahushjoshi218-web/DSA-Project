import streamlit as st
import numpy as np
import joblib

# load files
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
encoders = joblib.load('encoders.pkl')

st.title('Iris Flower Prediction')

# inputs
sl = st.number_input('Sepal Length')
sw = st.number_input('Sepal Width')
pl = st.number_input('Petal Length')
pw = st.number_input('Petal Width')

# prepare input
input_data = np.array([[sl, sw, pl, pw]])

# scale
input_data_scaled = scaler.transform(input_data)

# predict
if st.button('Predict'):
    pred = model.predict(input_data_scaled)
    
    # decode result
    label = encoders['species'].inverse_transform(pred)[0]
    
    st.success(f'Flower Type: {label}')