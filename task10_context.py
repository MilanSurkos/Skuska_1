import time

class TimeMeasurment:
    def __enter__(self):
        print(f"Spúštam výpočet")
        self.start_time = time.time()  # zaznam zaciatku casu
        return self

    def __exit__(self, a, b, c):
        self.end_time = time.time()  # Zaznam konca casu
        self.duration = self.end_time - self.start_time  # vypocet trvania
        print(f"Blok trval {self.duration:.3f} sekund.")  # Print trvani v sekundach


with TimeMeasurment() as t:
    cislo = 1
    for i in range(100000000):
        cislo += i
    print(cislo)
