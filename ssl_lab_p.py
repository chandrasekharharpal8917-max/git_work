import random

# def number_guessing_game():
print("welcome to the number guessing game!")
print("guess a number between 0 - 100")

secret_num = random.randint(0, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 0 or guess > 100:
            print("please guess your number between 0 to 100")
            continue

        if guess < secret_num:
            print("Too low! guess again")

        elif guess > secret_num:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("invalid input! enter a valid whole number")

    # if __name__ == "__main__":
    # number_guessing_game()