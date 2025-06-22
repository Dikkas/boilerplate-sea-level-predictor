import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


#starting
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    #plt.scatter(x,y,args*)
    plt.scatter( df['Year'], df['CSIRO Adjusted Sea Level'] )

    # Create first line of best fit
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    x_all = pd.Series(range(1880,2051))
    y_all = intercept + slope * x_all
    plt.plot(x_all, y_all, label = 'First line of best fit')


    # Create second line of best fit
    df_recent = df[df['Year']>= 2000]
    slope_recent, intercept_recent, = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])[:2]
    x_recent = pd.Series(range(2000,2051))
    y_recent = intercept_recent + slope_recent * x_recent
    plt.plot(x_recent, y_recent, label = 'Second line of best fit')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()