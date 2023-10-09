n = int(input())
possible_numbers = set(range(1, n + 1))
while True:
    try:
        line = input().split()
        if line[0] == "HELP":
            break
        question_set = set(map(int, line))
        answer = input()
        if answer == "NO":
            possible_numbers -= question_set
        elif answer == "YES":
            possible_numbers &= question_set
    except error:
        break
result = sorted(possible_numbers)
print(*result)