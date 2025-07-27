#kullanılan kütüphaneler
import csv
from datetime import datetime
import random
import sys

#kelimeleri yükle fonksiyonu examplewords.csv dosyasından kelimeleri almamızı sağlıyor.
def kelimeleri_yukle():
    #examplewords.csv kelimelerin olduğu dosya örnek dosyadaki gibi kelimleri en-tr olacak şekilde dosyaya yazmanız lazım
    dosya_yolu='data/examplewords.csv'

    try:
        with open(dosya_yolu,'r',encoding='utf-8',newline='') as csv_file:
            kelimeler = dict(csv.reader(csv_file))
            kelimeler.pop("english",None)
            kelimeler.pop("English",None)
            kelimeler.pop("ENGLISH",None)

            if not kelimeler:
                print("words dosyası boş")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Dosyayı bulunamadı : {dosya_yolu}")
        sys.exit(1)

    except PermissionError:
        print(f"Dosyaya erişim izni yok : {dosya_yolu}")
        sys.exit(1)

    except IsADirectoryError:
        print(f"Bu bir dosya değil, klasör {dosya_yolu}")
        sys.exit(1)

    except UnicodeDecodeError:
        print(f"Dosya kodlamasi uyumsuz ya da dosya boş!")
        sys.exit(1)

    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu : {type(e).__name__} - {e}")
        sys.exit(1)

    return kelimeler

def kelime_sor(kelimeler : dict, tur_sayisi : int):
#kelime sor fonksiyonu dict şekilde aldığımız kelimeleri kullanıcın istediği tur sayisina göre karışık şekilde sormamızı sağlıyor
    dogru_sayaci = 0
    yanlis_sayaci = 0
    secilen_kelimeler = random.sample(list(kelimeler.keys()), k=min(tur_sayisi, len(kelimeler)))

    for tur,ingilizce in enumerate(secilen_kelimeler,1):
        try:
            print(f"\nİngilizcesi : {ingilizce}")
            dogru_cevap = kelimeler[ingilizce]

            while True:
                giris = input("Turkcesini giriniz : ").strip().lower()
                if not giris.isalpha():
                    print("Lütfen sadece harf kullanın.")
                    continue
                break

            if dogru_cevap == giris:
                print("Doğru!")
                dogru_sayaci+=1

            else:
                print(f"Hatali cevap! Doğrusu : {dogru_cevap}")
                yanlis_sayaci+=1
        except Exception as e:
            print(f"bilinmeyen bir hata oluştu : {type(e).__name__}{e}")
            sys.exit(2)

    return dogru_sayaci,yanlis_sayaci

def oyun_uzulugunlu():
#oyuncudan oyun uzunluğunu almamızı sağlıyor istediğiniz gibi düzenleyebilirsiniz ben 1-20 arası tuttum
    while True:
        try:
            secim = int(input("Kac tur oynamak istersiniz (1-20): "))
            if secim < 1 or secim > 20:
                print("hatali giris")
                continue
            print(f"Secilen tur sayisi : {secim}")
            return secim
        except ValueError:
            print("Gecersiz giris yaptiniz tekrar deneyin")
            continue


def kullanici_bilgisi():
#oyuncu bilgisini öğrenmemizi sağlıyor
    try:
        while True:
            kullanici_adi = input("Oyuncu adini giriniz : ").strip().lower()

            if " " in kullanici_adi:
                print("Adinizi bitisik yaziniz!")
                continue
            elif not kullanici_adi.isalpha():
                print("Adiniz sadece harften olusmali!")
                continue
            break
        print(f"Oyuncu {kullanici_adi}")
        return kullanici_adi
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu : {type(e).__name__}{e}")
        sys.exit(3)


def giris_ekrani():
#kullanicinin ilk giriş yaptığında karşılaşacağı menu ekrani
    print("\n"+"*"*10+"MENU"+"*"*10)
    print("_"*24)
    print("1.Oyunu Basla")
    print("2.Skor Tablosunu Goster")
    print("3.Çıkış")
    print("_"*24)

    while True:
        try:
            giris = input("\nNe yapmak istersiniz lütfen listeden seçiniz : ")

            if giris == '1':
                return 1
            elif giris == '2':
                return 2
            elif giris == '3':
                exit(0)
            else:
                print("sadece 1 ya da 2'yi seciniz!")
                continue

        except Exception as e:
            print(f"Bilinmeyen bir hata olustu : {type(e).__name__}{e}")
            sys.exit(4)


def oyun_oynama_secimi():
#burada kullanicidan tekrar oyun oynamak isteyip istemediğini öğrenmek için kullancdığımız fonksiyon
    while True:
        try:
            islem = input("Oyun oynamak ister misiniz (e/h) : ").strip().lower()

            if islem == 'e':
                return 'e'
            elif islem == 'h':
                return 'h'
            else:
                print("Sadece 'e' ya da 'h' tuslayınız")

        except Exception as e:
            print(f"Bilinmeyen bir hata oluştu : {type(e).__name__}{e}")
            sys.exit(5)


