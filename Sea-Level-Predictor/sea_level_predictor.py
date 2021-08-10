import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(13,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

   
    # Create first line of best fit
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = reg.slope
    b = reg.intercept

    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = (m*x_pred)+b
    ax.plot(x_pred, y_pred, color="red")

    # Create second line of best fit
    df_2 = df.loc[df['Year']>=2000]
    reg2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    m2 = reg2.slope
    b2 = reg2.intercept

    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = (m2*x_pred2)+b2
    ax.plot(x_pred2, y_pred2, color="orange")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()