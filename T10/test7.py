import random
import time
from memory_profiler import profile

@profile
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr_size = 10000000
    arr = sorted([random.randint(1, arr_size) for _ in range(arr_size)])  # Сгенерирован отсортированный массив
    target = arr[-1]  # Поиск последнего элемента

    start_time = time.time()
    binary_search(arr, target)
    end_time = time.time()
    print(f"Время выполнения бинарного поиска: {end_time - start_time:.4f} секунд")
