#Assignment 02 - Question 01 - Task 01
from os import listdir
import pandas as pd

FILE_EXTENSION = '.csv'
TARGET_FILE = 'allText.txt'
COLUMN_NAMES = ['SHORT-TEXT', 'TEXT']

fileNames = listdir()
open(TARGET_FILE, "w").close()
pd.set_option('display.max_colwidth', None)
for filename in fileNames: 
    if filename.endswith(FILE_EXTENSION):
        print('Reading ' + filename)
        df = pd.read_csv(filename, usecols=lambda x: x in COLUMN_NAMES)   
        with open(TARGET_FILE, 'a') as the_file:
            the_file.write((df[df.columns[0]]).to_string())