def quizi_baslat(kullanici_adi : str):
#quizi başlatmak için kullandiğimiz fonksiyon
    print("Dogru cevap 10, yanlis cevap -5 puan. Basarılar!")

    kelimeler = kelimeleri_yukle()
    tur_sayisi = oyun_uzulugunlu()
    sonuc = kelime_sor(kelimeler,tur_sayisi)
    skor = sonuc[0]*10 - sonuc[1]*5

    print(f"Dogru cevap : {sonuc[0]} | Yanlis cevap : {sonuc[1]}")
    print(f"Skor : {skor}")

    sonuclari_kaydet(kullanici_adi,skor)
    gezinme_ekrani(kullanici_adi)


def sonuclari_kaydet(kullanci_adi : str, skor : int):
#en sonda sonuçları kaydetmek için kullandiğimiz fonksiyon aynı data klasörüne .csv dosyası olacak şekilde sonuçları kaydediyoruz
    try:
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        satir = [kullanci_adi, skor, tarih]
        dosya_yolu = "data/scores.csv"

        with open(dosya_yolu, 'a', encoding="utf-8", newline="") as dosya:
            yazilacakz_dosya = csv.writer(dosya)
            yazilacakz_dosya.writerow(satir)
    except FileNotFoundError:
        print("Yazilacak dosya bulunamadi lütfen skorları kaydetmek icin dosya oluşturunuz example: data/scores.csv")
        sys.exit(6)
    except PermissionError:
        print("Skorları kaydetmek icin yazilacak dosyaya erişiminiz yok!")
        sys.exit(6)
    except Exception as e:
        print(f"Bilinmeyen bir hata olustu {type(e).__name__} {e}")


def skor_tablosu_oku():
#data klasörüne kaydettiğimiz .csv dosyasını okuyarak list şeklinde alıyoruz
    try:
        with open('data/scores.csv', 'r', encoding='utf-8', newline='') as skor_csv:
            skorlar = list(csv.reader(skor_csv))

    except FileNotFoundError:
        print("Skor dosyasi bulunamadi!")
        sys.exit(7)

    except PermissionError:
        print(f"Dosyaya erişim izni yok : data/scores.csv")
        sys.exit(7)

    except IsADirectoryError:
        print(f"Bu bir dosya değil, klasör data/scores.csv")
        sys.exit(7)

    except UnicodeDecodeError:
        print(f"Dosya kodlamasi uyumsuz ya da dosya boş!")
        sys.exit(7)

    except Exception as e:
        print(f"Bilinmeyen bir hata olustu {type(e).__name__} {e}")
        sys.exit(7)
    return skorlar


def skor_tablosu_goster(kullanici_adi):
#okuduğumuz tabloyu ekrana yazdırıyoruz
    try:
        skorlar = skor_tablosu_oku()
        if not skorlar:
            print("Henüz kayitli skor yok!")
            return

        #skorlari büyükten küçüğe sıralıyoruz
        skorlar = sorted(skorlar,key=lambda satir: int(satir[1]), reverse=True)

        #şuan oyunu oynayan kullanıcın geçmiş skorlara göre hangi sıralamada olduğunu öğreniyoruz
        siralama = next((i+1 for i, satir in enumerate(skorlar) if satir[0] == kullanici_adi), None)

        basliklar = ["Ad", "Skor", "Tarih"]

        #tabloyu doğru hizalamak için skorlardaki en geniş sütunları buluyoruz
        genislikler = [max(len(satir[i])for satir in skorlar) for i in range (3)]

        print("\n"+"*** En İyi 10 Skor ***".center(40))
        print("_"*40)
        print(" | ".join([basliklar[i].ljust(genislikler[i]) for i in range(3)]))
        print("_"*40)

        for satir in skorlar[:10]:
            print(" | ".join([satir[i].ljust(genislikler[i]) for i in range(3)]))
        print("_"*40)

        if siralama:
            print(f"{kullanici_adi}, {siralama}.siradasin.")
        else:
            print(f"{kullanici_adi}, siralamaya giremedin.")

    except ValueError:
        print("Skorlar dosyasında ki veriler hatali!")
        sys.exit(8)
    except Exception as e:
        print(f"Bilinmeyen bir hata olustu {type(e).__name__} {e}")
        sys.exit(8)


def gezinme_ekrani(kullanici_adi : str):
#ilk giriş ekranindan sonra islemlerden sonra menude gezinmek için ekrana yazılan menu ekrani
    islem_secimi = giris_ekrani()
    if islem_secimi == 1:
        quizi_baslat(kullanici_adi)
    elif islem_secimi == 2:
        skor_tablosu_goster(kullanici_adi)
        secim = oyun_oynama_secimi()
        if secim == 'e':
            quizi_baslat(kullanici_adi)


def baslat():
#başlat bizim ana kod bloğumuzu çalıştıran fonksiyondur
    kullanici_adi = kullanici_bilgisi()
    print("Kelime Quizi Oyununa Hos Geldiniz")
    islem_secimi = giris_ekrani()
    if islem_secimi == 1:
        quizi_baslat(kullanici_adi)
    elif islem_secimi == 2:
        skor_tablosu_goster(kullanici_adi)
        secim = oyun_oynama_secimi()
        if secim == 'e':
            quizi_baslat(kullanici_adi)


if __name__ == "__main__":
    baslat()
