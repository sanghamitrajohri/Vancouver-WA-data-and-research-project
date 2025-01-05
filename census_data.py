# -*- coding: utf-8 -*-
"""Census_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RB9DGZJm7uXNYNtUSox4zPZDELD2MUG2
"""

import matplotlib.pyplot as plt
import pandas as pd
from google.colab import files

# Load the uploaded file
census_data = pd.read_csv('/content/census2020.csv')
# Calculate per capita electricity consumption
census_data['per_capita_consumption'] = census_data['electricity_consumption'] / census_data['total_population']

# Plot per capita electricity consumption vs median income
plt.figure(figsize=(10, 6))
plt.scatter(census_data['median_income'], census_data['per_capita_consumption'], color='blue', alpha=0.7)
plt.title('Per Capita Electricity Consumption vs Median Income')
plt.xlabel('Median Income (USD)')
plt.ylabel('Per Capita Electricity Consumption (kWh)')
plt.grid(True)
plt.show()

# Calculate race percentages
census_data['percent_white'] = census_data['population_white_alone'] / census_data['total_population'] * 100
census_data['percent_black'] = census_data['population_black_or_african_american_alone'] / census_data['total_population'] * 100
census_data['percent_asian'] = census_data['population_asian_alone'] / census_data['total_population'] * 100
census_data['percent_native_american'] = census_data['population_american_indian_and_alaska_native_alone'] / census_data['total_population'] * 100
census_data['percent_two_or_more'] = census_data['population_two_or_more_races'] / census_data['total_population'] * 100

# Re-defining the 'races' and 'race_labels' for the plot
races = ['percent_white', 'percent_black', 'percent_asian', 'percent_native_american', 'percent_two_or_more']
race_labels = ['White', 'Black or African American', 'Asian', 'Native American', 'Two or More Races']

# Create subplots for each race, adjusting for 5 plots (2 rows and 3 columns)
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# Plotting the 5 demographic groups
for i, race in enumerate(races):
    row = i // 3
    col = i % 3
    ax[row, col].scatter(census_data[race], census_data['per_capita_consumption'], alpha=0.7)
    ax[row, col].set_title(f'Per Capita Consumption vs {race_labels[i]} (%)')
    ax[row, col].set_xlabel(f'{race_labels[i]} Population (%)')
    ax[row, col].set_ylabel('Per Capita Electricity Consumption (kWh)')
    ax[row, col].grid(True)

# Hide the sixth (last) subplot
fig.delaxes(ax[1, 2])

# Adjust layout
plt.tight_layout()
plt.show()

# Sort the per capita consumption values
sorted_consumption = np.sort(census_data['per_capita_consumption'])

# Calculate the CDF
cdf = np.arange(1, len(sorted_consumption) + 1) / len(sorted_consumption)

# Plot the CDF
plt.figure(figsize=(12, 8))
plt.plot(sorted_consumption, cdf, marker='.', linestyle='none', color='blue')
plt.title('CDF of Per Capita Electricity Consumption (2020 Census)', fontsize=14)
plt.xlabel('Per Capita Electricity Consumption (kWh)', fontsize=12)
plt.ylabel('Cumulative Probability', fontsize=12)
plt.grid(True)

# Annotate all ZIP codes, ensuring no overlap
for _, row in census_data.iterrows():
    zip_code = row['zip_code']
    per_capita = row['per_capita_consumption']
    index = np.searchsorted(sorted_consumption, per_capita)
    cdf_value = cdf[index - 1] if index > 0 else 0

    # Adjust text offset dynamically based on position
    xy_offset = (5, -5) if cdf_value < 0.5 else (5, 5)
    plt.annotate(f'{int(zip_code)}', (per_capita, cdf_value),
                 textcoords="offset points", xytext=xy_offset, ha='left', fontsize=8, color='black', alpha=0.8)

plt.show()

# Extract data for outliers 98642 and 98686
outliers_data = census_data[census_data['zip_code'].isin([98642, 98686])]

# Calculate statistics for comparison with other ZIP codes
mean_consumption = census_data['per_capita_consumption'].mean()
median_consumption = census_data['per_capita_consumption'].median()
std_consumption = census_data['per_capita_consumption'].std()

