import re, requests

link = "https://auto.bazos.sk/"
hlavna_stranka = requests.get(link)
vyraz = r"/inzerat[A-z0-9/-]*"
odkazy = re.findall(vyraz, hlavna_stranka.text)
for odkaz in odkazy:
    print(link + odkaz)
    stranka = requests.get(link + odkaz)
    skratky = re.findall(r"\d{1,6}\s?km", stranka.text)
    for skratka in skratky:
        print(skratka)