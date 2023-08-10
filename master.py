import streamlit as st
import pandas as pd

st.title("Data Analysis")

df= pd.DataFrame({
    'Name' : ["Aman", "Krish", "Radha","Ayushi"] ,
    'Marks' : [95,54,76,28]
})

st.header("Data")
st.write(df.head(4))

st.header("Description of data")
st.write(df.describe())

st.header("Visualisation")
st.line_chart(df['Marks'])
