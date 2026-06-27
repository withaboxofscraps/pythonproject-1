import random
x=random.randint(1,100)
while True:
    blah=int(input("Enter your guess: "))
    if(blah>x):
      print("Your guess is too high.")
    elif(blah<x):
      print("Your guess is too low.")
    else:
      print("Congratulations! You guessed the number.")
      break