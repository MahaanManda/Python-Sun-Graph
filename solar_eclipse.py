import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

solar_eclipse = pd.read_csv('eclipse_subset.csv')

plt.scatter(solar_eclipse['temp_sun'], solar_eclipse['full_sun_brightness'], label='Full Sun Brightness', color='m', s=10)
plt.scatter(solar_eclipse['temp_shade'], solar_eclipse['shade_brightness'], label='Shade Sun Brightness', color='b', s=10)
plt.grid(axis = 'y', linestyle=':', color='cyan')

plt.xlabel('Temperature')
plt.ylabel('Brightness')
plt.title('Brightness vs Temperature')
plt.legend()
plt.savefig('brightness_vs_temperature.png')
