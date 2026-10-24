import schedule
import time
from extract import veri_cek
from transform import veriyi_temizle
from load_db import veritabanina_kaydet
from load_datalake import datalake_yukle

def tam_boru_hatti():
    print("\n--- GELİŞMİŞ VERİ BORU HATTI TETİKLENDİ ---")
    
    # 1. EXTRACT: Veriyi kaynaktan çek
    ham_veri = veri_cek()
    
    # 2. LOAD (Data Lake): Orijinal veriyi güvene al
    datalake_yukle(ham_veri)
    
    # 3. TRANSFORM: İhtiyacımız olanları cımbızla
    temiz_veri = veriyi_temizle(ham_veri)
    
    # 4. LOAD (Data Warehouse/DB): Analiz için temiz veriyi tabloya yaz
    veritabanina_kaydet(temiz_veri)

# Test için 10 saniyede bir çalıştırıyoruz
schedule.every(10).seconds.do(tam_boru_hatti)

print("Sistem dinlemede... (Durdurmak için Ctrl+C)")

while True:
    schedule.run_pending()
    time.sleep(1)