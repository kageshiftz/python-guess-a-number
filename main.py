import random

secret_number = random.randint(1, 100)
attempts = 0

print("================================")
print("       NUMBER GUESSING GAME")
print("================================")
print()
print("Picking a number between 1 and 100.")

while True:
    guess = int(input("Your Guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print()
        print("Correct! 🎉")
        print(f"You got it in {attempts} attempts.")
        break