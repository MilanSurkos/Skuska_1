def with_password(func):
    password = "cerdo"

    def nova_funkcia():

        if input("zadaj heslo: ") == password:
            print("Zadal si spravne heslo")
        else:
            print("Zadal si nespravne heslo")
    return nova_funkcia()


@with_password
def sucet(a,b):
    return a+b

print(sucet(5, 6))
