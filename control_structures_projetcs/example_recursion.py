def printer(max, current):
    # condition to stop the recursion
    if current < max:
        print(current)
        printer(max, current + 1)


if __name__ == "__main__":
    printer(10, 1)
