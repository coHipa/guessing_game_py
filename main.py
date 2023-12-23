import random

user_guess = input("What is your guess? ")
secret_number = random.randint(0, 10)

if user_guess == secret_number:
    print("Your guess was right")
else:
    print("Not even close, my guess was:", secret_number)