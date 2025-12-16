import pandas as pd



def getdata(x):
    return  pd.read_csv(f'{x}')
