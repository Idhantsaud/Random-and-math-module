import random 
num = random.randint(0,10)

print("I have generated a number between 0,10 try to guess the number ")
while True:
    user_int = int(input("Enter a number "))
    if user_int == num:
        print("You guessed the right number")
        break
    else:
       print("Try again")
