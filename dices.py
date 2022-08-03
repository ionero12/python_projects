#In this project, we will build a program that rolls a pair of dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.

from random import randint
from time import sleep

def get_user_guess():
  guess=int(input("Tell us your guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides)
  second_roll=randint(1,number_of_sides)
  max_val=number_of_sides*2
  print("The maxim value of dices is: %d" %max_val)
  guess=get_user_guess()
  if guess > max_val:
    print("Invalid number")
  else:
    print("Rolling...")
    sleep(3)
    print("The first roll is: %d" %first_roll)
    sleep(2)
    print("The second roll is: %d" %second_roll)
    sleep(2)
    total_roll=first_roll+second_roll
    print("Total roll is: %d" %total_roll)
    print("Result...")
    sleep(3)
    if guess == total_roll:
      print("Congrats!!!You won!")
    else:
      print("Sorry but you lost..you can be luckier next time")

roll_dice(6)


