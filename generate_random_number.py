import random


def generate_random_number():
    numbers_range = "0123456789"
    current_number = []

    for _ in range(4):
        random_char = random.choice(numbers_range)
        current_number.append(random_char)
        numbers_range = numbers_range.replace(random_char, "")

    return current_number
