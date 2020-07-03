import pandas as pd
import csv
import numpy as np
import nltk
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import seaborn as sb

# GossipCop and PolitiFact

gossipcop_fake = pd.read_csv('datasets/gossipcop_fake.csv')
gossipcop_real = pd.read_csv('datasets/gossipcop_real.csv')

# data observation


def data_obs(dataset):
    print("###########################")
    print(dataset.shape)
    print(dataset.head(10))


data_obs(gossipcop_fake)
data_obs(gossipcop_real)

# Eliminate columns
df_gossipcop_fake = gossipcop_fake[['title']]
df_gossipcop_real = gossipcop_real[['title']]

# add label column
df_gossipcop_fake['label'] = "FAKE"
df_gossipcop_real['label'] = "REAL"

# Merge dataframes
gossipcop_data = pd.concat([df_gossipcop_fake, df_gossipcop_real])
