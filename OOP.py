"""

class Person:
    # class attribute
    name = "Skinny"
    age = 75
    nationality = "Kenya"

# print(Person.name)

# using an instance variable

details = Person()
print(details.name)
print(details.age)
print(details.nationality)

"""

"""
class Person:
    # class attribute
    name = "Skinny"
    age = 75
    nationality = "Kenya"

    #constructor concept
    def __init__(self):
        print("This is a constructor")

details = Person()
print(details.name)
print(details.age)
print(details.nationality)

"""
class Person:

    def full_details(mypar):
        return f"Name: {mypar.name} Age: {mypar.age} Nationality: {mypar.nationality}"

details = Person("Skiny", 75, "SA")
print(details.full_details())



