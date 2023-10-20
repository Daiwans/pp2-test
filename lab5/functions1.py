import random
import math

def convert_grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def solve_head_and_legs(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

def is_number_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime_numbers(numbers):
    return list(filter(lambda x: is_number_prime(x), numbers)

from itertools import permutations

def get_string_permutations(input_string):
    perms = [''.join(p) for p in permutations(input_string)]
    return perms

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def contains_double_three(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def find_spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def find_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def display_histogram(numbers):
    for num in numbers:
        print('*' * num)

def play_number_guessing_game():
    name = input("Your name: ")
    print(f"{name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses_taken += 1
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"{name}, you guessed my number in {guesses_taken} guesses!")
            break

if __name__ == "__main":
    print(convert_grams_to_ounces(100))
    print(convert_fahrenheit_to_celsius(68))
    print(solve_head_and_legs(35, 94))
    print(filter_prime_numbers([2, 3, 5, 7, 10, 11, 13, 15]))
    print(get_string_permutations("abc"))
    print(reverse_sentence("We are ready"))
    print(contains_double_three([1, 3, 3]))
    print(find_spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(calculate_sphere_volume(3))
    print(find_unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    display_histogram([4, 9, 7])
    play_number_guessing_game()