# Compare the outliers' data to the overall statistics
outliers_data_vs_stats = {
    "Outliers": outliers_data[['zip_code', 'total_population', 'electricity_consumption', 'per_capita_consumption']],
    "Mean Consumption": mean_consumption,
    "Median Consumption": median_consumption,
    "Std Dev Consumption": std_consumption
}

outliers_data_vs_stats

# Create subplots for each race, adjusting for 5 plots (2 rows and 3 columns)
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# Plotting the electricity consumption vs percentage of each race
for i, race in enumerate(races):
    row = i // 3
    col = i % 3
    ax[row, col].scatter(census_data[race], census_data['electricity_consumption'], alpha=0.7)
    ax[row, col].set_title(f'Electricity Consumption vs {race_labels[i]} Population (%)')
    ax[row, col].set_xlabel(f'{race_labels[i]} Population (%)')
    ax[row, col].set_ylabel('Electricity Consumption (kWh)')
    ax[row, col].grid(True)

# Hide the sixth (last) subplot
fig.delaxes(ax[1, 2])

# Adjust layout
plt.tight_layout()
plt.show()

# Fit a linear regression line to the per capita consumption vs income data
from sklearn.linear_model import LinearRegression
import numpy as np

# Reshape the data for the regression model
X = census_data['median_income'].values.reshape(-1, 1)
y = census_data['per_capita_consumption'].values

# Create and fit the linear regression model
reg_model = LinearRegression()
reg_model.fit(X, y)

# Predict values using the fitted model
y_pred = reg_model.predict(X)

# Plot the per capita consumption vs income and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(census_data['median_income'], census_data['per_capita_consumption'], color='blue', alpha=0.7, label='Data')
plt.plot(census_data['median_income'], y_pred, color='red', label='Regression Line')
plt.title('Per Capita Electricity Consumption vs Median Income with Regression Line')
plt.xlabel('Median Income (USD)')
plt.ylabel('Per Capita Electricity Consumption (kWh)')
plt.legend()
plt.grid(True)
plt.show()

# Fit regression lines for per capita consumption vs percentages of each race
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

for i, race in enumerate(races):
    row = i // 3
    col = i % 3

    # Prepare the data for regression
    X_race = census_data[race].values.reshape(-1, 1)
    y_consumption = census_data['per_capita_consumption'].values

    # Fit the regression model
    reg_model_race = LinearRegression()
    reg_model_race.fit(X_race, y_consumption)

    # Predict the values using the fitted model
    y_race_pred = reg_model_race.predict(X_race)

    # Scatter plot and regression line
    ax[row, col].scatter(census_data[race], census_data['per_capita_consumption'], alpha=0.7)
    ax[row, col].plot(census_data[race], y_race_pred, color='red')
    ax[row, col].set_title(f'Per Capita Consumption vs {race_labels[i]} Population (%)')
    ax[row, col].set_xlabel(f'{race_labels[i]} Population (%)')
    ax[row, col].set_ylabel('Per Capita Electricity Consumption (kWh)')
    ax[row, col].grid(True)

# Hide the sixth (last) subplot
fig.delaxes(ax[1, 2])

# Adjust layout
plt.tight_layout()
plt.show()

# Plotting income vs race composition without regression
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

# Define race composition columns and labels
races = ['percent_white', 'percent_black', 'percent_asian', 'percent_native_american', 'percent_two_or_more']
race_labels = ['White', 'Black or African American', 'Asian', 'Native American', 'Two or More Races']

# Create scatter plots for each race
for i, race in enumerate(races):
    row = i // 3
    col = i % 3
    ax[row, col].scatter(census_data[race], census_data['median_income'], alpha=0.7)
    ax[row, col].set_title(f'Median Income vs {race_labels[i]} Population (%)')
    ax[row, col].set_xlabel(f'{race_labels[i]} Population (%)')
    ax[row, col].set_ylabel('Median Income (USD)')
    ax[row, col].grid(True)

# Hide the sixth (last) subplot
fig.delaxes(ax[1, 2])

# Adjust layout
plt.tight_layout()
plt.show()

"""Seems to be a moderate positive relationship between the percentage of White individuals and median income, and a moderate negative relationship between the percentage of Black or African American individuals and income."""