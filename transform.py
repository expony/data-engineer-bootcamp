import json
# Bir önceki yazdığımız dosyadan veri çekme fonksiyonumuzu içeri alıyoruz
from extract import veri_cek

def veriyi_temizle(ham_veri):
    temizlenmis_kullanicilar = []
    
    # 'results' listesinin içindeki her bir kullanıcıyı tek tek geziyoruz
    for kullanici in ham_veri["results"]:
        
        # İç içe geçmiş JSON yapısından sadece istediklerimizi cımbızlıyoruz
        temiz_kullanici = {
            "Ad": kullanici["name"]["first"],
            "Soyad": kullanici["name"]["last"],
            "Email": kullanici["email"],
            "Ulke": kullanici["location"]["country"]
        }
        
        # Temizlediğimiz bu kullanıcıyı yeni listemize ekliyoruz
        temizlenmis_kullanicilar.append(temiz_kullanici)
        
    return temizlenmis_kullanicilar

if __name__ == "__main__":
    print("--- T AŞAMASI BAŞLIYOR ---")
    
    # 1. E aşaması: Veriyi çek
    gelen_veri = veri_cek()
    
    # 2. T aşaması: Veriyi temizle
    temiz_veri = veriyi_temizle(gelen_veri)
    
    print("\nİşte tertemiz verimiz:")
    print(json.dumps(temiz_veri, indent=4))