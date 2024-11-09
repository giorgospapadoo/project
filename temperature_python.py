# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import toml

# Step 1: Load data from the TOML file
with open('dataFrame.toml', 'r') as f:
    data = toml.load(f)

# Extracting data from nested structure in the TOML file
# Since we structured it as "temperature_data", we extract that list
temperature_data = data["temperature_data"]

# Create lists for dates and temperatures based on the loaded data
dates = [entry["date"] for entry in temperature_data]
temps = [entry["temperature"] for entry in temperature_data]

# Store data in a DataFrame
df = pd.DataFrame({'date': dates, 'temperature': temps})

df['date'] = pd.to_datetime(df['date'])

# Ensure that 'temperature' values are numeric
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Check for any non-numeric entries that might have been converted to NaN
if df['temperature'].isna().any():
    print("Warning: Non-numeric values found in temperature column, replaced with NaN.")
    # Optionally, drop rows with NaN in the temperature column if needed
    df = df.dropna(subset=['temperature'])


print(df['date'])

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

# Main Script Execution
print("Generating dummy temperature data for the past 12 months...")
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
