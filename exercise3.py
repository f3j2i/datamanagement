import random

def toss_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

print("Tossing a coin...")
results = [toss_coin() for _ in range(3)]

for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")

print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
    print("You won!")
else:
    print("You lost!")