import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

solar_eclipse = pd.read_csv('eclipse_subset.csv')

plt.scatter(solar_eclipse['temp_sun'], solar_eclipse['full_sun_brightness'], label='Full Sun Brightness', marker='o', s=1)
plt.scatter(solar_eclipse['temp_shade'], solar_eclipse['shade_brightness'], label='Shade Sun Brightness', marker='o', s=1)
plt.xlabel('Temperature')
plt.ylabel('Brightness')
plt.title('Brightness vs Temperature')
plt.legend()
plt.savefig('brightness_vs_temperature.png')
