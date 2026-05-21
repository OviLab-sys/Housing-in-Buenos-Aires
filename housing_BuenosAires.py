"""This file Contains all the code and explanation for the housing_BuenosAires project"""

#we start by importing the necessary libraries and inspecting our data
#since we want to automate the data cleaning cleaning process, we create a function for that

#the following are the required libraries

import warnings

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import VimeoVideo
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.utils.validation import check_is_fitted

warnings.simplefilter(action="ignore", category=FutureWarning)

#The following is the data wrangling automation function

def wrangle(filepath):
    df = pd.read_csv(filepath)
    return df

df = wrangle("data/buenos-aires-real-estate-1.csv")

df.head()

##next we are going to inspect the data and findout the abnormalities it 
##contains and hence add the required lines of codes to our wrangle function

#the next exercise requires 