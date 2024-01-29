import kutuphane as kt
import random

tur = kt.hangitur().lower()
marka = ["mcdonalds", "burgerking", "popeyes"]
oyun = ["minecraft", "roblox", "fortnite"]
spor = ["basketbol", "futbol", "voleybol"]


if tur=="marka":
    kelime = kt.rndkelimesec(marka)
elif tur=="oyun":
    kelime = kt.rndkelimesec(oyun)
elif tur=="spor":
    kelime = kt.rndkelimesec(spor)

kt.oyunabasla(kelime)


