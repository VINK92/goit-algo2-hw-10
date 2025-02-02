import random
import time
import matplotlib.pyplot as plt
import numpy as np

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        times.append(time.time() - start_time)
    return np.mean(times)

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    rand_time = measure_time(randomized_quick_sort, arr)
    det_time = measure_time(deterministic_quick_sort, arr)
    randomized_times.append(rand_time)
    deterministic_times.append(det_time)
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

plt.figure(figsize=(10, 5))
plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", marker="o")
plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", marker="s")
plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання (с)")
plt.title("Порівняння часу виконання QuickSort")
plt.legend()
plt.grid()
plt.show()
