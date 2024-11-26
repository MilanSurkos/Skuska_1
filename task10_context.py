import time

class TimeMeasurment:
    def __enter__(self):
        self.start_time = time.time()  # zaznam zaciatku casu
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  # Zaznam konca casu
        self.duration = self.end_time - self.start_time  # vypocet trvania
        print(f"Blok trval {self.duration:.2f} sekund.")  # Print trvani v sekundach


with TimeMeasurment() as t:
    cislo = 1
    for i in range(100000000):
        cislo += i
    print(cislo)
