import timeit
import matplotlib.pyplot as plt
dict_fun = {}

def func(n):
    if n == 0 or n == 1: 
        return n 
    else:
        return func(n-1) + func(n-2)

def funcnew(n):
    if n == 0 or n == 1:
        return n 
    else:
        if(n in dict_fun):
            return dict_fun[n]
        else:
            val = funcnew(n-1) + funcnew(n-2)
            dict_fun[n] = val
            return val

c = range(0,36)
elasped_time = 0 
elasped_time_new = 0
y_input = []
x_input_new = []
x_input_old = []

for x in c: 
    y_input.append(x)
    m = timeit.timeit(lambda : func(x))
    x_input_old.append(m)

for mo in c: 
    p = timeit.timeit(lambda : funcnew(x))
    dict_fun.clear()
    x_input_new.append(p)

plt.plot(x_input_new, y_input, label = "modified function") 
plt.plot(x_input_old, y_input, label = "original function")
plt.xlabel("Time taken")
plt.ylabel("value of n ")
plt.legend()
plt.show()
