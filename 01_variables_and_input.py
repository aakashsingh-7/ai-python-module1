"""Program 1: Variables, data types, and input/output."""

name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("Your height in metres (e.g. 1.70): "))
is_student = True

print(f"\nHello, {name}!")
print(f"Next year you will be {age + 1}.")
print(f"Height: {height} m | Student: {is_student}")
print("Types ->", type(name), type(age), type(height), type(is_student))
