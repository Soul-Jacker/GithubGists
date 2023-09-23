import os
import glob
from RISparser import readris
import pandas as pd

# Fetch all .ris files in the current directory
files = glob.glob('*.ris')

consolidated_data = []

for file in files:
    with open(file, errors="ignore") as bibliography_file:
        entries = readris(bibliography_file)
        
        # Filter out entries with 'unknown_tag'
        filtered_entries = [entry for entry in entries if 'unknown_tag' not in entry]
        
        # Convert filtered entries to DataFrame and append to consolidated_data list
        consolidated_data.append(pd.DataFrame(filtered_entries))

# Concatenate all individual DataFrames to get the final DataFrame
end = pd.concat(consolidated_data, ignore_index=True)
