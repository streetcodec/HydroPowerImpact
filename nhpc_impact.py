# -*- coding: utf-8 -*-
"""NHPC Impact.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sfB2M1OiKAj7CHRfGTQjp7K4zPH-rdTU
"""

import matplotlib.pyplot as plt

# Sample data
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
safety = [4, 5, 7, 8, 9, 9, 9]
beneficiary_satisfaction = [3, 4, 6, 7, 8, 9, 9]
night_activities = [2, 3, 4, 6, 7, 8, 8]

# Plotting trends
plt.figure(figsize=(10,6))

plt.plot(years, safety, label='Impact on Safety', marker='o')
plt.plot(years, beneficiary_satisfaction, label='Beneficiary Satisfaction', marker='o')
plt.plot(years, night_activities, label='Night Activities', marker='o')

# Adding titles and labels
plt.title("Trends After Installing Hydropower Plant")
plt.xlabel("Years")
plt.ylabel("Impact Rating (1-10)")

# Displaying the legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()