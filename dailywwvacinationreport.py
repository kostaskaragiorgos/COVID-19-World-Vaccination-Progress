import logging
import os
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

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
    indexlist = ["Asia", "Europe", "Africa", "Middle East", "World", "Upper middle income", "High income", "North America", "Lower middle income"]
    for i in indexlist:
        dataframe = dataframe.drop(dataframe[dataframe['location'] == str(i)].index)
    return dataframe


def getvaccinationsplotforeverylocation(dataframe):
    """
    Saves a Vaccinations plot for every location.
    Args:
        dataframe: a pandas dataframe
    """
    indexlist = dataframe.location.unique().tolist()
    for i in indexlist:
        dataframe[dataframe['location'] == str(i)].plot(figsize=(15, 10), x='date', y=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'], title="Vaccinations of "+str(i), ylabel="Number of Vaccinated People")
        plt.savefig("plots/Vaccinations of "+str(i)+".png")

def getvalueofrows(dataframe):
    """
    continents.
    Args:
        dataframe: the dataframe
    Return:
        info: a list of rows
    """
    info = []
    indexlist = ["Asia", "Europe", "Africa", "Middle East", "World", "Upper middle income", "High income", "North America", "Lower middle income"]
    for i in indexlist:
        info.append(str(dataframe.loc[dataframe['location'] == str(i)].to_string(index=False)))
    return info

def novaluecomparison(info, index, dataframe, comparison):
    """
    Args:
        info: a list
        index: a list of index names
        dataframe: a dataframe
        comparison
    Return:
        info: a list
    """
    for i in index:
        if comparison == "min":
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()]["location"].to_string(index=False)) + str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()][str(i)].to_string(index=False)))
        else:
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()]["location"].to_string(index=False)) + str(dataframe[dataframe[str(i)] == dataframe[str(i)].max()][str(i)].to_string(index=False)))
    return info


def valuecomparison(info, index, dataframe, comparison, value):
    """ min/max comparison based on value
    Args:
        info: list to fill
        index: index list
        dataframe: the dataframe
        comparison: min/max
        value: column name to compare
    Returns:
        info: list full of comparissons
    """
    for i in index:
        if comparison == "max":
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()]["location"].to_string(index=False)) + str(dataframe[dataframe[str(i)] == dataframe[str(i)].max()][str(value)].to_string(index=False)))
        else:
            info.append(str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()]["location"].to_string(index=False)) + str(dataframe[dataframe[str(i)] == dataframe[str(i)].min()][str(value)].to_string(index=False)))
    return info

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
    index = ["total_vaccinations",	"people_vaccinated",	"people_fully_vaccinated",	"daily_vaccinations_raw", "daily_vaccinations",	"total_vaccinations_per_hundred", "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred", "daily_vaccinations_per_million"]
    if value is None:
        info = novaluecomparison(info, index, dataframe, comparison)
    else:
        info = valuecomparison(info, index, dataframe, comparison, value)
    return info

def addtoafile(data, flag):
    """
    write data to a .txt file
    Args:
        data: data to the file save 
    """
    with open('dailyreport.txt', flag) as f:
        f.writelines(data)


def main():
    """ main function """
    df = createdataframe(FILENAME)
    getvaccinationsplotforeverylocation(df)
    df = cleardataframe(df)
    logging.info("vaccinations plots has been successfully created")
    info = getvalueofrows(df)
    
    addtoafile(info, "w")
    df = removecontinents(df)
    infosmin = getvalueofcomparison(df, min, value=None)
    addtoafile(infosmin, "a+")
    infosmax = getvalueofcomparison(df, max, value=None)
    addtoafile(infosmax, "a+")
    print(infosmax)
    logging.info("dailyreport.txt has been successfully created")
    os.system("pause")




if __name__ == '__main__':
    main()
