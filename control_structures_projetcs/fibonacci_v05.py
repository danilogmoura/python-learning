def fibonacci(quantity):
    result = [0, 1]

    while True:
        result.append(sum(result[-2:]))

        if len(result) == quantity:
            break

    return result


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
