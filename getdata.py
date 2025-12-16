import pandas as pd



def getdata(x):
    if x.endswith(".csv"):
        return pd.read_csv(f'{x}')

    elif x.endswith(".xlsx"):
        return pd.read_excel(f'{x}')

