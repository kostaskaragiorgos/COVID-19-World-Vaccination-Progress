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

def getvalueofcomparison(dataframe, comparison, value):
    locations = []
    index = ["total_vaccinations",	"people_vaccinated",	"people_fully_vaccinated",	"daily_vaccinations_raw"	,"daily_vaccinations",	"total_vaccinations_per_hundred",	"people_vaccinated_per_hundred",	"people_fully_vaccinated_per_hundred",	"daily_vaccinations_per_million"]
    for i in index:
        locations.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].comparison()][str(i)]))
    return locations


