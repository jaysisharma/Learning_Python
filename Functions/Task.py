# Create a program that simulates a simple guessing game. The program should:

# Generate a random number between 1 and 100 as the target number.
# Prompt the user to guess the target number.
# Provide feedback to the user based on their guess:
# If the guess is correct, print "Congratulations! You guessed the number!"
# If the guess is higher than the target number, print "Too high! Try again."
# If the guess is lower than the target number, print "Too low! Try again."
# Allow the user to continue guessing until they correctly guess the target number.
# Keep track of the number of attempts the user takes to guess the target number and print the number of attempts at the end.



import random as r

random_num = r.randint(1,100)
attempt = 0
while True:
    user_input = int(input("Guess the random number "))
    print(random_num)
    attempt +=1
    if (user_input == random_num):
        print('Congratulations! You guessed the number!')
        print("You had done total :", attempt ,"attempts")
        break
    if (user_input > random_num ):
        print("Too high,Try again")
    else:
        print('Too low, Try again')

