from people import People
def main():
    names = People()
    names.add_person("hen")
    names.add_person("yair")
    names.add_person("roz")
    names.add_person("dan")
    iter_names = iter(names)
    
    print(next(iter_names))
    print(next(iter_names))
    print(next(iter_names))
    print(next(iter_names))
    print(next(iter_names))
    print(next(iter_names))
if __name__ == "__main__":
    main()