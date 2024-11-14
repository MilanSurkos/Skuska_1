def with_password(func):
    password = "cerdo"

    def nova_funkcia(a,b):

        if input("zadaj heslo: ") == password:
            print("Zadal si spravne heslo")
            return func(a,b)
        else:
            return"Zadal si nespravne heslo"
    return nova_funkcia


@with_password
def sucet(a,b):
    return a+b

@with_password
def rozdiel(a,b):
    return a-b

print(sucet(7,9))
print(rozdiel(8,4))
