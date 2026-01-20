import random

print("Welcome to the Guess The Number. you have 10 chances to guess the number.")
print("The secret number is between 1 and 50")
secret_number = random.randint(1, 50)
attempts = int(input("How many attempts do you want?"))
is_guess_correct=False
while attempts > 0:
    print(f"you have {attempts} chances to guess the number")
    user_number = int(input("enter your number"))
    if user_number== secret_number:
        print("congrats! you guessed the number")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower="higher"
        else:
            higher_or_lower="lower"
        print(f"your guess is wrong please try {higher_or_lower} number ")

    attempts = attempts - 1
if not is_guess_correct:
    print("Bad Luck!! You exhausted your attempts.")
print(f"The secret number is {secret_number}. GAME OVER🎊🎊🎊.\nThanks for playing.")
