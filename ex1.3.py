dict_fun = {}

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
