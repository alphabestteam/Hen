def main():
    try:
        x = int(input("enter number"))
        print(x)
    except:
        print()
    try:
        y = int(input("enter number"))
        print(y)
    except ValueError:
        print()
    
    print("finish runnig")


if __name__ == "__main__":
    main()