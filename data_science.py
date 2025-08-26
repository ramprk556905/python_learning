import numpy as np
import pandas as pd
from io import StringIO

# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])

# print("Adding arrays:")
# print(np.add(arr1, arr2))
# print(np.shape(arr1))
# print(np.reshape(arr1, (5, 1)))

arr = np.array([1,2,3,4,5,6,7])
# print(np.log(arr))
arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print( arr2d)
print(arr2d[1:,2:])
print(arr2d[0:2,2:])


# mean = np.mean(arr)
# print("Mean of arr:", mean) 

# median = np.median(arr)
# print("Median of arr:", median) 

# std_dev = np.std(arr)
# print("Standard Deviation of arr:", std_dev)

# normalized_arr = (arr - mean) / std_dev
# print("Normalized arr:", normalized_arr)

# variance = np.var(arr)
# print("Variance of arr:", variance)


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [24, 30, 22, 35, 29],    
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)  
# df['Salary']=[78000, 87900, 75000,90000,86000]
# df['Experience']=[2, 5, 1, 8, 4]

# list_data = [
#     {'Name': 'Alice', 'Age': 24, 'City': 'New York', 'Salary': 70000, 'Experience': 2},
#     {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles', 'Salary': 80000, 'Experience': 5},
#     {'Name': 'Charlie', 'Age': 22, 'City': 'Chicago', 'Salary': 60000, 'Experience': 1},
#     {'Name': 'David', 'Age': 35, 'City': 'Houston', 'Salary': 90000, 'Experience': 8},
#     {'Name': 'Eve', 'Age': 29, 'City': 'Phoenix', 'Salary': 75000, 'Experience': 4}
# ]

# df_from_list = pd.DataFrame(list_data)
# print(df_from_list)

# df = pd.read_csv('data.csv')
# # print(df.isnull())
# df['Sales_fillNA']=df['Sales'].fillna(df['Sales'].mean())
# # print(df)
# # Renaming Column
# df = df.rename(columns = {'Sales_fillNA':'Mean Sales'})
# # Changing the data in column
# df['Mean Sales']=df['Mean Sales'].astype(int)
# df['New_Value'] = df['Value'].fillna(df['Value'].mean()).astype(int)
# df['New_Value'] = df['New_Value'].apply(lambda x:x*2)
# print(df.head())

# # Grouping

# grouped_mean = df.groupby('Product')['Value'].mean()
# print(grouped_mean)
# grouped_sum = df.groupby(['Product','Region'])['Value'].sum()
# print(grouped_sum)

# # Aggregate multiple functions
# grouped_agg = df.groupby('Region')['Value'].agg(['mean','sum','count'])
# print(grouped_agg)

# Merging and Joining Dataframes
# Create sample Dataframes
# df1 = pd.DataFrame({'Key':['A','B','C'], 'Value1':[1,2,3]})
# df2 = pd.DataFrame({'Key':['A','B','D'], 'Value2':[4,5,6]})

# print(df1)
# print(df2)
# print(pd.merge(df1,df2, on = "Key",how='inner'))


# Data = '{"employee_name":"James","email": "james@gmail.com", "job_profile":[{"title1":"Team Lead","title2":"Sr.Developer"}]}'
# print(pd.read_json(StringIO(Data)))