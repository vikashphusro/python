import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I am thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct! You found it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    start_game()