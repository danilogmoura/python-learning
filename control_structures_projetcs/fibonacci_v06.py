def fibonacci(quantity):
    result = [0, 1]
    for _ in range(quantity - 2):
        result.append(sum(result[-2:]))
    return result


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
