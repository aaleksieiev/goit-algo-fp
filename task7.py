import random
import matplotlib.pyplot as plt
import pandas as pd

# Number of simulations (dice throws)
num_throws = 1000000

# Simulate dice throws and count the sums
sums = [0] * 13  # Index from 0 to 12, but we'll use 2 to 12

for _ in range(num_throws):
    diсe1 = random.randint(1, 6)
    diсe2 = random.randint(1, 6)
    dice_sum = diсe1 + diсe2
    sums[dice_sum] += 1

# Calculate probabilities
probabilities = [s / num_throws for s in sums]

# Theoretical probabilities (known for two dice)
theoretical_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Create a DataFrame for better visualization
data = {
    'Sum': list(range(2, 13)),
    'Simulated Probability': [probabilities[i] for i in range(2, 13)],
    'Theoretical Probability': [theoretical_probs[i] for i in range(2, 13)]
}
df = pd.DataFrame(data)

# Display the results in a table
print(df)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(df['Sum'], df['Simulated Probability'], marker='o', linestyle='-', label='Simulated Probability')
plt.plot(df['Sum'], df['Theoretical Probability'], marker='x', linestyle='--', label='Theoretical Probability')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Simulated vs Theoretical Probabilities of Dice Sums')
plt.legend()
plt.xticks(df['Sum'])  # Show all possible sums on the x-axis
plt.grid(True)
plt.show()