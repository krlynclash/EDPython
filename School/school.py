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