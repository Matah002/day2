print("Hello James")
print(3*2)

a = 3
b = 4
print(a+b)

integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print(new_number)
print(type(new_number))

a=5
b=8
print(a>b)

"""
num = input("Enter a number:")

print("You entered:", num)

print("Data type of num:", type(num))


name = input("What is your name:")
age = input("How old are you:")
location = input("where do you live:")

print("Hello"+ name + "you are" + age + "years old and live in" + location )

"""
a = (1, 2, 3)

b = list(a)

print(b)

a = 10

b = 3

print(a % b)


x = {}
x[2] = 10
x[1] = [20,30,40]
print(x[1][2])

#my_list[2:5] returns a list with items from index 2 to index 4.
#my_list[5:] returns a list with items from index 1 to the end.
#my_list[:] returns all list items

numbers = [21, 34, 54, 12]
numbers.append(32)
print(numbers)

prime_numbers = [2,3,5]
even_numbers = [4,6,8]

print(prime_numbers)

prime_numbers.extend (even_numbers)

print(prime_numbers)

languages = ["Python", "Swift", "C++"]
languages[2] = "C"
print(languages)

#ITERATING THROUGH A LIST

languages = ["Python", "Swift", "C++"]
for language in languages:
    print(language)


#Python List Comprehension

numbers = [number*number for number in range (1, 6)]

print(numbers)

# TUPLES

my_tuple = ("a", "p", "p", "l", "e")

print(my_tuple.count("p"))
print(my_tuple.index("l"))


# DICTIONARIES

#ITERATING THROUGH A DICTIONARY

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9:81}

for i in squares:
    print(squares[i])

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9:81}

for square in squares:
    print(square)

greet = "Hello"
for letter in greet:
    print(letter)

# ESCAPE SEQUENCES IN PYTHON.
    
#example = "He said, "What's there?""
#print(example)
    #Throws an error

#SOLUTION
    
example = "He said,\"What's there?\""
print(example)

# fStrings

name = "Cathy"
country = "UK"

print(f"{name} is from {country}")

if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

grade = 83

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#LOOPS
    
names = ["Paul", "Skinny", "Ahmad","Saruni"]

for name in names:
    print(name)

welcome_message = "Welcome to PLP"

for i in range(5):
    print(welcome_message)

count = 0
while count <= 2:
    print(count)
    count += 1

colors = ["blue","green","white","yellow","brown","cream"]
color_i_want = "white"

for color in colors:

    if color == color_i_want:
        print("They have the color I want")
        break
    print(color)

#Let's say you want to automate a gate entrance process, where the age of people entering is limited to 21 years. 
#Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.

ages = [13,24,17,36]

for age in ages:
    if age < 21:
        continue
    print(age)

# NESTED LOOPS
    
groups = [["Paul","Skinny"],["Ahmad","Gregory"]]

for group in groups:

    for name in group:
        print(name)

nums = [4, -11, 69, 53, -65]
doubled = [num * 2 for num in nums]
print(doubled)

#FUNCTIONS

def add_nums():
    print(2 + 13)

add_nums()

def is_divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
    
number = 50
result = is_divisible_by_ten(number)
print(f"Is {number} divisible by ten? {result}")


def add_nums(a, b):
    answer = a + b

    def double_it():
        double = answer * 2
        print(double)
    double_it()
    return answer
print(add_nums(2, 13))

def add_nums(a, b):
    answer = a + b
    return answer
total = add_nums(2, 13)
print(total)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

for num in range(1, 5):
    print(num)


def some_thing(number1, number2):
    first_value = number1 + 8
    second_value = number2 - 5
    return first_value

print(some_thing(13, 10))


z = lambda x : x * x

print(z(6))

def greet():
    print("Hello")

greet()

def greet_two(greeting):
    print(greeting)

greet_two("Howdy")

def greet_two(greeting):
    print(greeting)

greet_two("Hi how are you doing?")

def greet_two(greeting = "Alamsiki"):
    print(greeting)

greet_two()

def many_types(x):
    if x < 0:
        return "Hello!"
    else:
        return 0
    
print(many_types(1))
print(many_types(-1))
print(many_types(-100))


# Defining a function with an arbitrary number of
#arguments

#Defining a function capable of taking an arbitrary number of arguments can be done by prefixing 
#one of thearguments with a *

