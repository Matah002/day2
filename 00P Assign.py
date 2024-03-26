class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_Person_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        
print("These are my details:")
print()
Person1 = Person("James", "19", "Male")
Person1.display_Person_details()


