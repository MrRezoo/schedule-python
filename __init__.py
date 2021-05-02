import time

import main


def show(name):
    print(f"Hello {name}")


def greeting():
    print("How are you?")


if __name__ == '__main__':

    main.every().second.do(show, name='rezoo')  # job1
    main.every(4).second.do(greeting)  # job2

    while True:
        main.run_pending()
        time.sleep(1)
