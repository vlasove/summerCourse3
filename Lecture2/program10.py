def Sqrt(a, acc = 0.000000000001):
    x = 1
    while True:
        if abs(x - 1/2*(x+a/x)) < acc:
            return x
        else:
            x = 1/2*(x+a/x)

def Factorial(n):
    if n <= 1:
        return 1
    else:
        return Factorial(n-1)*n

#0,1,1,2,3,5,8,13...
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Sqrt(25))
print(Factorial(3))
fib_enum = [Fibonacci(x) for x in range(10)]
print(fib_enum)
