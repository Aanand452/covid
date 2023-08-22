import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def covid():

    covid_df = pd.read_csv(
        "/Users/anandkumar/Downloads/data/Covid Data Analysis.csv")

    print(covid_df)

    # Before going to Analyze the data we should explore the dataframe

    print(covid_df.shape)

    print(covid_df.head())

    print(covid_df.columns)

    print(covid_df.dtypes)

    print(covid_df.index)

    print(covid_df.nunique())

    print(covid_df.value_counts())

    # it shows the null vales in each column
    print(covid_df.count())

    print(covid_df.isnull().sum())

    print(sns.heatmap(covid_df.isnull()))
    print(plt.show())

    # show the number of confirmed,deaths and recovred cases in each region

    print(covid_df.groupby('Region').sum())
    print(covid_df.groupby('Region')[
          'Confirmed'].sum().sort_values(ascending=True))
    print(covid_df.groupby('Region')['Confirmed', 'Recovered'].sum())

    # Remove all the records where confirmed cases less than 10
    print(covid_df[~(covid_df['Confirmed'] < 10)])

    # IN which region,maximum number of confirmed cases were recorded
    print(covid_df.groupby('Region').Confirmed.sum(
    ).sort_values(ascending=False).head(20))

    # In which Region minimum number of death cases were recorded
    print(covid_df.groupby('Region').Deaths.sum(
    ).sort_values(ascending=True).head(80))

    # How many Confirmed,Deaths & Recovered cases were reported from India till 29 April 2020?

    print(covid_df[covid_df.Region == 'India'])

    # Sort the entire data wrt no ofconfirmed cases in ascending order

    print(covid_df.sort_values(by=['Confirmed'], ascending=True))

    # Sort the entire data wrt no ofconfirmed cases in decending order

    print(covid_df.sort_values(by=['Confirmed'], ascending=False))


covid()
