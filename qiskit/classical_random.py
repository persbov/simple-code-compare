"""
Classical version of the same idea.

High-level algorithm:
1. Flip a fair coin many times
2. Count the number of 0s and 1s
"""

import random
from collections import Counter

# Number of coin flips (same as "shots" in the quantum version)
shots = 1024

results = []
for _ in range(shots):
    # Classic coin flip: 0 or 1 with equal probability
    bit = random.randint(0, 1)
    results.append(str(bit))

counts = Counter(results)
print("Classical random results:")
print(counts)
print(f"\nTotal shots: {shots}")
