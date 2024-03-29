def frekans_analizi(metin):

    frekanslar = {}
    toplam_karakter_sayisi = 0

    for karakter in metin:  

        if karakter.isalnum():  

            karakter = karakter.lower()  
            frekanslar[karakter] = frekanslar.get(karakter, 0) + 1
            toplam_karakter_sayisi += 1

    return frekanslar, toplam_karakter_sayisi

def main():
    
    metin = input("Lütfen metni girin: ")
    karakter_frekanslari, toplam_karakter_sayisi = frekans_analizi(metin)
    
    print("Karakter Frekansları:")
    for karakter, frekans in sorted(karakter_frekanslari.items()):
        yuzde = (frekans / toplam_karakter_sayisi) * 100
        print(f"{karakter}: {frekans} kez, yüzdesi: %{yuzde:.2f}")

if __name__ == "__main__":
    main()
