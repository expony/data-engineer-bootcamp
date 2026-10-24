import csv
from extract import veri_cek
from transform import veriyi_temizle

def veriyi_csv_kaydet(temiz_veri, dosya_adi="kullanicilar.csv"):
    # CSV dosyasının başlıkları (sütun isimleri)
    basliklar = ["Ad", "Soyad", "Email", "Ulke"]
    
    # Dosyayı yazma ('w') modunda açıyoruz
    with open(dosya_adi, mode='w', newline='', encoding='utf-8') as dosya:
        yazici = csv.DictWriter(dosya, fieldnames=basliklar)
        
        # Önce en üste başlıkları yazıyoruz
        yazici.writeheader()
        
        # Sonra temizlediğimiz her bir kullanıcıyı satır satır dosyaya yazıyoruz
        for kisi in temiz_veri:
            yazici.writerow(kisi)
            
    print(f"\nBaşarılı! Veriler {dosya_adi} dosyasına kaydedildi.")

if __name__ == "__main__":
    print("--- ETL BORU HATTI BAŞLIYOR ---")
    
    # 1. E (Extract) - Veriyi internetten çek
    ham_veri = veri_cek()
    
    # 2. T (Transform) - İhtiyacımız olmayan kısımları at, temizle
    temiz_veri = veriyi_temizle(ham_veri)
    
    # 3. L (Load) - Temizlenmiş veriyi CSV dosyasına yaz
    veriyi_csv_kaydet(temiz_veri)
    
    print("ETL İşlemi Tamamlandı!")