import random

throw_dice = 1

while throw_dice <= 100:
    number = random.randint(1,6)
    print(f"{throw_dice}'s throw = {number}")
    throw_dice += 1