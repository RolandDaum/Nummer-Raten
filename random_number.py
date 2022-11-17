import random

while 1 == 1:
    von = int(input("Zahlenbereich - Von: "))
    bis = int(input("Zahlenbereich - Bis: "))
    num = random.randint(von, bis)
    num_guess = ""
    guess_count = 1
    while num != num_guess:
        num_guess = int(input("Guess number: "))
        if num_guess > num:
            print("lower")
            guess_count = guess_count + 1
        if num_guess < num:
            print("higher")
            guess_count = guess_count + 1
    print("Gueesed right with ", guess_count, "Guesses.")