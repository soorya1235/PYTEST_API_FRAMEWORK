def fibo_gen(max=10):
    a, b = 0, 1
    counter = 0
    while counter < max:
        a, b = b, a + b
        yield a


fib = fibo_gen(20)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
