import pandas as pd
import streamlit as st
import os



def file_selectbox(dir_path='/home/michael/DATA/'):
    filenames = os.listdir(dir_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(dir_path, selected_filename)
