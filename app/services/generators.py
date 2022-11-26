import random


def generate_random_string(length) -> str:
    nums = '0123456789'
    rand_string = ''.join(random.choice(nums) for i in range(length))
    return rand_string