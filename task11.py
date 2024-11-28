#Task 11 - udělat iterátor, kterému řekneme kolik chceme čísel, např. 5.
#Iterátor bude postupně vracet mocniny těchto čísel. Tzn pro číslo 5, iterátor vrátí 1, 4, 9, 16, 25


class IteratorMocnin():
    def __init__(self, n):
        self.n = n
        self.numbers = 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers > self.n:
            raise StopIteration
        vysledok = self.numbers ** 2
        self.numbers += 1
        return vysledok



mocniny = IteratorMocnin(5)
for mocnina in mocniny:
    print(mocnina)
