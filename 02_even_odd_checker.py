"""Program 2: Conditionals - check whether a number is even or odd."""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

if number > 0:
    print("It is positive.")
elif number < 0:
    print("It is negative.")
else:
    print("It is zero.")
