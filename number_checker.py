import random

secret_number = random.randint(1, 100)
guesses = 0

print("Welcome to Guess the Number!")
print("I’m thinking of a number between 1 and 100.")

while True:
    # Get the player's guess
    try:
        guess = int(input("Enter your guess: "))
        guesses += 1  # Increase guess count by 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You got it in {guesses} guesses!")
            break  # Exit the loop if correct
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    except ValueError:
        print("Please enter a valid number!")