# [expression for item in list if conditional]
double_of_even = [i * 2 for i in range(10) if i % 2 == 0]
print(double_of_even)


# normal version
double_of_even = []
for i in range(10):
    if i % 2 == 0:
        double_of_even.append(i * 2)
print(double_of_even)
