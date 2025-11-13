import pandas as pd

#global data
data= []
filename = "./School/Schools.csv"

def ReadFile():
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))


ReadFile()

print(data)

linecount = 0
for line in data:
    linecount += 1

    #print(linecount)

yourschool = "JOSEPH GREENBERG SCHOOL"


# for line in data:
#     # words = line.split(',')
#     for word in words:
#         if word == yourschool:
#             print(word)
#             print(words)
#             print(words[8])





"""
PANDAS
"""

import pandas as pd

filename = "./School/Schools.csv"

df = pd.read_csv(filename)

# print(df)

# print(df.head())

# print(df.info())

#print(df.describe())

# print(df.columns())

# print(df.iloc[8])

# print(df["school_name_label"].unique())

# print(df["school_name_label"].nunique())

# print(df[df["school_name_label"] == "JOSEPH GREENBERG SCHOOL"])

print(df.sort_values(by=["zip_code"]))


import numpy as np
# x = [1, 2, 3, 4]
# y = 2x^2 + 3x + 1
# y = [#, #, #, #]

x = np.array([1, 2, 3, 4])

y = 2 * x**2 + 3 * x + 1

print(y)



"""
2x + y = 9
x + 3y = 8

 6x + 3y = 27
 - x - 3y = -8
5x = 19
x = 19/5
x = 3.8

3.8 + 3y = 8
3y = 4.2
y = 4.2/3
y = 1.4
"""

A = np.array([[2, 1], [1, 3]])
B = np.array([9, 8])

print(np.linalg.solve(A, B))
