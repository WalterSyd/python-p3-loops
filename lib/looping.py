#!/usr/bin/env python3

def happy_new_year():
    #apply & check countdown condition
    i = 10
    while i > 0:
        print(i)
        #Decrement the counter
        i -= 1
        #print message after countdown
    print("Happy New Year!")
#call the fn 
happy_new_year()


def square_integers(int_list):
    # code goes here!
  if len(int_list) == 0:
    #return empty list to store squared integers
    return []
  else:
    # return squared integers in a list
    return [i**2 for i in int_list]

def fizzbuzz():
    # code goes here!
    
    # define the range of numbers you want to loop over
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)