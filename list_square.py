def main():
    num = int(input("enter number"))
    squared = [x**2 for x in range(num)]
    print(squared)

if __name__ == "__main__":
    main()