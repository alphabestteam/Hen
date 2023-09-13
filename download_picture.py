import requests
import shutil
import threading
import time


def timer(func):
    def inner(*args, **kwads):
        start_time = time.time()
        func(*args, **kwads)
        end_time = time.time() - start_time
        print("the function ends in ", end_time)

    return inner


@timer
def download_url(url):
    response = requests.get(url)
    with open("img.png", "a") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


def main():
    # the 5 url in the quation the url not working so i put in the list just 4
    url_list = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
        "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
        "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
        "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
    ]
    start_time = time.time()
    for url in url_list:
        download_url(url)
    print("end of run without threads ", time.time() - start_time)

    print("threads")
    start_time = time.time()
    t1 = threading.Thread(target=download_url(url_list[0]))
    t2 = threading.Thread(target=download_url(url_list[1]))
    t3 = threading.Thread(target=download_url(url_list[2]))
    t4 = threading.Thread(target=download_url(url_list[3]))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("end of run without threads ", time.time() - start_time)


if __name__ == "__main__":
    main()
