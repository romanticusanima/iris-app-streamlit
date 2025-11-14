import streamlit as st
import pandas as pd
import numpy as np
import joblib

def predict(sepal_l, sepal_w, petal_l, petal_w):
    model = joblib.load('model/rf_model.joblib')
    data = np.expand_dims(np.array([sepal_l, sepal_w, petal_l, petal_w]), axis=0)
    predictions = model.predict(data)
    return predictions[0]

st.title('Classification of Iris flowers')
st.markdown('This is a simple model for classifying Iris flowers into three types: \
setosa, versicolor, virginica')
st.image('images/iris.png')

# Table
st.header("Average characteristic values ​​for each Iris type")
iris_df = pd.read_csv("data/iris.csv")
mean_values = iris_df.groupby('Species').mean().reset_index()
st.dataframe(mean_values)

# Title
st.header("Flower characteristics")
col1, col2 = st.columns(2)

# Вnter sepal data
with col1:
    st.text("Sepal characteristics")
    sepal_l = st.slider('Sepal length (sm)', 1.0, 8.0, 0.5)
    sepal_w = st.slider('Sepal width (sm)', 2.0, 4.4, 0.5)

# Enter petal data
with col2:
    st.text("Petal characteristics")
    petal_l = st.slider('Petal length (sm)', 1.0, 7.0, 0.5)
    petal_w = st.slider('Petal width (sm)', 0.1, 2.5, 0.5)

# Predict
if st.button("Predict type of Iris"):
    result = predict(sepal_l, sepal_w, petal_l, petal_w)
    st.write(f"Predicted iris type: {result}")