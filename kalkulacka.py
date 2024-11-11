try:
    prve_cislo = int(input("vloz prve cislo: "))
except(ValueError):
    print("vlozil jsi chybnu hodnotu, bude pouzite '1'")
    prve_cislo = 1


znamienko = input("vloz znak pozadovanej matematickej operacie (+, -, *, /): ")
if znamienko not in ["+", "-", "*", "/"]:
    raise ValueError("zvolil jsi chybnu matematicku operaciu a program bude ukoncen")

try:
    druhe_cislo = int(input("vloz druhe cislo: "))
except(ValueError):
    print("vlozil jsi chybnu hodnotu, bude pouzite '1'")
    druhe_cislo = 1

if znamienko == "+":
    print(f"Sucet cisiel {prve_cislo} a {druhe_cislo} je {prve_cislo + druhe_cislo}")
elif znamienko == "-":
    print(f"Rozdiel cisiel {prve_cislo} a {druhe_cislo} je {prve_cislo - druhe_cislo}")
elif znamienko == "*":
    print(f"Krat cisiel {prve_cislo} a {druhe_cislo} je {prve_cislo * druhe_cislo}")
elif znamienko == "/":
    try:
        print(f"podiel cisiel {prve_cislo} a {druhe_cislo} je {prve_cislo / druhe_cislo}")
    except (ZeroDivisionError):
        print("nula sa neda delit")
else:
    print(f"Zla operacia program bude ukonceny")