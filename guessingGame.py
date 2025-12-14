def greet():
    print("Welcome to number guessing game you have 4 trials")
greet()
def welcome(name, title="Mr",title2="Mrs" , sex="m/f"):
    name = input("Enter your name: ")
    sex = input("Are you a male or female?(m/f) ")
    if sex == "m":
        print(f"Welcome {title} {name.capitalize()} to this guessing game")
    elif sex == "f":
        print(f"Welcome {title2} {name.capitalize()} to this guessing game")
welcome("")
import random
number_to_guess = random.randint(1,10)
def getuser(count=0):
    user = int(input("Input the number you want to guess: "))
    while user != number_to_guess:
        count += 1
        if count == 4:
            break
        elif user < number_to_guess:
            print("Your number is lesser")
            user = int(input("Please guess again: "))
        elif user > number_to_guess:
            print("You input an higher number: ")
            user = int(input("Please guess again: "))
    if user == number_to_guess:
        print("Congratulations!!! you won the game")
        print(f"It takes {count + 1} trails to complete the game")
getuser()
print(f"Game over, number to guess is {number_to_guess}")
