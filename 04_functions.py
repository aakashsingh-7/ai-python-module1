"""Program 4: Functions - reusable blocks of code."""


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def square(x):
    return x * x


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(greet("Asha"))
print(greet("Ravi", "Good morning"))
print("Square of 7:", square(7))
print("Primes up to 30:", [n for n in range(31) if is_prime(n)])
print("5! =", factorial(5))
