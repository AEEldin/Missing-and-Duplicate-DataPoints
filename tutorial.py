
'''
Prepare the matplotlib library
Python version 3.8 is the most stable version, used in the different tutorials

python3 --version
pip3 --version
pip3 install pandas
pip3 install numpy
'''

# assume you have your data stored in a .csv file somewhere on your computer, the first step is to load and read such data
# for these tutorials, we will generate data using https://www.mockaroo.com or https://cobbl.io and test the different functions offered by the libraries we imported


import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)    # use pandas library to read the first 5 rows of your dataset

print(data.info())                        # Print statistical information about the dataset (e.g., the columns names and their data types)
print(data.head())                        # Print the first 5 records of your dataset along with the header


# handling missing values per column

data["First_name"].fillna("No Name", inplace = True)    # replace NULL or NaN in the "First_name" column with "No Name" string
data["Last_name"].fillna("No Name", inplace = True)     # replace NULL or NaN in the "Last_name" column with "No Name" string
data["State"].fillna("No State", inplace = True)        # replace NULL or NaN in the "State" column with "No State" string

meanValue = data["Apt"].mean()                          # calculate the mean value on the Apt column
data["Apt"].fillna(meanValue, inplace = True)           # replace NULL or NaN in the "Apt" column with -1 value


# drop the duplicates
data.drop_duplicates(inplace = True)

print(data)

# write the updated info back to another csv file
data.to_csv('updatedEmployeeInfo.csv', sep='\t', encoding='utf-8', index=False)
