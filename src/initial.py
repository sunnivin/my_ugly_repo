import pandas as pd
from matplotlib import pyplot as plt

NUM_MEASUREMENTS = 25

# read data from file
data = pd.read_csv('data/temperatures.csv', nrows=NUM_MEASUREMENTS)
temperatures = data['Air temperature (degC)']

# compute statistics
mean = sum(temperatures)/NUM_MEASUREMENTS

# plot results
plt.plot(temperatures, 'r-')
plt.axhline(y=mean, color='b', linestyle='--')
plt.savefig('25.png')
plt.clf()
