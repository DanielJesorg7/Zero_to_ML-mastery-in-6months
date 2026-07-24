import random

for i in range(3):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    is_lucky_7 = (total == 7)
    is_snake_eyes = (die1 == 1 and die2 == 1)
    
    print(f"Die 1: {die1}, Die 2: {die2}, Total = {total}, Lucky 7: {is_lucky_7}, Snake eyes: {is_snake_eyes}")
