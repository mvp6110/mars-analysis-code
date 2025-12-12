# mars-analysis-code
Python code used to compute and visualize temperature analysis increments (analysis minus guess) from EMIRS model output
# Mars Analysis Code – EMIRS

This repository contains Python code used to compute and visualize
temperature analysis increments (analysis minus guess) from
EMIRS model output.

## Files
- `Analysis_and_Observation_Increments_EMIRS.py`

## Required data files
- `001357300_anal_mean_EMIRS.nc`
- `001357300_gues_mean_EMIRS.nc`

*(Data files are not included unless otherwise specified.)*

## How to run
1. Place the required `.nc` files in the same directory as the script
2. Run:
   ```bash
   python Analysis_and_Observation_Increments_EMIRS.py
