# Extracts digits from an integer in reverse order and returns them as a string.

def extract_digits_reversed(number):
    digits = []
    while number > 0:
     digit = number % 10
     digits.append(digit)
     number //= 10
    return digits

number = 7536
digits = extract_digits_reversed(number)
print(digits) 