import psycopg2
from extract import veri_cek
from transform import veriyi_temizle

def veritabanina_kaydet(temiz_veri):
    # 1. Veri tabanına bağlanıyoruz (Docker'da belirlediğimiz kimlik bilgileriyle)
    baglanti = psycopg2.connect(
        host="localhost",
        dbname="bootcamp_db",
        user="admin",
        password="admin",
        port=5432
    )
    
    # 2. İmleç (cursor) oluşturuyoruz. Bu, SQL komutlarımızı veri tabanına taşıyan kuryemizdir.
    imlec = baglanti.cursor()

    # 3. Tablo oluşturma (Eğer 'kullanicilar' adında bir tablo yoksa sıfırdan oluşturur)
    tablo_sorgusu = """
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id SERIAL PRIMARY KEY,
        ad VARCHAR(100),
        soyad VARCHAR(100),
        email VARCHAR(150),
        ulke VARCHAR(100)
    );
    """
    imlec.execute(tablo_sorgusu)

    # 4. Verileri tabloya tek tek ekleme (SQL Injection saldırılarından korunmak için %s yapısını kullanırız)
    ekleme_sorgusu = "INSERT INTO kullanicilar (ad, soyad, email, ulke) VALUES (%s, %s, %s, %s);"
    
    for kisi in temiz_veri:
        imlec.execute(ekleme_sorgusu, (kisi["Ad"], kisi["Soyad"], kisi["Email"], kisi["Ulke"]))

    # 5. Yapılan değişiklikleri veri tabanına kalıcı olarak kaydet (commit) ve kuryeyi/bağlantıyı kapat
    baglanti.commit()
    imlec.close()
    baglanti.close()
    
    print("\nBaşarılı! Veriler PostgreSQL veri tabanına yazıldı.")

if __name__ == "__main__":
    print("--- POSTGRESQL ETL BORU HATTI BAŞLIYOR ---")
    ham_veri = veri_cek()
    temiz_veri = veriyi_temizle(ham_veri)
    veritabanina_kaydet(temiz_veri)