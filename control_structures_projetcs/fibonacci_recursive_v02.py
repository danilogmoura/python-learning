def fibonacci(quantity, sequence=(0, 1)):
    # Condition of stop
    return sequence if len(sequence) == quantity else \
        fibonacci(quantity, sequence + (sum(sequence[-2:]),))


if __name__ == "__main__":
    # List of the first 20 fibonacci numbers
    for fib in fibonacci(20):
        print(fib)
