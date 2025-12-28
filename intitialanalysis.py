import pandas as pd
import streamlit as st
import plotly.express as px
import os
dir_path='/home/michael/DATA/'
filenames = os.listdir(dir_path)
selected_filename = st.selectbox('Select a file', filenames, key = 'fileselect')
filename = os.path.join(dir_path, selected_filename)

def dataloading(filename):
    df_exists = st.session_state.get('chosendata')
    fnmatch = st.session_state.get("filename") == filename  
    if df_exists is not None and not df_exists.empty and fnmatch:
        df = st.session_state.chosendata
    elif filename.endswith(".xlsx"): 
        excelfile = pd.ExcelFile(filename)
        sheetname = st.selectbox('Select a sheet', excelfile.sheet_names, key = 'pageselect')
        st.session_state.chosendata = excelfile.parse(sheet_name=sheetname) 
        df=st.session_state.chosendata 
    elif filename.endswith(".csv"): 
        st.session_state.chosendata = pd.read_csv(filename)
        df=st.session_state.chosendata
    elif os.path.isdir(filename):
        errormessage = "Chosen path is a directory!"
        df = pd.DataFrame()
        st.write(errormessage)
        print(errormessage)
    else:
        raise ValueError('Invalid input please try something else!')
    return df 
df = dataloading(filename)
st.title(":blue[Initial Analysis]")
st.write(df.columns) ####type:ignore
st.dataframe(df.head()) #####type:ignore

