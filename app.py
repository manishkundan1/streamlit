import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.linear_model import LinearRegression

df=yf.download('SBIN.NS')
# Load the trained model
model = LinearRegression()
# Assuming df is your training data loaded from a CSV file or another source
# Features and target should be set accordingly based on your training data
features = df[['Open', 'Volume']]
target = df['Close']
model.fit(features, target)

# Streamlit App
st.title('Stock Price Prediction App')

# Input form for user to input features
open_price = st.number_input('Enter the Opening Price:', value=0.0)
volume = st.number_input('Enter the Trading Volume:', value=0.0)

# Make prediction using the trained model
prediction = model.predict([[open_price, volume]])

# Display the prediction
st.write('Predicted Closing Price:', prediction[0])
