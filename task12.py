#Task12 - Vytvoříte generátor, který bude postupně vracet
# Albert - máme koncovku "bert".
# před tu koncovku budou dávány předpony "Al", "Ro", "Hu", "Nor", "Gil"

def GeneratorJmen(pred, konc):
    for cele_jmeno in pred:
        yield cele_jmeno + konc

predpony = ["Mi", "Ro", "Hu", "Snor", "Si"]
koncovka = "lan"
for jmeno in GeneratorJmen(predpony, koncovka):
    print(f"Tvé jméno je {jmeno}") # Albert, Robert, Hubert, Norbert, Gilbert






