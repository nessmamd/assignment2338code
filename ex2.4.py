

import requests
import time
import matplotlib.pyplot as plt


def func2(array, start, end):
    count1 = start-1
    pivot = array[(start+end)//2]
    count2 = end+1
    while (1):
        count1+=1
        while (array[count1] < pivot):
            count1+=1
        count2-=1
        while (array[count2]> pivot):
            count2-=1
        if count1>=count2:
            return count2
        array[count1], array[count2] = array[count2], array[count1]

def func1(array, start, end):
    if start < end:
        p = func2(array, start, end)
        func1(array, start, p)
        func1(array, p+1, end)

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
