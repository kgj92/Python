import random

def generate_lotto():
    lotto = random.sample(range(1, 46), 6)
    return lotto

lotto_numbers = generate_lotto()
print("123456:", lotto_numbers)

