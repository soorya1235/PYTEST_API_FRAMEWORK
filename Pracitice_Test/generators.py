def pow_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


abcd = pow_gen(10)
print(next(abcd))
print(next(abcd))
print(next(abcd))
