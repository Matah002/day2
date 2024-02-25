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

'a' + 'x' if '123'.isdigit() else 'y' + 'b'

















