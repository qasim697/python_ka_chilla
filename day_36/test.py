import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
st.header('Streamlit Example')
df= sns.load_dataset('iris')
st.write(df)
#plot data
st.write('## Plot Data')
st.line_chart(df['sepal_length'])
st.write('## Plot Data')
st.area_chart(df['sepal_length'])
st.write('## Plot Data')
st.bar_chart(df["sepal_length"])

st.write('## Plot Data')
st.write(df)
st.write('## Plot Data')
st.table(df)
st.write('## Plot Data')
st.write(df)
st.write('## Plot Data')
st.write(df)
