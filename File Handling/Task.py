# Task: Write a Python program that reads a text file containing a list of numbers, one number per line. The program should calculate the sum of all the numbers in the file and print the result.

# Requirements:

# Create a text file named "numbers.txt" and populate it with a list of numbers, each on a separate line.
# Write a Python program that reads the contents of "numbers.txt", calculates the sum of all the numbers, and prints the result.
# The program should handle cases where the file contains non-numeric values gracefully, skipping them and continuing with the calculation.
# Ensure to close the file properly after reading its contents.

# initalizing sum to zero so we can add the value of the file
sum= 0

with open('/home/jaysi/Desktop/Learning_Python/File Handling/numbers.txt', 'r') as file: # Opening the file
    number = file.readlines() # reading file lines
    for i in number: #created a loop to read each line
        try:
            sum += int(i) # Parsing the file values to int and adding the value to sum
        except ValueError: # If error occurs it will skip the line and continue the further process
            continue
    print("The Sum of the number is :", sum) # Printing the Final Value