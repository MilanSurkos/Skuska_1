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
        # A function that returns the third power of a number given as a parameter
    return sucet

def print_nasobenie(num):
    nasobenie = 0
    for i in range(num):
        nasobenie = i ** 2
    return nasobenie
                                        # A function that returns the square of the number given as a parameter


if __name__ == "__main__":     #K čomu to je ? ..... sa vykona len ked pustam tento subor task 13 ...
                                                        # ked niekde ho importujem tak sa to nestpusti
    # creating threads
    t1 = ThreadWithReturnValue(target=print_nasobenie, args=(100,))
    t2 = ThreadWithReturnValue(target=print_scitanie, args=(1000000,))

    # starting threads
    t1.start()
    t2.start()

    # waiting until both threads have finished executing before executing further code
    print(f"Vysledok nasobenia: {t1.join()}")
    print(f"Vysledok scitania: {t2.join()}")

    print("Done!")