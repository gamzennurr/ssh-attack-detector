import time
from collections import defaultdict

ESIK = 5
ZAMAN_PENCERESI = 300

ip_zamanlari = defaultdict(list)
uyarilmis_ipler = set()

try:  #Hataları yakalama döngüsü
    dosya = open("loglar.txt", "r")
    dosya.seek(0, 2)
    
    print("📡 Canlı izleme başladı...")
    
    while True:
        satir = dosya.readline()
        
        if not satir:
            time.sleep(1)
            continue
        
        if "Failed password" in satir:
            try:  #IP çıkarma hatalarını yakala
                ip = satir.split("from")[1].split()[0]
                su_an = time.time() #şuanki zamanı saniye cinsinden alır
                
                ip_zamanlari[ip].append(su_an)
                
                ip_zamanlari[ip] = [
                    zaman for zaman in ip_zamanlari[ip] 
                    if su_an - zaman < ZAMAN_PENCERESI
                ]
                
                deneme_sayisi = len(ip_zamanlari[ip])
                
                print(f"Başarısız deneme: {ip} (Son 5 dk: {deneme_sayisi})")
                
                if deneme_sayisi >= ESIK and ip not in uyarilmis_ipler:
                    print(f"ALARM! {ip} saldırı yapıyor! ({deneme_sayisi} deneme)")
                    uyarilmis_ipler.add(ip)
                    
            except (IndexError, ValueError):  # IP parse hatası 
                print("Log satırı okunamadı")
                continue

except FileNotFoundError:  #Dosya bulunamadı hatası
    print("loglar.txt dosyası bulunamadı!")
    
except KeyboardInterrupt:  # Ctrl+C ile çıkış sağlar.
    print("Program durduruldu.")
    dosya.close()
