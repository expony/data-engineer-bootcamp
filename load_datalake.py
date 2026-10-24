import boto3
import json
from datetime import datetime
from extract import veri_cek

def datalake_yukle(ham_veri):
    # 1. S3 protokolüyle rustfs sunucumuza bağlanıyoruz
    s3_istemci = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='rustfsadmin',
        aws_secret_access_key='password123',
        region_name='us-east-1' # S3 standardı gereği formalite
    )
    
    # 2. Üzerine yazmaması için dosya adına güncel zamanı ekliyoruz
    zaman_damgasi = datetime.now().strftime("%Y%m%d_%H%M%S")
    dosya_adi = f"kullanicilar_ham_{zaman_damgasi}.json"
    
    # 3. Python verisini JSON formatına dönüştürüp kovaya yüklüyoruz
    s3_istemci.put_object(
        Bucket='raw-data',
        Key=dosya_adi,
        Body=json.dumps(ham_veri)
    )
    
    print(f"\nBaşarılı! Ham veri {dosya_adi} adıyla göle atıldı.")

if __name__ == "__main__":
    print("--- DATA LAKE YÜKLEME TESTİ ---")
    gelen_veri = veri_cek()
    datalake_yukle(gelen_veri)