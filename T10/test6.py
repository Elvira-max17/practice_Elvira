import random
import time
from memory_profiler import profile

@profile
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr_size = 10000000
    arr = sorted([random.randint(1, arr_size) for _ in range(arr_size)])  # Сгенерирован отсортированный массив
    target = arr[-1]  # Поиск последнего элемента

    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    print(f"Время выполнения линейного поиска: {end_time - start_time:.4f} секунд")
