import threading
import time


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_scitanie(num):
    sucet = 0
    for i in range(num):
        sucet = sucet + i
        print(f"Scitanie: {sucet}")    # A function that returns the third power of a number given as a parameter
    time.sleep(3)


def print_nasobenie(num):
    nasobenie = 0
    for i in range(num):
        nasobenie = i ** 2
        print(f"Nasobenie: {nasobenie}")
                                        # A function that returns the square of the number given as a parameter


if __name__ == "__main__":
    # creating threads
    t1 = ThreadWithReturnValue(target=print_nasobenie, args=(100,))
    t2 = threading.Thread(target=print_scitanie, args=(1000000,))

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    print(t1.join())
    t2.join()

    print("Done!")