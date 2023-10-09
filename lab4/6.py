lines = int(input())
words = set()
for _ in range(lines):
    line = input().split()
    words.update(line)
print(len(words))