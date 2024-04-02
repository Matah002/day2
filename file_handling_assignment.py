f = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\day1\\my_file.txt", "r")
print(f.read())

with open("C:\\Users\\ASUS\\OneDrive\\Desktop\\day1\\my_file.txt", "r+")as file:
    contents = file.read()
    file.write("I am 19 years old.")





