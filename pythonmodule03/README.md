# Python Module 03

Bu modul komut satiri argumanlari, Python veri yapilari ve veri donusturme pratiklerine odaklanir. Oyun temali egzersizlerde `sys.argv`, list, tuple, set, dictionary, generator, comprehension, hata yakalama ve matematiksel hesaplama kullanilir.

## Kullanilan Temel Konular

### `sys.argv`

`sys.argv`, program calistirilirken terminalden verilen argumanlari tutan listedir.

```bash
python ex0/ft_command_quest.py sword shield
```

Bu komutta:

- `sys.argv[0]` dosya adidir.
- `sys.argv[1]` `"sword"` olur.
- `sys.argv[2]` `"shield"` olur.

### `len()`

Bir listenin, stringin veya koleksiyonun eleman sayisini verir.

```python
len(sys.argv)
```

### `while`

`while`, kosul dogru oldugu surece calisir. Bu modulde argumanlari tek tek gezmek icin kullanilir.

```python
index = 1
while index < len(sys.argv):
    ...
    index += 1
```

### List

List sirali ve degistirilebilir veri tutar. Skorlar ve event listeleri icin kullanilir.

```python
scores: list[int] = []
scores.append(100)
```

### Tuple

Tuple sirali ama degistirilmemesi beklenen veri gruplari icin kullanilir. Koordinatlar `(x, y, z)` olarak tuple icinde tutulur.

```python
return (x_pos, y_pos, z_pos)
```

### Set

Set benzersiz elemanlar tutar. Basarim analizinde ayni basarimin tekrar etmesini engeller.

Kullanilan set islemleri:

- `union()`: Iki setin tum elemanlarini birlestirir.
- `intersection()`: Ortak elemanlari bulur.
- `difference()`: Bir sette olup digerinde olmayanlari bulur.

### Dictionary

Dictionary key-value yapisidir. Inventory ve oyuncu skorlarinda kullanilir.

```python
inventory: dict[str, int] = {}
inventory["sword"] = 2
```

### `try` / `except`

Hata cikabilecek islemleri guvenli hale getirmek icin kullanilir. Bu modulde string'i sayiya cevirirken `ValueError` yakalanir.

```python
try:
    scores.append(int(sys.argv[index]))
except ValueError:
    print("Invalid parameter")
```

### Generator ve `yield`

Generator, degerleri tek seferde liste olarak uretmek yerine ihtiyac oldukca uretir.

```python
def gen_event():
    while True:
        yield (player, action)
```

### Comprehension

List veya dictionary uretmek icin kisa yazimdir.

```python
capitalized_players = [player.capitalize() for player in players]
```

```python
score_by_player = {
    player: random.randint(50, 999) for player in capitalized_players
}
```

## Egzersizler

### ex0 - `ft_command_quest.py`

Program adini ve terminalden verilen argumanlari yazdirir.

Kullanilanlar:

- `import sys`
- `sys.argv`
- `len()`
- `while`
- F-string

Bu egzersiz komut satirindan gelen verinin Python icinde nasil temsil edildigini gosterir.

### ex1 - `ft_score_analytics.py`

Komut satirindan skorlar alir, gecersiz degerleri ayiklar ve istatistik hesaplar.

Kullanilanlar:

- `list[int]`
- `append()`
- `int()` donusumu
- `try` / `except ValueError`
- `sum()`
- `max()`
- `min()`
- Ortalama hesaplama
- Skor araligi hesaplama

Ornek:

```bash
python ex1/ft_score_analytics.py 100 250 abc 90
```

`abc` sayiya cevrilemedigi icin gecersiz parametre olarak raporlanir.

### ex2 - `ft_coordinate_system.py`

Kullanicidan iki farkli 3D koordinat alir ve mesafe hesaplar.

Kullanilanlar:

- `import math`
- `input()`
- `split(",")`
- `float()`
- Tuple return type
- Fonksiyon parametrelerinde tuple type hint
- `math.sqrt()`
- Us alma operatoru `**`
- `round()`

Mesafe formulu:

```python
sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
```

Bu egzersiz hem input dogrulama hem de tuple ile veri gruplama pratigi verir.

### ex3 - `ft_achievement_tracker.py`

Oyuncular icin rastgele basarim setleri olusturur ve set islemleriyle analiz yapar.

Kullanilanlar:

- `import random`
- Sabit listeler
- `random.randint()`
- `random.sample()`
- `set`
- `dict[str, set[str]]`
- `union()`
- `intersection()`
- `difference()`

Hesaplananlar:

- Tum oyuncularda gorulen tum basarimlar
- Her oyuncuda ortak olan basarimlar
- Sadece tek bir oyuncuda bulunan basarimlar
- Her oyuncunun eksik basarimlari

### ex4 - `ft_inventory_system.py`

Terminalden `item:quantity` formatinda arguman alir ve inventory dictionary'si olusturur.

Kullanilanlar:

- `sys.argv`
- `split(":")`
- Dictionary ekleme
- `keys()`
- `values()`
- `list()`
- `sum()`
- Duplicate key kontrolu
- Yuzde hesaplama
- En cok ve en az bulunan item'i bulma
- `dict.update()`

Ornek:

```bash
python ex4/ft_inventory_system.py sword:2 potion:5 shield:1
```

Bu egzersiz dictionary ile veri modelleme ve komut satiri verisini parse etme konusunu calistirir.

### ex5 - `ft_data_stream.py`

Rastgele oyun eventleri ureten ve liste icindeki eventleri rastgele tuketen iki generator icerir.

Kullanilanlar:

- `typing.Generator`
- Sonsuz `while True`
- `yield`
- `random.choice()`
- `random.randrange()`
- `next()`
- `list.pop()`

`gen_event()` sonsuz event uretir. `consume_event()` ise verilen listenin elemanlarini rastgele sirayla tuketir.

### ex6 - `ft_data_alchemist.py`

Oyuncu isimlerini ve skorlarini comprehension kullanarak donusturur.

Kullanilanlar:

- List comprehension
- Dict comprehension
- `str.capitalize()`
- `random.randint()`
- Ortalama hesaplama
- Kosullu dict comprehension

Uretilen veriler:

- Tum isimlerin bas harfi buyuk hali
- Zaten dogru capitalized olan isimler
- Oyuncu -> skor dictionary'si
- Ortalama ustu skorlar

## Calistirma

Komut satiri argumani isteyenler:

```bash
python ex0/ft_command_quest.py sword shield potion
python ex1/ft_score_analytics.py 100 250 90
python ex4/ft_inventory_system.py sword:2 potion:5 shield:1
```

Input isteyen veya kendi verisini uretenler:

```bash
python ex2/ft_coordinate_system.py
python ex3/ft_achievement_tracker.py
python ex5/ft_data_stream.py
python ex6/ft_data_alchemist.py
```
