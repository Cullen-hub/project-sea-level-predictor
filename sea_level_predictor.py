import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err  = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    min_year = df['Year'].min()
    max_year = 2050
    x_values = list(range(min_year, max_year + 1))
    line_of_bf = [slope * x + intercept for x in x_values]
    plt.plot(x_values, line_of_bf, 'r')


    # Create the second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err  = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    min_year = df_2000['Year'].min()
    max_year = 2050
    x_values = list(range(min_year, max_year + 1))
    line_of_bf = [slope * x + intercept for x in x_values]
    plt.plot(x_values, line_of_bf, 'r')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
