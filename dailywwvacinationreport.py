import pandas as pd
def createdataframe(filename):
    return pd.read_csv(filename)

def cleardataframe(dataframe):
    return dataframe.drop_duplicates(subset='location', keep='last', inplace=True)

def removecontinents(dataframe):
    indexlist = ["Asia", "Europe", "Africa", "Middle East", "World", "Upper middle income", "High income","North America", "Lower middle income"]
    for i in indexlist:
        dataframe.drop(dataframe[dataframe['location']== str(i)].index, inplace=True)
    return dataframe