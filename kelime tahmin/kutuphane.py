import random

def hangitur():
    ui = input("Kelimeniz hangi tür olsun? (marka,spor,oyun):\n")
    if ui == "marka":
        return "marka"
    elif ui == "spor":
        return "spor"
    elif ui == "oyun":
        return "oyun"
    
def rndkelimesec(klm):
    return random.choice(klm)

def oyunabasla(kelime):
    hak = 6
    uzunluk = len(kelime)
    tedkel = []
    kelalt = ''.join([harf if harf in tedkel else '_' for harf in kelime])
    while True:
        kelalt = ''.join([harf if harf in tedkel else '_' for harf in kelime])
        print(f"\n {kelalt} \nLütfen bir harf yazınız: ")
        tahmin = input().lower()
        if len(tahmin)==1:
            tedkel.append(tahmin)
            if tahmin in kelime:
                print(f"\nbu kelimede bu harf var! {hak} hakkınız var!")
            else:
                hak -= 1
                print(f"\nbu harf bu kelimede yok! {hak} hakkınız kaldı!")
        else:
            print("Lütfen sadece 1 tane harf yazınız!")
        kelalt = ''.join([harf if harf in tedkel else '_' for harf in kelime])
        if "_" not in kelalt:
            print(kelalt)
            print(f"Tebrikler kelimeyi buldun! {kelime}!")
            break
        if hak == 0:
            print(f"Malesef kelimeyi bulamadın kelimeniz {kelime}di")
            break
    
            
