#import streamlit numpy matplotlib seaborn plotly.express
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


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
      
with features:
      st.header("Features")
      st.write("This is a simple app to showcase the use of streamlit")
      
with mode_training:
      st.header("Mode Training")
      st.write("This is a simple app to showcase the use of streamlit")
      
