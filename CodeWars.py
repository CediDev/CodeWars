import time as t



def timetest(func):
    def wrapper(*args):
        t1 = t.time()
        func(*args)
        print(t.time()-t1)
    return wrapper





@timetest
def comp2(array1, array2):
    if (array1 is None or array2 is None) or len(array1) is not len(array2):
        return False
    for i in array1:
        if i**2 not in array2:
            return False
        array2.remove(i**2)
    return True
    




def Fib(n):
    num = [0, 1]
    for FibNum in range(-1,n):
        num.append(num[FibNum] + num[FibNum+1])
        print("dipa")
    print(num[-3])

@timetest
def productFib(prod):
    print(prod)
    if prod == 0:
        return [0, 1, True]
    n=3
    while (Fib(n) * (Fib(n-1))) != int(prod):
        print(Fib(n) * (Fib(n-1)))
        n += 1
        if (Fib(n) * (Fib(n-1))) > prod:
            return [Fib(n-1), Fib(n), False]
    return [Fib(n-1), Fib(n), True]
