import time
from DataProcessing import test2


def run():
    test1 = 1
    test23 = 2
    while True:
        try:
            a = test2.Write_file("1", 2)
            a.run_script()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    run()
