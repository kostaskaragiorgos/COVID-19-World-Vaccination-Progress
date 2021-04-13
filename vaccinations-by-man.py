import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE = 'vaccinations-by-manufacturer.csv'


def create_df(filename):
    return pd.read_csv(filename)

def findvaccine(location):
    