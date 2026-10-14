"""Program 5: Lists - store and process collections of values."""

marks = [78, 92, 65, 88, 54]

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks), "| Lowest:", min(marks))

marks.append(95)          # add an item
marks.remove(54)          # remove an item
marks.sort(reverse=True)  # sort high to low
print("Updated and sorted:", marks)

passed = [m for m in marks if m >= 60]
print("Passing marks:", passed)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit.title()}")
