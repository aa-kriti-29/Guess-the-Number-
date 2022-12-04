print('Welcome to "Guess The Number" game!!')
print("You will get only 10 guesses.")
for i in range(10):
    n = 45
    print("Guess ",i+1)
    num = int(input("Guess a number:"))
    if (num == n):
        print("You have guessed it right\n Congratulations!!")
        break
    elif (num < n and 0 < num < 30):
        print("Your choice is too small than the number")
        continue
    elif (num < n and 30 < num < 40):
        print("Your number is small.")
        continue
    elif (num < n and num >= 41):
        print("Too close")
        continue
    elif (num > n and 46 <= num <= 50):
        print("Too close")
        continue
    elif (num > n and 51 <= num <= 70):
        print("Your number is large")
        continue
    elif (num > n and 71 <= num <= 100):
        print("Too far ")
        continue
    else:
        print("Number is between 0 to 100")
        continue
