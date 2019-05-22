

import random

number = random.randint(1, 10)
tries = 1

name = input("Welcome! Please enter your name...")
print ("Hello", name + ".", )

question = input("Are you ready to play my game? [Y/N]")
if question == "n":
  print("Well you are no fun")
  
if question == "y":
  print("I'm thinking of a number between 1 & 10, can you guess it?")
  guess = int(input("Your guess: "))
  while guess != number:
    tries += 1
    if guess > number:
      print("lower...")
    if guess < number:
      print("higher...")
    guess = int(input("Try again: "))
    if guess == number:
      print("You got it!", name, "wins! The number was", number, "and it only took you", tries, "tries!")
      print("Thanks for playing!")