def fibunachi():
    num1=0
    num2=1
    while True:
        yield num1
        num3 = num1
        num1 = num2
        num2 = num3 + num2
def main():
    number = fibunachi()
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
if __name__ == "__main__":
    main()