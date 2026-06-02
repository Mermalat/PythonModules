# Python Module 01

Bu modul Python'da nesne yonelimli programlamaya giris yapar. Kodlar bitki temasi uzerinden sinif, nesne, constructor, attribute, getter/setter, encapsulation, inheritance, method overriding, static method, class method ve nested class konularini kullanir.

## Genel Yapi

Moduldeki dosyalar `Plant` sinifi etrafinda gelisir. Ilk egzersiz basit degiskenlerle baslar, sonraki egzersizlerde ayni fikir siniflara tasinir ve daha gelismis OOP kavramlari eklenir.

## Kullanilan Temel Konular

### Sinif ve Nesne

`class`, ayni turden nesnelerin ortak ozelliklerini ve davranislarini tanimlar.

```python
class Plant:
    ...
```

Bir siniftan nesne olusturmak icin sinif adi fonksiyon gibi cagirilir:

```python
rose = Plant("Rose", 15.0, 10)
```

### `__init__`

`__init__`, nesne olusturuldugunda otomatik calisan constructor methodudur. Baslangic degerleri burada ayarlanir.

```python
def __init__(self, name: str, height: float, age: int) -> None:
    self._name = name
```

### `self`

`self`, olusturulan nesnenin kendisini temsil eder. Nesneye ait attribute ve methodlara `self` uzerinden erisilir.

```python
self._height = 0.0
```

### Private Benzeri Attribute

Python'da `_name`, `_height`, `_age` gibi tek alt cizgiyle baslayan isimler "bu alan sinifin ic detayi" anlaminda kullanilir. Bu gercek anlamda zorunlu private degildir, ama disaridan dogrudan degistirilmemesi gerektigini anlatir.

### Getter ve Setter

Getter methodlari veri okumak, setter methodlari veri guncellemek icin kullanilir. Bu sayede deger atanmadan once kontrol yapilabilir.

```python
def set_height(self, height: float) -> bool:
    if height < 0:
        return False
    self._height = float(height)
    return True
```

### Encapsulation

Encapsulation, nesnenin verisini koruma altina alip dis dunyaya kontrollu methodlar vermektir. Bu modulde negatif boy veya negatif yas degerleri setter icinde reddedilir.

### Inheritance

Inheritance, bir sinifin baska bir siniftan ozellik ve method almasidir.

```python
class Flower(Plant):
    ...
```

`Flower`, `Tree` ve `Vegetable`, `Plant` sinifindan turetilir.

### `super()`

Alt sinif, ust sinifin constructor veya methodunu kullanmak istediginde `super()` cagirir.

```python
super().__init__(name, height, age)
```

### Method Overriding

Alt sinif, ust siniftaki bir methodun kendi surumunu yazabilir. Buna overriding denir.

```python
def show(self) -> None:
    super().show()
    print("Color: " + self._color)
```

### Static Method

`@staticmethod`, nesneye veya sinifa ait veriye ihtiyac duymayan ama mantiksal olarak sinifla ilgili olan fonksiyonlar icin kullanilir.

```python
@staticmethod
def is_older_than_year(age: int) -> bool:
    return age > 365
```

### Class Method

`@classmethod`, sinifin kendisini `cls` olarak alir. Alternatif constructor yazmak icin kullanislidir.

```python
@classmethod
def anonymous(cls) -> "Plant":
    return cls("Unknown plant", 0.0, 0)
```

### Nested Class

Bir sinifin icinde baska bir sinif tanimlanabilir. `Plant.Statistics`, bitkinin kac kez buyudugunu, yaslandigini ve gosterildigini takip eder.

```python
class Plant:
    class Statistics:
        ...
```

## Egzersizler

### ex0 - `ft_garden_intro.py`

Bu dosya OOP kullanmadan basit degiskenler ile bir bitkinin bilgilerini yazdirir.

Kullanilanlar:

- `main()` fonksiyonu
- String, integer degiskenler
- F-string
- `if __name__ == "__main__":`

Bu egzersiz, sonraki sinifli cozumlerin baslangic noktasi gibidir.

### ex4 - `ft_garden_security.py`

`Plant` sinifi tanimlanir. Bitkinin adi, boyu ve yasi tutulur. Boy ve yas dogrudan atanmak yerine setter methodlariyla kontrol edilir.

Kullanilanlar:

- `class Plant`
- `__init__`
- `_name`, `_height`, `_age`
- `set_height()`
- `set_age()`
- `get_height()`
- `get_age()`
- `show()`
- Negatif deger kontrolu
- Boolean donus degeri ile islemin basarili olup olmadigini bildirme

Bu egzersizin ana fikri, nesne icindeki verinin rastgele degistirilmemesi ve setter ile guvenli hale getirilmesidir.

### ex5 - `ft_plant_types.py`

Bu dosyada `Plant` sinifindan farkli bitki turleri turetilir:

- `Flower`
- `Tree`
- `Vegetable`

`Flower`, renk ve cicek acma durumunu tutar. `Tree`, govde capini ve golge uretme davranisini ekler. `Vegetable`, hasat sezonu ve besin degeri bilgisi tasir.

Kullanilanlar:

- Inheritance
- `super().__init__()`
- Method overriding
- Alt sinifa ozel attribute ekleme
- Ust siniftaki `grow()` ve `age()` methodlarini genisletme

Bu egzersizde her alt sinif `Plant` davranisini kullanir ama kendi ihtiyacina gore ek bilgi ve davranis ekler.

### ex6 - `ft_garden_analytics.py`

Bu egzersiz onceki yapilari daha ileri tasir. Bitki davranislarinin istatistikleri tutulur ve sinif seviyesinde yardimci methodlar eklenir.

Eklenen yapilar:

- `Plant.Statistics`
- `Tree.TreeStatistics`
- `Plant.is_older_than_year()`
- `Plant.anonymous()`
- `display_statistics()`
- `Seed` sinifi

Kullanilanlar:

- Nested class
- Nested class inheritance
- Static method
- Class method
- Polymorphism
- Method overriding zinciri
- Ortak taban sinif uzerinden istatistik gosterme

`Seed`, `Flower` sinifindan turetilir. `bloom()` methodunu override eder ve cicek actiginda seed sayisini gunceller.

## Calistirma

```bash
python ex0/ft_garden_intro.py
python ex4/ft_garden_security.py
python ex5/ft_plant_types.py
python ex6/ft_garden_analytics.py
```

## Ogrenme Sirasi

Once `ex0` ile basit degiskenli programi incelemek, sonra `ex4` ile ayni fikrin sinifa nasil tasindigini gormek iyi olur. Ardindan `ex5` inheritance konusunu, `ex6` ise daha gelismis sinif ozelliklerini anlatir.
