import pandas as pd
import streamlit as st

def sheets(x):
    excelfile = pd.ExcelFile(x)
    sheetnames = excelfile.sheet_names
    ##### print(sheetnames)
    sheetselect = st.selectbox('Select a sheet', sheetnames)
    

def getdata(x):
    if x.endswith(".csv"):
        return pd.read_csv(x)

    elif x.endswith(".xlsx"):
        return sheets(x)
