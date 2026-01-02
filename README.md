**SSH Attack Detector**, sunucu loglarını gerçek zamanlı olarak izleyen ve **Brute-Force (Kaba Kuvvet)** saldırılarını tespit eden Python tabanlı bir güvenlik aracıdır.

Siber güvenlik operasyonlarında, başarısız giriş denemelerini analiz etmek ve saldırgan IP adreslerini belirlemek kritik öneme sahiptir. Bu proje, belirli bir zaman penceresi içindeki anormallikleri tespit ederek basit bir **IDS (Saldırı Tespit Sistemi)** mantığıyla çalışır.

## 🚀 Özellikler

* **Canlı Log İzleme:** Dosya sonuna eklenen verileri anlık olarak ("tailing") takip eder.
* **Sliding Window (Kayan Pencere):** Sadece son 5 dakika (300 saniye) içindeki denemeleri analiz eder, eski verileri bellekten temizler.
* **Eşik Kontrolü:** Belirlenen başarısız deneme sayısı (Varsayılan: 5) aşıldığında alarm üretir.
* **Optimizasyon:** `defaultdict` ve `set` veri yapıları ile performanslı çalışır.

## 🛠️ Kurulum
Bu proje **Python 3** ile çalışır ve harici bir kütüphane kurulumu gerektirmez.

⚠️ Yasal Uyarı
Bu yazılım eğitim ve savunma amaçlı geliştirilmiştir. Sistem yöneticilerinin kendi sunucularını izlemelerine yardımcı olmayı hedefler. Sadece yetkili olduğunuz sistemlerde test ediniz.
