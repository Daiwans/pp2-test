numbers = input().split()
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        seen.add(num)
        print("NO")