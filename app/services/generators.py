import random


def generate_random_string(length) -> str:
    nums = '0123456789'
    return ''.join(random.choice(nums) for _ in range(length))