def func(*args):
    # args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

func(1, 2, 3)

list_of_arg_values = [1, 2, 3]
func(*list_of_arg_values)
func()

def func(**kwargs):
   # kwargs will be a dictionary containing the names as keys and the values as values
    for name, value in kwargs.items():
        print(name, value)

func(value1 = 1, value2 = 2, value3 = 3)
func()


my_dict = {"foo" : 1, "bar" : 2}
func(**my_dict)
func()

greet_me = lambda: "Hello"
print(greet_me())

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting("hello", "world", world="world")

def num_square(num):
    return num ** 2
print(num_square(8))

num_square = lambda num: num ** 2
print(num_square(9))

"""
def ispalindrome(string):
    if (string == string[::-1]):
        return "A Palindrome."
    else:
        return "Not a Palindrome."
    
string = input("Enter string:")

print(ispalindrome(string))

"""
class Person:

# name & age parameters passed in constructor

    def __init__(self, name, age): 

        self.name = name

        self.age = age

P1 = Person("Mutemi",65)
print(P1.name)
print(P1.age)

"""
print("This program illustrates a chaotic function")
x = eval(input("Enter a number between 0 and 1"))
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)

    """


"""
Susan is spending a year studying in Germany. She has no problems with 
language, as she is fluent in many languages (including Python). Her problem 
is that she has a hard time figuring out the temperature in the morning so that 
she knows how to dress for the day. Susan listens to the weather report each
morning, but the temperatures are given in degrees Celsius, and she is used to 
Fahrenheit. 
Fortunately, Susan has an idea to solve the problem. Being a computer science major, she never goes anywhere without her laptop computer. She thinks 
it might be possible that a computer program could help her out. 
Susan begins with an analysis of her problem. In this case, the problem is 
pretty clear: the radio announcer gives temperatures in degrees Celsius, but 
Susan only comprehends temperatures that are in degrees Fahrenheit.

"""

"""
def main () : 

    celsius = eval (input ("What is the Celsius temperature? ") ) 
    fahrenheit = 9/5 * celsius + 32 
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.") 

main () 

"""

import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

print(3 + 4)

print("The answer is", end= " ")
print(3 + 5)

"""

ans = eval(input("Enter an expression: "))
print(ans)

"""

# A simple program to average two exam scores 
# Illustrates use of multiple input 


"""
def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores separated by a comma:"))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)

main()

"""

for i in range(10):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

for odd in [1, 3, 5, 7, 9]:
    print(odd * odd)

for i in range(10):
    print(odd)

x = list(range(10))
print(x)

# A program to compute the value of an investment 
# carried 10 years into the future

"""

def main():
    print("This program calcalutes the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annual interst rate:"))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in 10 years is:", principal)

main()

"""

for i in range(5):
    print(i * i)

print("start")
for i in range(0):
    print("Hello")
print("end")

# A program that computes the real roots of a quadratic equation. 
# Illustrates use of the math library. 
# Note: This program crashes if the equation has no real roots.

"""

import math
def main():
    print("This program finds the real solution to aquadratic")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1,root2)

main()

"""
fact = 1
for factor in [6,5,4,3,2,1]:
    fact = fact * factor

"""
def main():
    n = int(input("Please enter a whole number"))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()   

"""

# Simple string processing program to generate usernames .

"""
def main():
    print("This program generates computer usernames. \n")

    first = input("Please enter your first name (all lowercase)")
    last  = input("Please enter your last name (all lowercase)")

    uname = first[0] + last[:7]

    print("Your username is:", uname)
 
main()

"""
# A program to print the month abbreviation, given its number .

"""
def main() : 

# months is a list used as a lookup table 
    
    months = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , 
    "Jul " , "Aug" , "Sep" , "Oct " , "Nov" , "Dec "] 
    n = int (input ( "Enter a month number ( 1-12) : ")) 
    print ( "The month abbreviation is" , months [n-1] + " . ") 

main()

"""

s = "hello, I came here for an argument " 
s.lower () 
print(s)

s1 = "hello, I came here for an argument " 
s1.center(50) 
print(s1)

s2 = "hello, I came here for an argument " 
s2.lower () 
print(s2)

s3 = "hello, I came here for an argument " 
s3.upper() 
print(s3)

squares = []
for x in range(1,101):
    squares.append(x*x)

print(squares)











