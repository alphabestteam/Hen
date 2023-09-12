from person import person


def main():
    number_of_people = int(input("enter the number of people you want "))

    list_of_people = [person() for _ in range(number_of_people)]
    bigger_than_18 = [p for p in list_of_people if p.print_age() >= 18]
    for p in bigger_than_18:
        print(p)


if __name__ == "__main__":
    main()