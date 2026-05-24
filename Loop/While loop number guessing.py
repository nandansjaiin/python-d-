#Generate a random number, user guesses until correct
print("Generate a random number, user guesses until correct")
num = 0
a = 5
while num != a:
    num = int(input("Enter your guess:"))
    if num == a:
        print("You have guessed correct")
    else:
        print("wrong! guess again")