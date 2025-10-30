import random
# Initialize counters
heads = 0
tails = 0
print("Flipping a coin 20 times...")
# Loop 20 times
for _ in range(20):
    # 0 = Heads, 1 = Tails
    flip = random.randint(0, 1)
    if flip == 0:
        print("H", end=" ")
        heads += 1
    else:
        print("T", end=" ")
        tails += 1
# Print a newline to separate from the H/T results
print() 
# Print the final counts
print(f"Heads: {heads}")
print(f"Tails: {tails}")