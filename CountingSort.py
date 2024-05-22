import random
import timeit

def counting_sort(arr):
    # Find the maximum element in the array
    max_val = max(arr)

    # Create a count array to store the count of each element
    count = [0] * (max_val + 1)

    # Count the occurrences of each element in the array
    for num in arr:
        count[num] += 1

    # Calculate the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create a sorted array to store the sorted elements
    sorted_arr = [0] * len(arr)

    # Place the elements in the sorted array based on their count
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr


# Test the counting sort algorithm

def benchmark(max_element, size):
    arr = [random.randint(1, max_element) for _ in range(size)]

    start_time = timeit.default_timer()
    counting_sort(arr)
    dur = (timeit.default_timer() - start_time) * 1000

    return dur

for i in range(1, 6):
    size = 10 ** i
    for j in range(1, 6):
        max_element = 10 ** j
        print(f"|{size}|{max_element}|{benchmark(max_element, size):.5f}|")