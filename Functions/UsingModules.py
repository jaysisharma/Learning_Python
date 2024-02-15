# Learning random Module
# importing random module
import random as r

random_number = r.random() # This will print random number from 0 to 1
print(random_number)

radom_integer = r.randint(1,10) # Generate radom value from 1 to 10
print(radom_integer)

players = ['Dhoni', 'Rohit', 'Virat', 'Bumrah'] 
choice_random = r.choice(players) # Generating random values from a list
print(choice_random) # Give random player name as output

r.shuffle(players) # Shuffle the list instead of printing random value
print(players) 

#Difference between random.choice and random.shuffle is Choice will print random value and shuffle will shuffle the list

alphabets = ['a','e','i','o','u']
random_sample = r.sample(alphabets, 2) # sample return the random value by the help of second parameter like 1,2,4
print(random_sample)