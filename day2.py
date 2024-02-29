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

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price













