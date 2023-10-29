def generate_squares(N):
    for i in range(N + 1):
        yield i * i

for x in generate_squares(5):
    print(x)

def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print("Even numbers up to", n, "are:", ", ".join(map(str, generate_even_numbers(n))))

def generate_divisible_numbers(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))
print("Numbers divisible by 3 and 4 up to", n, "are:")
for num in generate_divisible_numbers(n):
    print(num)

def generate_squares_in_range(a, b):
    for i in range(a, b + 1):
        yield i * i

for x in generate_squares_in_range(1, 5):
    print(x)

def countdown_from(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
print("Countdown from", n, "is:")
for num in countdown_from(n):
    print(num)
