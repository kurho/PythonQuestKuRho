import csv

with open('example1.csv' , 'r') as file:
    reader = csv.reader(file)

    next(reader)

    for line in reader:
        print(line[0])
