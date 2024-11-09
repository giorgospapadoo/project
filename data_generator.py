from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import toml

# Step 1: Function to generate the dummy dataset (unchanged)
def generate_dummy_temperature_data():
    """
    This function generates a dummy dataset with daily temperatures
    for the last 12 months with a range between -5°C and 25°C.
    """
    end_date = datetime.today()  # Current date
    start_date = end_date - timedelta(days=365)  # 12 months ago from today

    # Create a date range from start to end date with a daily frequency
    dates = pd.date_range(start=start_date, end=end_date, freq='D')

    # Random temperature values between -5°C and 25°C
    np.random.seed(20)  
    temperatures = np.random.uniform(low=0, high=25, size=len(dates))

    return dates, temperatures

# Step 2: Generate data
dates, temps = generate_dummy_temperature_data()

# Step 3: Convert to desired output format
output_data = [{"date": date.strftime('%Y-%m-%d'), "temperature": round(temp, 1)} for date, temp in zip(dates, temps)]

# Step 4: Write to TOML file
output = {"temperature_data": output_data}

with open('dataFrame.toml', 'w') as f:
    toml.dump(output, f)
