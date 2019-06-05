print("Please type your guess number: ")
secret = 9
chance = 3

while chance > 0:
    guess = int(input("Guess: "))
    chance = chance - 1
    if guess == secret:
        print("You win!")
        break
    else:
        print(f"Fail! You still have {chance} time(s) to input ")

else:
    print('Sorry, you failed!')