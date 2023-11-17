#1
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
#2
def count_case(s):
    counts = {"upper": 0, "lower": 0}
    for char in s:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
    return counts["upper"], counts["lower"]
#3
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True
#4
def delayed_sqrt(number, delay_ms):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number")
    if delay_ms < 0:
        raise ValueError("Delay cannot be negative")
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)
#5
def all_true(t):
    for element in t:
        if not element:
            return False
    return True

