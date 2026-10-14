"""Program 3: Loops - print a multiplication table."""

n = int(input("Print the table of which number? "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# while loop example: countdown
count = 5
print("\nCountdown:")
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
