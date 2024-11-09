import numpy as np
import pandas as pd
from temperature_python import generate_dummy_temperature_data, calculate_monthly_averages, calculate_monthly_extremes

def test_temperature_functions():
    # Testing generate_dummy_temperature_data
    df = generate_dummy_temperature_data()
    assert 'date' in df.columns and 'temperature' in df.columns, "DataFrame should have 'date' and 'temperature' columns"
    assert len(df) in [365, 366], "Data should contain daily data for approximately one year"
    assert df['temperature'].min() >= 0, "Minimum temperature should be at least 0°C"
    assert df['temperature'].max() <= 25, "Maximum temperature should be at most 25°C"

    # Testing calculate_monthly_averages
    monthly_avg = calculate_monthly_averages(df)
    assert isinstance(monthly_avg, pd.Series), "Monthly average should be a pandas Series"
    assert len(monthly_avg) == 13, "Monthly averages should contain 13 entries, one for each month"

    # Testing calculate_monthly_extremes
    monthly_max, monthly_min = calculate_monthly_extremes(df)
    assert isinstance(monthly_max, pd.Series), "Monthly max should be a pandas Series"
    assert isinstance(monthly_min, pd.Series), "Monthly min should be a pandas Series"
    assert len(monthly_max) == 13, "Monthly max should contain 13 entries, one for each month"
    assert len(monthly_min) == 13, "Monthly min should contain 13 entries, one for each month"
   
