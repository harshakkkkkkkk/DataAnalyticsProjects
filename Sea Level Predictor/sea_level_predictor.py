import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    fig, ax = plt.subplots(figsize=(12, 12))
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    x_forecast = pd.Series(range(1880, 2051))
    y_forecast = res.slope * x_forecast + res.intercept
    plt.plot(x_forecast, y_forecast, 'r-', label='1880-2050 Best Fit')

    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent["Year"]
    y_recent = df_recent["CSIRO Adjusted Sea Level"]
    res_recent = linregress(x_recent, y_recent)
    x_recent_forecast = pd.Series(range(2000, 2051))
    y_recent_forecast = res_recent.slope * x_recent_forecast + res_recent.intercept
    plt.plot(x_recent_forecast, y_recent_forecast, 'orange', label='2000-2050 Best Fit')

    # Setting x ticks and labels
    x_ticks = range(1850, 2100, 25)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([f"{tick:.0f}" for tick in x_ticks])

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()