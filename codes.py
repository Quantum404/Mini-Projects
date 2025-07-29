## Chore Distribution
list_names = []
n = int(input('Enter the number of People for chores '))
for i in range(n):
    element = input(f"Enter name {i+1}: ")
    list_names.append(element)

import random
print("Cooking will be done by", random.choice(list_names))
print("Laundry will be done by", random.choice(list_names))
print("Dishes will be done by", random.choice(list_names))
print("Cleaning will be done by", random.choice(list_names))

## Calculator 
def add(a,b):
  print(a+b)
def sub(a,b):
  if a>b:
    print(a-b)
  else:
    print(b-a)
def mul(a,b):
    print(a*b)
def div(a,b):
  print(round(a/b,2))

print("---Calculator---")
x = int(input("Enter first number "))
y = int(input("Enter second number "))
Z = str(input("Enter the operation + for add, - for sub, * for multiply and / for divide "))
if Z == '+':
  add(x,y)
elif Z == '-':
  sub(x,y)
elif Z == '*':
  mul(x,y)
else:
  div(x,y)

## Guessing game

print("Guessing game - Select a number from 1 to 100\n You have 3 chances!!!")
import random as r
X = r.randint(1,100)
for i in range(3):
  try:
    Y = int(input("Enter your guess "))
  except:
    print("Enter a valid number")
    continue

  if X==Y:
    print("You've guessed it right")
  elif Y<X:
    print("The number you chose is too low")
  else:
    print("The number you chose is quite high")
