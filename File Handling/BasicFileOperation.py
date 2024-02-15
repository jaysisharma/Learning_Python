
# Reading a file 
# Opening a file
# syntax =  open('path', permission)
file = open('/home/jaysi/Desktop/Learning_Python/File Handling/abc.txt', 'r') 

print(file.readable) # Returns a boolean value that file is readble or not

content = file.read() # Reading the file
print(content) # Printing the content

content2 = file.readline() # List just a line of the file
print(content2)

content3 = file.readlines() #Returns the whole file as a  list
print(content3)

file.close() # Closing the file



# Writing on a file

file = open('/home/jaysi/Desktop/Learning_Python/File Handling/abc.txt', 'w')
file.write("Hello This is overriden")
file.close()

# Appending on a file
file = open('/home/jaysi/Desktop/Learning_Python/File Handling/abc.txt', 'a')

file.write('\nThis is appended value from program')
file.close()


#by using with it automatically closes the file

with open('/home/jaysi/Desktop/Learning_Python/File Handling/abc.txt', 'r') as file:
    content = file.read()
    print(content)


