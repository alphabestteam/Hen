def total_age(**kwargs):
    print(kwargs)
    sum = 0
    for key in kwargs:
        sum += kwargs[key]
    print(sum)

def words_length(*args):
    sum = 0
    for length_of_word in args:
        sum+= len(length_of_word)
    print(sum)
def main():
    words_length("hen","yair","rozolio")
    total_age(age1 = 5,age2 = 6)
if __name__ == "__main__":
    main()