class pow:

    def __init__(self, max=20):
        self.max = 20
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        else:
            result = 2 ** self.n
            self.n += 1
            return result


abcd = pow(10)
print(abcd)
print(type(abcd))

print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
