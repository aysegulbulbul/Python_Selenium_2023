"""
Python Veri Tipleri

1. Numbers: Sayısal her türlü değeri saklar.
   Kendi içinde alt tanımları: integer(tamsayılar), float(ondalıklı sayılar), complex(reel sayılar)
   
2. Strings: Öncelikli text değerlerini saklar. 
   Fakat sayısal değerler de String haline çevrilebilir. 
   
3. Lists: Bileşik veri tipidir.
   Farklı veya aynı tipte 1 veya daha fazla değeri birarada saklar.
   List yaratıldıktan sonra güncellenebilir. 
   
4. Tuples: Bileşik veri tipidir.
   Farklı veya aynı tipte 1 veya daha fazla değeri birarada saklar.
   Tuple yaratıldıktan sonra güncellenemez.
   
5. Dictionary: Bileşik veri tipidir, bir çeşit hash tablo türüdür.
   İçindeki değerlerin herbirine bir anahtar(key) atanır. Key sayesinde veriye hızlıca ulaşılır.
   
   
***********************************************************************************************************

Kodlama.io Sitesindeki Değişkenler

String  örnekler: "Kurslarım", "Tüm Kurslar", "Kariyer" alt başlıkları
Integer örnekler: Dersin tamamlanma yüzdesi, yorumların adedi
List    örnekler: Eğitmen(List'in değerleri:Tümü,Engin Demirog,Halit Enes Kalaycı)


************************************************************************************************************
#Kodlama.io sitesinde bulunan veri tipleri örnekleri

*(string)*
kursAdı = "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"
print(kursAdı)
print(type(kursAdı))

*(int,float,double)*
#Kodlama.io sitesinde bulunan kurs tamamlama oranları rakamsal veri tipleri için örnek olarak verilebilir.

*(bool)*
#bool veya boolean şeklinde tabir edilen veri tipleri tanımlanan durumun sonucunun True veya False olarak işleme alınmasını sağlar.
bool1 = True
print(bool1)
print(type(bool1))
bool2 = False
print(bool2)
print(type(bool2))
bool3 = 10 - 2 > 9 # bu değişken 8 > 9 koşulunu sorgulayacağı için bize False şeklinde dönüş yapmasını beklemeliyiz.
print(bool3)

*(Dizi Tipleri)*
#Dizi tipleri içerisine birden fazla eleman atayabildiğimiz, türlerine göre farlılık gösteren liste türleridir ve index numaraları vardır.
print("List")
#içerisine farklı tiplerde elemanlar atayabildiğimiz ve aynı elamanı birden fazla kabul edebilen bir veri tipidir.
list = ["Kodlama.io", 5, True, "Hello World", True]
list.remove("Kodlama.io") #listeler'de içerisindeki elemanları silmemiz mümkündür.
print(list)
print(len(list))

*(Tuple)*
#list'den farklı olarak elemanları dinamik değildir, yani elamanlarını değiştiremeyiz, aynı elemanı birden fazla kabul edebilir.
#oluşturuken () parantez ile oluşturulurlar ve index numarası vardır.
tuple = (1, 2, 3)
print(tuple)

*(Set)*
#Set türünde ise index numarası bulunmamaktadır ve elaman tekrarını kabul etmez yani bir eleman sadece bir defa kabul edilir.
#setler {} süslü parentez ile oluşturulur.

arabaMarkaları = {"Toyota", "Mazda", "Mitsubishi"}
print(arabaMarkaları)
print("Set yapı türlerinde her bir elemana for each loop döngü yapısıyla ulaşabiliriz")
for marka in arabaMarkaları:
    print(marka.upper())

#Kodlama.io sitesinde bulunan kur Tüm Kurslar Listelere örnek olarak gösterilebilir.

************************************************************************************************************

Kodlama.io Sitesindeki Şart Blokları

kursÜcretsiz = False

if(kursÜcretsiz == True):
    print("Ücretsiz")
else:
    print("Ücretli")


"""