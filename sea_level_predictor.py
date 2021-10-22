import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv(r'D:\python\freecodecamp\fifth_project\epa-sea-level.csv')


def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    sp1 = pd.Series([i for i in range(1880, 2051)])

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(sp1, intercept + slope*sp1, 'r', label='fitted line')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    sp2 = pd.Series([int(i) for i in range(2000, 2051)])
    slope, intercept, r, p, se = linregress(
        df_recent['Year'], df_recent["CSIRO Adjusted Sea Level"])
    df_recent.append(sp2, ignore_index=True)
    plt.plot(sp2, intercept + slope*sp2, color='g', label='fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
