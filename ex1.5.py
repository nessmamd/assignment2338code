import timeit
import time 
import matplotlib.pyplot as plt
dict_fun = {}

def func(n):
    if n == 0 or n == 1: 
        return n 
    else:
        return func(n-1) + func(n-2)

def funcnew(nz):
    if nz == 0 or nz == 1:
        return nz 
    else:
        if(nz in dict_fun):
            return dict_fun[nz]
        else:
            val = funcnew(nz-1) + funcnew(nz-2)
            dict_fun[nz] = val
            return val 

y_input = list(range(1,37))
y_input_two = list(range(1,37))
x_input_new = []
x_input_old = []

for x in y_input: 
    start = time.time()
    func(x)
    end = time.time()
    x_input_old.append(end-start)


for mo in y_input_two: 
    p = timeit.timeit(lambda : funcnew(mo))
    dict_fun.clear()
    x_input_new.append(p) 

print(x_input_new)
plt.plot(y_input, x_input_new, label = "modified function") 
plt.plot(y_input, x_input_old, label = "original function") 
plt.xlabel("value of n")
plt.ylabel("time taken ")
plt.legend()
plt.show()

    
