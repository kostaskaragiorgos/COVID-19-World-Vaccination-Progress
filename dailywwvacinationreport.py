import pandas as pd
def createdataframe(filename):
    return pd.read_csv(filename)

def cleardataframe(dataframe):
    return dataframe.drop_duplicates(subset='location', keep='last', inplace=True)