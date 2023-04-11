generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # output 0
print(next(generator))  # output 4
print(next(generator))  # output 16
print(next(generator))  # output 36
print(next(generator))  # output 64
# print(next(generator))  # output Erro!
