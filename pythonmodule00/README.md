# Python Module 00

Bu modul Python'a giris seviyesindeki temel konulari bahce temali kucuk fonksiyonlarla anlatir. Her egzersiz tek bir dosyada durur ve basit bir programlama fikrini uygular: ekrana yazdirma, kullanicidan veri alma, sayi donusumu, kosul, dongu, recursion ve type hint.

## Genel Yapi

Egzersiz dosyalari `ex0` ile `ex7` arasinda klasorlenmistir. Her dosyanin icinde ayni ada sahip bir fonksiyon bulunur. Ornegin:

```python
def ft_plot_area():
    ...
```

Bu yapi, fonksiyonlari test etmeyi kolaylastirir. Modul kokundeki `main.py`, kullanicidan hangi egzersizi test etmek istedigini alir ve ilgili fonksiyonu calistirmaya calisir.

## Kullanilan Temel Konular

### `print()`

`print()` fonksiyonu ekrana metin yazdirmak icin kullanilir. Bu modulde ilk egzersizden itibaren cikti uretmenin temel yolu budur.

```python
print("Hello, Garden Community!")
```

### `input()`

`input()` kullanicidan terminal uzerinden veri alir. Geri donen deger her zaman `str` tipindedir. Sayi olarak kullanilacaksa once donusturulmelidir.

```python
name = input("Enter garden name: ")
```

### `int()`

Kullanicidan gelen metinsel sayilari tam sayiya cevirmek icin kullanilir.

```python
length = int(input("Enter length: "))
```

Kullanici sayi olmayan bir deger girerse program `ValueError` hatasi alabilir.

### F-string

Degiskenleri metin icine temiz sekilde yerlestirmek icin f-string kullanilir.

```python
print(f"Plot area: {length * width}")
```

### Kosul Yapisi

`if` ve `else`, bir durumun dogru olup olmamasina gore farkli cikti uretmek icin kullanilir.

```python
if age > 60:
    print("Plant is ready to harvest!")
else:
    print("Plant needs more time to grow.")
```

### Dongu

`for` dongusu belirli sayida tekrar yapmak icin kullanilir. `range(1, days + 1)` ifadesi 1'den baslayip `days` degerine kadar sayar.

```python
for i in range(1, days + 1):
    print(f"Day {i}")
```

### Recursion

Recursion, bir fonksiyonun kendi kendini cagirmasidir. `ft_count_harvest_recursive.py` icinde `helper()` fonksiyonu gun sayisini artirarak kendini tekrar cagirir. Bitirme kosulu olmazsa recursion sonsuza kadar surer.

```python
def helper(day):
    if day > days:
        print("Harvest time!")
        return

    print(f"Day {day}")
    helper(day + 1)
```

### Type Hint

`ft_seed_inventory()` fonksiyonunda parametre tipleri belirtilir:

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

Bu ifade fonksiyonun iki metin, bir tam sayi aldigini ve deger dondurmedigini anlatir. Type hint Python'u zorla statik tipli yapmaz, ama kodun okunmasini ve kontrol edilmesini kolaylastirir.

## Egzersizler

### ex0 - `ft_hello_garden.py`

Bu egzersiz sadece ekrana sabit bir mesaj yazdirir.

Kullanilanlar:

- Fonksiyon tanimlama
- `print()`
- Sabit string

### ex1 - `ft_garden_name.py`

Kullanicidan bahce adi alir ve iki satirlik bir durum mesaji yazdirir.

Kullanilanlar:

- `input()`
- Degiskene deger atama
- F-string
- String icinde `\n` ile yeni satir kullanimi

### ex2 - `ft_plot_area.py`

Kullanicidan uzunluk ve genislik alir, alan hesaplar.

Kullanilanlar:

- `input()`
- `int()` ile tip donusumu
- Carpma operatoru `*`
- F-string ile sonuc yazdirma

### ex3 - `ft_harvest_total.py`

Uc farkli gunun hasat miktarini alir ve toplamlarini yazdirir.

Kullanilanlar:

- Birden fazla input alma
- Tam sayi donusumu
- Toplama operatoru `+`
- Degerleri tek ifadede toplama

### ex4 - `ft_plant_age.py`

Bitkinin yasi 60 gunden buyukse hasada hazir oldugunu, degilse daha buyumesi gerektigini soyler.

Kullanilanlar:

- `if`
- `else`
- Karsilastirma operatoru `>`
- Sayi tabanli karar verme

### ex5 - `ft_water_reminder.py`

Son sulamadan gecen gun sayisini kontrol eder. 2 gunden fazlaysa sulama uyarisi verir.

Kullanilanlar:

- `if` / `else`
- Esik degeriyle kontrol
- Kullanicidan sayi alma

### ex6 - Iterative ve Recursive Sayac

Bu egzersizde ayni fikir iki farkli yolla cozulur.

`ft_count_harvest_iterative.py` dongu kullanir:

- `for`
- `range()`
- Sirali sayma

`ft_count_harvest_recursive.py` recursion kullanir:

- Ic fonksiyon
- Base case
- Fonksiyonun kendi kendini cagirmasi

### ex7 - `ft_seed_inventory.py`

Tohum turu, miktar ve birim alir. Birime gore farkli mesaj yazar.

Kullanilanlar:

- Parametreli fonksiyon
- Type hint
- `str.capitalize()`
- `if` / `elif`
- Farkli birimlere gore dallanma

## `main.py` Ne Yapar?

`main.py`, egzersizleri secerek test etmek icin yazilmis yardimci dosyadir.

Kullandigi yapilar:

- `input()` ile secim alma
- `if` / `elif` / `else` ile secime gore karar verme
- `__import__()` ile modul import etme
- `getattr()` ile fonksiyonu adindan bulma
- `try` / `except` ile hata yakalama
- `sys.path.append()` ile import yolu ekleme
- `if __name__ == "__main__":` ile dosya dogrudan calistirildiginda `main()` fonksiyonunu baslatma

## Calistirma

Tek egzersiz:

```bash
python ex0/ft_hello_garden.py
```

Yardimci menu:

```bash
python main.py
```

Not: `main.py` icindeki import yolu bazi egzersiz klasorleri icin elle duzenleme isteyebilir.
