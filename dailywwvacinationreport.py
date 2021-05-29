import pandas as pd
FILENAME = "vaccinations.csv"
def createdataframe(filename):
    """
    creates a dataframe.
    Args:
        filename: a csv file
    Returns:
        a dataframe
    """
    return pd.read_csv(filename)

def cleardataframe(dataframe):
    """ removes the duplicate values
    Args:
        dataframe: a dataframe
    Returns:
        a modified dataframe
    """
    dataframe = dataframe.drop_duplicates(subset='location', keep='last')
    return dataframe

def removecontinents(dataframe):
    """ removes rows from dataframe
    Args:
        dataframe: a dataframe
    Returns:
        a modified dataframe
    """
    indexlist = ["Asia", "Europe", "Africa", "Middle East", "World", "Upper middle income", "High income","North America", "Lower middle income"]
    for i in indexlist:
        dataframe.drop(dataframe[dataframe['location']== str(i)].index, inplace=True)
    return dataframe

def getvalueofcomparison(dataframe, comparison, value=None):
    """ removes rows from dataframe
    Args:
        dataframe: a dataframe
        comparison = min or max
        value index name
    Returns:
        info: a listofinfo
    """
    info = []
    index = ["total_vaccinations",	"people_vaccinated",	"people_fully_vaccinated",	"daily_vaccinations_raw"	,"daily_vaccinations",	"total_vaccinations_per_hundred",	"people_vaccinated_per_hundred",	"people_fully_vaccinated_per_hundred",	"daily_vaccinations_per_million"]
    if value == None:
        for i in index:
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].comparison()][str(i)]))
    else:
        for i in index:
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].comparison()][str(value)]))
    return info

def main():
    df = createdataframe(FILENAME)
    df = cleardataframe(df)
    print(df.head())


if __name__=='__main__':
    main()
