# İngilizce-Türkçe Kelime Quiz Oyunu

Bu proje, İngilizce kelimelerin Türkçe karşılıklarını test eden komut satırı tabanlı interaktif bir quiz oyunudur. Öğrenme ve tekrar yapmak isteyenler için sade ve kullanışlı bir uygulama sunar.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)
- [Lisans](#Lisans)

---

## Genel Bakış

Bu Python projesi, `examplewords.csv` dosyasından İngilizce-Türkçe kelimeleri okuyarak kullanıcının Türkçe karşılıklarını girmesini isteyen bir quiz oluşturur. Kullanıcı doğru ve yanlış cevaplarına göre puan kazanır ve sonuçlar `scores.csv` dosyasına kaydedilir. Oyunun sonunda kullanıcı skoru ve skor tablosu gösterilir.

---

## Özellikler

- Kelimeler CSV dosyasından dinamik olarak yüklenir.
- Kullanıcı adı ile kişisel skor kaydı ve skor tablosu.
- İstenen tur sayısına göre rastgele karışık kelime soruları.
- Hatalı girişlere karşı detaylı hata yönetimi ve kullanıcı uyarıları.
- Skor tablosunda en iyi 10 skor sıralaması ve kullanıcının sıralaması gösterilir.
- Basit ve kullanımı kolay menü arayüzü.
- Dosya bulunamama, erişim izni hataları gibi durumlar için kapsamlı hata yakalama.

---

## Kurulum

1. Python 3 yüklü olduğundan emin olun.  
2. Projeyi klonlayın veya zip olarak indirin.  
3. `data` klasörü altında `examplewords.csv` ve `scores.csv` dosyalarını oluşturun.

`examplewords.csv` örnek formatı:

```
english,turkish
apple,elma
book,kitap
car,araba
```

`scores.csv` ise başlangıçta boş olabilir, program otomatik ekleyecektir.

---

## Kullanım

Terminal veya komut satırında projenin bulunduğu dizinde:

```bash
python quiz.py
```

Ardından ekrandaki yönergeleri takip ederek:

- Oyuncu adı girin.
- Menüden oyun başlatma, skor tablosu gösterme veya çıkış yapma seçeneklerini kullanın.
- Tur sayısını seçin (1-20 arası).
- Sorulan İngilizce kelimelerin Türkçe karşılıklarını yazın.
- Sonuçlarınızı görün ve kaydedin.

---

## Dosya Yapısı

```
.
├── quiz.py                # Ana Python kod dosyası
├── data
│   ├── examplewords.csv   # İngilizce-Türkçe kelime listesi
│   └── scores.csv         # Skorların kaydedildiği dosya
├── README.md              # Bu dosya
```
---
## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  
Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz — ancak orijinal geliştiriciyi belirtmeniz gerekir.

---

## Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.  



**İyi çalışmalar ve bol kelime öğrenmeli oyunlar!**
