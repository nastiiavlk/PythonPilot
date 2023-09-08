import random

# Create a list of 100 random numbers from 0 to 1000.
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# Bubble sort 
n = len(random_numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if random_numbers[j] > random_numbers[j+1]:
            random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j]

# Calculate averages using list comprehensions
even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

# Print results
print("AVG Even:", even_avg)
print("AVG Odd:", odd_avg)