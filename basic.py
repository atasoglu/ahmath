"""
basic.py
"""
pi = 3.141592653589793
e = 2.718281828459045

# simple operations

def sum(*args):    
    if len(args) == 1:
        res = 0
        for i in args[0]: res += i
        return res
    elif len(args) > 1:
        return sum(args)
    else:
        return None
    
def fact(x):
    if x > 1:
        return x * fact(x-1)
    else:
        return 1
    
def power(x, n):
    if n > 0:
        return x * power(x, n-1)
    else:
        return 1
    
def deg_to_rad(degree):
    # from degree to radian
    if type(degree) is int or type(degree) is float:
        return (pi / 180) * degree
    elif type(degree) is list:
        return [deg_to_rad(deg) for deg in degree]
    else:
        return None

def rad_to_deg(radian):
    # from radian to degree
    if type(rad) is int or type(rad) is float:
        return (180 / pi) * radian
    elif type(radian) is list:
        return [rad_to_deg(rad) for rad in radian]
    else:
        return None
    
# creating vectors

def arange(start, end, step):
    if end > start:
        res = [start]
        while (start + step) < end:
            res.append(start + step)
            start += step
        return res
    else:
        return None
    
def arangef(start, end, step, fpoint = 2): # f for floating points
    if end > start:
        res = [start]
        next_value = round(start + step, 2)
        while next_value < end:
            res.append(next_value)
            start += step
            next_value = round(start + step, 2)
        return res
    else:
        return None

# diff. and integral tools

def intg():
    pass

def diff(x):
    return [x[i] - x[i-1] for i in range(1, len(x))]

def dy(y, h):
    dy = diff(y)
    return [y/h for y in dy]

def dydx(y, x):
    dy, dx = [], x[:-1]
    for i, j in zip(diff(y), diff(x)):
        dy.append(i/j)
        
    return dy, dx