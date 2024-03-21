import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generate random data for testing
data_sets = {
    "Small": [random.randint(0, 1000) for _ in range(200)],
    "Medium": [random.randint(0, 1000) for _ in range(2000)],
    "Large": [random.randint(0, 1000) for _ in range(20000)]
}

# Perform sorting and measure time
for name, data in data_sets.items():
    print(f"Data Set: {name}")
    
    # Merge Sort
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Час сортування злиттям: {merge_sort_time:.6f} сек.")
    
    # Insertion Sort
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Час сортування за допомогою Insertion Sort: {insertion_sort_time:.6f} сек.")
    
    # Timsort (Python built-in)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    print(f"Час сортування за допомогою Timsort : {timsort_time:.6f} сек.")
    
    print()