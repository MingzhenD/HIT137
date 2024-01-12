import os
import pandas as pd
import zipfile
import io

# Get the user's directory
home_dir = os.path.expanduser("~")

# Construct path to zipped folder in Downloads directory
zip_folder = "Downloads"
zip_file_name = "Assignment 2.zip"
zip_path = os.path.join(home_dir, zip_folder, zip_file_name)

every_txts = []

# Open zip file and iterate through CSV files
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        if file_name.endswith(".csv"):
            # Read the CSV file directly from the zip archive
            with zip_ref.open(file_name) as file:
                df = pd.read_csv(io.TextIOWrapper(file))

                # Extract the 'TEXT' or 'SHORT-TEXT' column and append to the list
                if 'TEXT' in df.columns:
                    every_txts.extend(df['TEXT'].astype(str))
                elif 'SHORT-TEXT' in df.columns:
                    every_txts.extend(df['SHORT-TEXT'].astype(str))

# Put texts into one string
consolidated_txt = '\n'.join(every_txts)

# Path to text file
outward_txt_file = os.path.join(home_dir, zip_folder, "Combined_Text.txt")

# Publish the txt file
with open(outward_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write(consolidated_txt)

print("Texts exported and pasted to:", outward_txt_file)
