import random

print("Number guessing game")

#function to generate the random number between 1 to 9
number = random.randint(1, 9)

#While loop to count the chances of the player
while chances < 5 :

# Compare the user entered number with the number to be guessed

if guess == number:
    # if number entered by user is same as the generated
    # number by randint function then break from loop using loop
    # control statement "break"
    print("Congratulation You Won! ! !")
    break

# Check whether the user guessed the correct number
if not chances < 5 :
    print("YOU LOSE! ! ! The number is ", number)