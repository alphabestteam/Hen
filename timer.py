import time



def timer_decorator(func):
    st = time.time()
    def inner():
        for _ in range(10000000):
            pass
        et =time.time()
        print(et-st)
    return inner

@timer_decorator
def name():
    pass


def main():
    name()
if __name__ == "__main__":
    main()