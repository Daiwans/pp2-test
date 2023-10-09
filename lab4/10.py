n, k = [int(x) for x in input().split()]
strike = [0] * (n + 1)
for _ in range(k):
    a, b = [int(x) for x in input().split()]
    for day in range(a, n + 1, b):
        if day % 7 != 6 and day % 7 != 0:
            strike[day] = 1
total = sum(strike)
print(total)