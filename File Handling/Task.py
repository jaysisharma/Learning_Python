# Task: Write a Python program that reads a text file containing a list of numbers, one number per line. The program should calculate the sum of all the numbers in the file and print the result.

# Requirements:

# Create a text file named "numbers.txt" and populate it with a list of numbers, each on a separate line.
# Write a Python program that reads the contents of "numbers.txt", calculates the sum of all the numbers, and prints the result.
# The program should handle cases where the file contains non-numeric values gracefully, skipping them and continuing with the calculation.
# Ensure to close the file properly after reading its contents.

sum= 0

with open('/home/jaysi/Desktop/Learning_Python/File Handling/numbers.txt', 'r') as file:
    number = file.readlines()
    for i in number:
        try:
            sum += int(i)
        except ValueError:
            continue
    print("The Sum of the number is :", sum)