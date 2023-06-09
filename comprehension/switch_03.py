def get_kind_of_day(day):
    days = {
        (1, 7): "Weekend",
        tuple(range(2, 7)): "Weekday",
    }

    chosen_day = (kind for numbers, kind in days.items() if day in numbers)
    return next(chosen_day, "** invalid day **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia}: {get_kind_of_day(dia)}")
