##### day 1 #####

print ( " This is day 3 of my 30 day coding challenge")

def addition():
    a = 10
    b = 11

    c = a + b
    print(c)


def operations():
    num1 = int(input("Enter a number from 1-10: "))
    num2 = int(input("Enter a second number from 1-10:  "))
    print("Addition:", num1 + num2)
    print("Subtraction:", num2 - num1)
    print("Multiplication:", num2 * num1)
    print("Division:", num2 % num1)
    
##### day 2 : conditionals #####

def odd_even_checker():
    num1 = int(input("Enter a number from 1-10: "))
    num2 = int(input("Enter a second number from 1-10:  "))
    if num1 % 2 == 0:    
        print("number is even")
    else:
        print("number is odd")
    
        
##odd_even_checker()

#### day 3 : loops ##### 
### multiplication table ###


def multiplication_game():
    print("Welcome to the multiplication table game! ")
    num = int(input("Enter a number: "))

    i = 0
    for i in range (0, 12):
        if num <= 12:
            i = i + 1
            print(num, "x", i, "=", num * i)
        else:
            return print("Number outside of range, please try again")
        
#### day 4 : functions, parameters #####

### turned lines of code into functions ####

multiplication_game()

### day 5 : lists & dictionaries ###
### contact book add/search

fruits = [ 'apples', 'banana', 'orange', 'grapes', 'kiwi' ]
numbers = [ 1, 2, 3, 4, 5, 6, 7]

## dictionary ##
newdict = {
  "brand": "Nike",
  "size": "7",
  "year": 2025
}

print(newdict)

### contact book ###
