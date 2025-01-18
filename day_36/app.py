#import streamlit numpy matplotlib seaborn plotly.express
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
# import RandomForestRegressor from sklearn.ensemble
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


#make containers
header = st.container()
datasets = st.container()
features = st.container()
mode_training = st.container()

#with header:
with header:
      st.title("kashtii ki app")
      st.text("This is a simple app to showcase the use of streamlit")
      
#with datasets:
with datasets:
      st.header("Datasets")   
      st.write("This is a simple app to showcase the use of streamlit")
      #importing dataset
      df = sns.load_dataset('titanic')
      df= df.dropna()
      st.write(df.head(10))
      #barchart of sex count
      st.bar_chart(df['sex'].value_counts(), use_container_width=True, color='#11abf9')
      st.bar_chart(df['pclass'].value_counts(), use_container_width=True, color='#ccabf9')
      st.line_chart(df['age'].value_counts(), use_container_width=True)
      # app features usin markdown
      
with features:
      st.header("Features")
      st.write("This is a simple app to showcase the use of streamlit")
      #app features usin markdown feature 1
      st.markdown("1. **Feature 1:** This will tell us about the feature 1")
      #app features usin markdown feature 2
      st.markdown("2. **Feature 2:** This will tell us about the feature 2")
with mode_training:
      st.header("Mode Training")
      st.write("This is a simple app to showcase the use of streamlit")
      # makng columns for input
      input, display = st.columns(2)
      input.slider("HOW MANY PEOPLE DO YOU KNOW? ", 10,100,20,5)
      
N_ESTIMATORS = input.selectbox("how many tree should be RF", 
            options=[100,200,300,400,500], index=0
      )
input.write(df.columns)
# input feature frm user

uinput = input.text_input("Enter the feature you want to plot")
# machine learning model
model = RandomForestRegressor(n_estimators=N_ESTIMATORS)
x= df[[uinput]]
y=df[['fare']]
model.fit(x,y)

pred = model.predict(x)

#display the result
display.subheader("Mean Squared Error")
display.write(mean_squared_error(y,pred))
display.subheader("R2 Score")
display.write(r2_score(y,pred))
display.subheader("Mean Absolute Error")
display.write(mean_absolute_error(y,pred))
