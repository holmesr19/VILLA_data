'''
purpose: prep tei xml's from perseus for upload into a real reference system (VILLA)
author: bancks holmes
'''
import numpy, pandas, filesystem

## build a list of every file in the dowload data.
files = filesystem.listFiles('/Users/owner/code/VILLA_data/Classics')
df = pandas.DataFrame(files, columns=['files'])
print(df)

## parse file path for all the info it holds, store in a dataframe

## parse xml into dataframe

## cast dataframe into json docs