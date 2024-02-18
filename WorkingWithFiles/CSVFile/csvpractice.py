# Initally i had done a mistake that i had created this file with filename csv.py so don't do that mistake it will 
# create an error and doesn't let your program run


#importing csb
import csv

sample_file ='example.csv' # getting the file
with open(sample_file, 'r') as file:
    reader = csv.reader(file) # reading the file
    for row in reader: 
        print(row) #printing each row


data = [
    ['Product', 'Category', 'Price'],
    ['T-Shirt', 'Cloth', 'Rs 700'],
    ['Trimmer', 'Electronics', 'Rs 450'],
    ['Laptop', 'Electronics', 'Rs 600000']
],   # be alert with the comma

with open('datas.csv', 'w',newline='\n') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# The above one and below one gives separate output

data = [
    ['Product', 'Category', 'Price'],
    ['T-Shirt', 'Cloth', 'Rs 700'],
    ['Trimmer', 'Electronics', 'Rs 450'],
    ['Laptop', 'Electronics', 'Rs 600000']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

        


with open('datas.csv', 'r') as file:
    reader = csv.DictReader(file) # reads the value as dictonary
    for row in reader:
        print(row['Product'], row['Category']) # returns only the Product name and Category as these both are only considered here


# Working with DictWriter 

fieldnames = ['Name', 'email', 'Age']  # Initializing the Keys
data =[
    {'Name': 'sam', 'email' : "s@gmail.com", 'Age':22},
    {'Name': 'mike', 'email' : "m@gmail.com", 'Age':26},
]

with open('sample.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames) # Assigning the Keys
    writer.writeheader()
    writer.writerows(data) # Writing the data 




