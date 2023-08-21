# Handling Missing and Duplicate DataPoints using Pandas

In a [previous tutorial](https://github.com/AEEldin/Pandas-read_CSV), we learned how to use pandas' read_csv() function to load and read the full csv holding your dataset or parts of the file (by rows or columns). In this tutorial, we will discuss using Python's Pandas library to detect and handle missing and duplicate data records as an essential technique for cleaning your dataset.


### Part 1: loading and read your dataset
Assume you have your data stored in a .csv file somewhere on your computer; the first step is to load and read such data. For these tutorials, we will generate data using https://www.mockaroo.com or https://cobbl.io and test the different functions offered by the libraries we imported. Our dataset is named employeeInfo.csv and stores randomly generate information about employees (e.g., names, addresses, salaries, IDs, emails)

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv')    # use pandas library to read the dataset
print(data.info())                        # Print statistical information about the dataset (e.g., the columns names and their data types)
print(data.head())                        # Print the first 5 records of your dataset along with the header
```


### Part 2: Handling missing data using the dropna() function

The dropna() function detects missing values and is used to eliminate the corresponding rows. Using this function, any row with at least one missing value (NULL or NaN) will be removed. 
```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)      # let's test the dropna() function on the firtst rows only
print(data)                                            # print the original DataFrame

newData = data.dropna()                                # apply dropna()
print(newData)                                         # print the original DataFrame
```

The dropna(), by default, returns a new DataFrame without changing the original DataFrame. To reflect the changes on the original DataFrame, use the inplace = True argument in the dropna() function.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)      # let's test the dropna() function on the firtst rows only
data.dropna(inplace=True)                              # apply dropna() with inplace parameter

print(newData)                                         # print the updated DataFrame
```

You can use the drop() function to drop columns.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)      # let's test the dropna() function on the firtst rows only
to_drop = ['First_name','Last_name','City']            # list the columns to drop

data.drop(columns=to_drop, inplace=True)
print(data)
```


### Part 2: Handling missing data using the fillna() function

The fillna() function replaces missing data points (e.g., NULL or NaN) with values instead of deleting the entire rows

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)                # let's test the dropna() function on the firtst rows only
data.fillna("Missing Value", inplace=True)                       # replace NULL or NaN with "Missing Value" string

print(data)                                                      # print the updated DataFrame
```



However, the example we developed replaces all empty cells with a _Missing Value_ string. To define a replacement per column, we need to specify the column name for the fillna() function.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)                # let's test the dropna() function on the firtst rows only

data["Last_name"].fillna("Missing Name", inplace = True)         #replace NULL or NaN in the "Last_name" column with "Missing Value" string
data["Apt"].fillna(-1, inplace = True)                           #replace NULL or NaN in the "Apt" column with -1 value

print(data)                                                      # print the updated DataFrame
```


You can also replace a missing value with a statistical value calculated from the entire column. Pandas provides a set of functions that can be used for this purpose:
+ Mean (using mean()) is the average value which is the sum of all values divided by their number.
+ Median (using median()) is the value in the middle after sorting the values ascendingly.
+ Mode (using mode()) is the value of the most frequent value in the column.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)            # let's test the dropna() function on the firtst rows only

meanValue = data["Apt"].mean()                               # calculate the mean value on the "Apt" column

data["Last_name"].fillna("Missing Name", inplace = True)     # replace NULL or NaN in the "Last_name" column with "Missing Value" string
data["Apt"].fillna(meanValue, inplace = True)                # replace NULL or NaN in the "Apt" column with the calculated mean value

print(data)                                                  # print the updated DataFrame
```





### Part 3: Discovering and handling duplicates

We can use the duplicated() function to discover duplicates in a dataset. For each row, the duplicated() function returns _True_ if such row is duplicated and _False_ if such row is unique.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)

print(data.duplicated())
```

The drop_duplicates() function is used to remove the duplicates.

```
import pandas as pd

data = pd.read_csv('employeeInfo.csv', nrows = 5)

data.drop_duplicates(inplace = True)

print(data)

# write the updated info back to another csv file
data.to_csv('updatedEmployeeInfo.csv', sep='\t', encoding='utf-8', index=False)
```
