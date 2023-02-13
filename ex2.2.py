import sys
import threading
import requests
import time
import matplotlib.pyplot as plt

threading.stack_size(33554432)
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high



url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = requests.get(url)
data = response.json()
input_sizes = []
timing_results = []
for array in data:
    input_sizes.append(len(array))
    start_time = time.time()
    func1(array, 0, len(array)-1)
    end_time = time.time()
    timing_results.append(end_time - start_time)
plt.plot(input_sizes, timing_results)
plt.xlabel("Input size")
plt.ylabel("Time (s)")
plt.show()
