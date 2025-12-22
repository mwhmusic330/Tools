import pandas as pd
import streamlit as st
import plotly.express as px
from getdata import getdata
from fileselector import file_selectbox
import os

filename = file_selectbox() 

st.title(":blue[Initial Analysis]")
df = getdata(filename)
###    df.info()
###    st.dataframe(df.head())

