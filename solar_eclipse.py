import pandas as pd
import matplotlib.pyplot as plt

# Read in the data Pandas DATAFRAME and close file after done
with open('eclipse_subset.csv') as f:
    df = pd.read_csv(f)

# Sorting the DataFrame based on 'temp_sun' column
df_sorted = df.sort_values(by='temp_sun')

# Extracting sorted data from DataFrame
full_sun_brightness = df_sorted['full_sun_brightness']
shade_brightness = df_sorted['shade_brightness']
temp_sun = df_sorted['temp_sun']
temp_shade = df_sorted['temp_shade']

# Specify the size of the markers
marker_size = 1

# Plot the data using scatter plot with reduced marker size
plt.scatter(temp_sun, full_sun_brightness, label='Full Sun Brightness', marker='o', s=marker_size)
plt.scatter(temp_shade, shade_brightness, label='Shade Sun Brightness', marker='o', s=marker_size)

##label the axes
plt.xlabel('Temperature')
plt.ylabel('Brightness')
plt.title('Brightness vs Temperature')
plt.legend()




#display
plt.grid(True)
plt.show()
