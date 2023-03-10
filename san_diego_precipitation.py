# Import libraries and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 31)

# Create point for San Diego, CA
san_diego = Point(32.7157, 117.1611, 62)

# Get daily data
data = Daily(san_diego, start, end)
data = data.fetch()
print(data)

# Create x and y values for precipitation
x = mdates.date2num(data.prcp.index)
y = data.prcp.values

# Calculate equation for trendline for precipitation
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Plot average precipitation
plt.style.use('seaborn')
plt.rcParams["figure.figsize"] = (10, 7.5)
title = "Daily precipitation - 2022 San Diego, CA"
fig, ax = plt.subplots()
ax.set_title(title, fontsize=20)
ax.set_xlabel('Dates', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (mm)", fontsize=16)
plt.scatter(data.prcp.index, y)

count = 0
for x in data.prcp.values:
    if x > 0:
        count += 1
print("The number of times it rained in 2022 is:", count)

plt.show()