import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

#import the files and open them 

anal_path = r"C:\Users\mypin\Downloads\Mars_Research\001357300_anal_mean_EMIRS.nc"
gues_path = r"C:\Users\mypin\Downloads\Mars_Research\001357300_gues_mean_EMIRS.nc"

anal = xr.open_dataset(anal_path)
gues = xr.open_dataset(gues_path)

# Select temperature at model level 20 (0-based index = 19)
level_idx = 19

#temperature variable at the first time step at the model level of 20

T_anal = anal['T'].isel(Time=0, pfull=level_idx)
T_gues = gues['T'].isel(Time=0, pfull=level_idx)

# Analysis increment = analysis - guess
T_inc = T_anal - T_gues


plt.figure(figsize=(9,5))

levels = np.linspace(-5, 5, 21)  

#contour plot being made to create the lat/lon/temperature plot, color map of red and blue for temp and extend to look fancy because why not

cf = plt.contourf(
    anal.lon,
    anal.lat,
    T_inc,
    levels=levels,
    cmap='RdBu_r',
    extend='both'
)

plt.colorbar(cf, label='Temperature increment (K)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Analysis Increment (Anal − Gues)\nTemperature, Model Level 20')

plt.show()

#observation file download and open, no column names and split by any white space 

import pandas as pd

obs_path = r"C:\Users\mypin\Downloads\Mars_Research\obsincr001357300_EMIRS.txt"

obs = pd.read_csv(
    obs_path,
    sep=r'\s+',
    header=None
)

#make column names 

obs.columns = ['T_obs', 'lon', 'lat', 'pressure', 'obs_minus_model']

#check to see if it did it right 
print(obs.head())


#select pressures between 200 and 250 Pa
obs_224 = obs[
    (obs['pressure'] > 200) & (obs['pressure'] < 250)
]

#how many observations were made 

print(f"Number of obs near 224 Pa: {len(obs_224)}")

plt.figure(figsize=(9,5))

levels = np.linspace(-5, 5, 21)

#new plot for scatters, starting with original plot from before with contours

cf = plt.contourf(
    anal.lon,
    anal.lat,
    T_inc,
    levels=levels,
    cmap='RdBu_r',
    extend='both'
)

#observation increments as points, lat and lon for position and the rest for size and outline color 

plt.scatter(
    obs_224['lon'],
    obs_224['lat'],
    c=obs_224['obs_minus_model'],
    cmap='RdBu_r',
    edgecolor='k',
    s=30
)

plt.colorbar(cf, label='Temperature increment (K)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(
    'Analysis Increment with Observation Increments\n'
    'Temperature, Model Level 20 & Obs near 224 Pa'
)

plt.show()
