import time

import main


def show(name):
    print(f"Hello {name}")


def greeting():
    print("How are you?")


if __name__ == '__main__':

    # main.every(6).seconds.do(show, name='rezoo')  # job1
    # main.every(4).seconds.do(greeting)  # job2
    main.every().hour.at(':14').do(show, name='rezoo')

    while True:
        main.run_pending()
        time.sleep(1)
