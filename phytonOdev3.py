class Personel:
    def __init__(self, ad, departman, calisma_yili, maas, personel_id):
        self.ad = ad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas
        self.personel_id = personel_id

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(f"Ad: {personel.ad}, Departman: {personel.departman}, Çalışma Yılı: {personel.calisma_yili}, Maaş: {personel.maas}, Personel ID: {personel.personel_id}")

    def maas_zammi(self, personel, zam_orani):
        personel.maas *= (1 + zam_orani/100)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)

def menu():
    firma = Firma()
    while True:
        print("1- Personel Ekle")
        print("2- Personel Listele")
        print("3- Maaş Zamı")
        print("4- Personel Çıkart")
        print("5- Çıkış")
        secim = input("Seçiminizi yapınız: ")
        if secim == "1":
            ad = input("Ad: ")
            departman = input("Departman: ")
            calisma_yili = int(input("Çalışma Yılı: "))
            maas = float(input("Maaş: "))
            personel_id = input("Personel ID: ")
            personel = Personel(ad, departman, calisma_yili, maas, personel_id)
            firma.personel_ekle(personel)
        elif secim == "2":
            firma.personel_listele()
        elif secim == "3":
            personel_id = input("Zam yapılacak personelin ID'si: ")
            zam_orani = float(input("Zam oranı: "))
            for personel in firma.personel_listesi:
                if personel.personel_id == personel_id:
                    firma.maas_zammi(personel, zam_orani)
                    print("Maaş zamı yapıldı.")
                    break
            else:
                print("Personel bulunamadı.")
        elif secim == "4":
            personel_id = input("Çıkarılacak personelin ID'si: ")
            for personel in firma.personel_listesi:
                if personel.personel_id == personel_id:
                    firma.personel_cikart(personel)
                    print("Personel çıkarıldı.")
                    break
            else:
                print("Personel bulunamadı.")
        elif secim == "5":
            break
        else:
            print("Geçersiz seçim.")

menu()
