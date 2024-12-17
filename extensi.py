import numpy as np
import matplotlib.pyplot as plt
import time

# Set seed for reproducibility
np.random.seed(37)

# Generate arrays with specified lengths and max value = 213
arr1 = np.random.randint(1, 214, size=100)
arr2 = np.random.randint(1, 214, size=150)
arr3 = np.random.randint(1, 214, size=200)
arr4 = np.random.randint(1, 214, size=250)
arr5 = np.random.randint(1, 214, size=300)
arr6 = np.random.randint(1, 214, size=350)
arr7 = np.random.randint(1, 214, size=400)
arr8 = np.random.randint(1, 214, size=500)

arrays = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8]

# Function to check if an array has unique elements
def is_unique(array):
    return len(array) == len(set(array))

# Function to measure worst case time
def measure_worst_case(array):
    start_time = time.perf_counter()
    is_unique(array)
    end_time = time.perf_counter()
    return end_time - start_time

# Function to measure average case time
def measure_average_case(array, trials=10):
    times = []
    for _ in range(trials):
        start_time = time.perf_counter()
        is_unique(array)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

# Measure times for each array
worst_cases = []
average_cases = []
unique_results = []

for array in arrays:
    worst_cases.append(measure_worst_case(array))
    average_cases.append(measure_average_case(array))
    unique_results.append(is_unique(array))

# Print execution times
print("Execution Times:")
for i, size in enumerate([len(arr) for arr in arrays]):
    print(f"Array Size: {size}")
    print(f"  Worst Case: {worst_cases[i] * 1e6:.2f} microseconds")
    print(f"  Average Case: {average_cases[i] * 1e6:.2f} microseconds")

# Print unique array sizes
print("\nUnique Arrays:")
unique_found = False
for i, size in enumerate([len(arr) for arr in arrays]):
    if unique_results[i]:
        print(f"Array of size {size} is unique.")
        unique_found = True
if not unique_found:
    print("No arrays are unique.")

# Function to plot results for all arrays in one graph
def plot_cases(array_sizes, worst_cases, average_cases):
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, [wc * 1e6 for wc in worst_cases], marker='o', color='red', label='Worst Case')
    plt.plot(array_sizes, [ac * 1e6 for ac in average_cases], marker='o', color='blue', label='Average Case')
    plt.title('Performance Comparison Across Array Sizes')
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (microseconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot results for all arrays
array_sizes = [len(arr) for arr in arrays]
plot_cases(array_sizes, worst_cases, average_cases)
