 n = int(input())
 possible_numbers = set(range(1, n + 1))
 while True:
     question = input().split()
     if question[0] == 'HELP':
         break
     question_numbers = set(map(int, question))
     intersection = possible_numbers.intersection(question_numbers)
     if len(intersection) * 2 == len(possible_numbers):
         answer = 'NO'
     else:
         answer = 'YES'
         possible_numbers.intersection_update(question_numbers)

     print(answer)
 print(*sorted(possible_numbers))
