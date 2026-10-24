import requests
import json

def veri_cek():
    # 1. Veriyi çekeceğimiz adres (API Endpoint)
    url = "https://randomuser.me/api/?results=5"
    
    print("Veri çekiliyor...")
    
    # 2. Siteye gidip kapıyı çalıyoruz (GET isteği)
    cevap = requests.get(url)
    
    # 3. Gelen cevabı JSON formatına (Python sözlüğüne) çeviriyoruz
    veri = cevap.json()
    
    # 4. Ekrana düzenli görünmesi için yazdırıyoruz
    print(json.dumps(veri, indent=4))
    
    return veri

# Sadece bu dosya çalıştırıldığında aşağıdaki kodu işlet
if __name__ == "__main__":
    cekilen_veri = veri_cek()