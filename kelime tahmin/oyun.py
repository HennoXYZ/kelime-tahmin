import random

class oyun:
    def __init__(self):
        self.kelimeturu = None
        self.kelime = None
        self.hak = 6
        self.tedkel = []
    
    def hangitur(self):
        self.kt = input("(spor, marka, oyun)\nKelimenin türü ne olsun:\n").lower()
        oyun.rndkelimesec(self)
            
    
    def rndkelimesec(self):
        if self.kt=="spor":
            kelimeler = ["futbol", "basketbol", "voleybol", "koşu", "yüzme"]
        elif self.kt=="marka":
            kelimeler = ["apple", "samsung", "nike", "adidas", "google"]
        elif self.kt=="oyun":
            kelimeler = ["minecraft", "fortnite", "leagueoflegends", "pubg", "amongus"]

        self.kelime = random.choice(kelimeler)
        oyun.oyunabasla(self)

    def oyunabasla(self):
        while True:
            kelalt = ''.join([harf if harf in self.tedkel else '_' for harf in self.kelime])
            print(f"\n {kelalt} \nLütfen bir harf yazınız: ")
            tahmin = input().lower()

            if len(tahmin):
                self.tedkel.append(tahmin)
                if tahmin in self.kelime:
                        print(f"\nbu kelimede bu harf var! {self.hak} hakkınız var!")
                else:
                    self.hak -= 1
                    print(f"\nbu harf bu kelimede yok! {self.hak} hakkınız kaldı!")
            else:
                    print("Lütfen sadece 1 tane harf yazınız!")

            kelalt = ''.join([harf if harf in self.tedkel else '_' for harf in self.kelime])

            if "_" not in kelalt:
                print(kelalt)
                print(f"Tebrikler kelimeyi buldun! {self.kelime}!")
                break
            if self.hak == 0:
                print(f"Malesef kelimeyi bulamadın kelimeniz {self.kelime}di")
                break

oyun1 = oyun()
oyun1.hangitur()


