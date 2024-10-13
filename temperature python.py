# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Step 1: Function to generate the dummy dataset
def generate_dummy_temperature_data():
    """
    This function generates a dummy dataset with daily temperatures
    for the last 12 monthswith a range between -5°C and 25°C to be in 
    accordance with the real values.
    """
    end_date = datetime.today()  # Current date
    start_date = end_date - timedelta(days=365)  # 12 months ago from today

    # Create a date range from start to end date with a daily frequency
    dates = pd.date_range(start=start_date, end=end_date, freq='D')

    # Random temperature values between -5°C and 25°C
    np.random.seed(20)  
    temperatures = np.random.uniform(low=0, high=25, size=len(dates))

    # Create a DataFrame with dates and temperatures
    df = pd.DataFrame({'date': dates, 'temperature': temperatures})

    return df

# Step 2: Function to calculate the monthly average temperatures
def calculate_monthly_averages(df):
    """
    This function calculates the average temperature for each month.
    """
    # Sort values by date to ensure chronological order
    df = df.sort_values(by='date')

    # Extract year and month into a separate column (e.g., 2023-01)
    df['year_month'] = df['date'].dt.to_period('M')

    # Group by year_month and calculate the mean temperature for each month
    monthly_avg = df.groupby('year_month')['temperature'].mean()

    return monthly_avg

# Step 3: Calculate the monthly max and min temperatures
def calculate_monthly_extremes(df):
    """
    This function calculates the highest and lowest temperatures for each month.

    """
    df['year_month'] = df['date'].dt.to_period('M')

    # Group by year_month and calculate max and min temperatures
    monthly_max = df.groupby('year_month')['temperature'].max()
    monthly_min = df.groupby('year_month')['temperature'].min()

    return monthly_max, monthly_min

# Step 4: Function to plot monthly temperature data
def plot_monthly_temperatures(monthly_avg, monthly_max, monthly_min):
    """
    This function takes the calculated monthly averages, maximum, and minimum temperatures
    and generates a bar plot to visualize the average temperatures, with lines for max and min values.
    """
    plt.figure(figsize=(12, 7)) 

    # Plot the bar graph for monthly averages
    monthly_avg.plot(kind='line', color='lightblue', label='Average Temperature')

    # Overlay the max and min temperatures with line plots
    monthly_max.plot(kind='line', color='red', marker='o', label='Max Temperature')
    monthly_min.plot(kind='line', color='blue', marker='o', label='Min Temperature')

    plt.title('Monthly Average, Max, and Min Temperatures in the Netherlands (Dummy Data)', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.legend(loc='upper left')  

    plt.show()


print("Generating dummy temperature data for the past 12 months...")
# Generate dummy data
df = generate_dummy_temperature_data()
print("Calculating monthly average temperatures...")
# Calculate monthly average temperatures
monthly_avg = calculate_monthly_averages(df)
print("Calculating monthly max and min temperatures...")
# Calculate monthly max and min temperatures
monthly_max, monthly_min = calculate_monthly_extremes(df)
print("Plotting the temperature data...")
# Plot the monthly temperature data
plot_monthly_temperatures(monthly_avg, monthly_max, monthly_min)
print("Temperature data plot complete.")



