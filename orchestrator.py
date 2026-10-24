import schedule
import time
from extract import veri_cek
from transform import veriyi_temizle
from load_db import veritabanina_kaydet

def etl_job():
    print("\n--- OTOMATİK ETL TETİKLENDİ ---")
    # E, T ve L aşamalarını sırayla çağırıyoruz
    ham_veri = veri_cek()
    temiz_veri = veriyi_temizle(ham_veri)
    veritabanina_kaydet(temiz_veri)

# Test amaçlı görevi her 10 saniyede bir çalışacak şekilde kuruyoruz.
# Gerçek bir senaryoda bu: schedule.every().day.at("03:00").do(etl_job) olurdu.
schedule.every(10).seconds.do(etl_job)

print("Orkestratör devrede. Görev bekleniyor... (Durdurmak için: Ctrl+C)")

# Sonsuz döngü ile programı ayakta tutuyoruz
while True:
    schedule.run_pending()
    time.sleep(1)