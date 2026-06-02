# Python Module 05

Bu modul daha ileri Python konularina girer: abstract base class, polymorphism, type hint, union type, `Any`, `Protocol`, veri dogrulama, veri akis yonetimi ve plugin benzeri cikti sistemi. Kodlar `DataProcessor` fikrinden baslayip daha buyuk bir data pipeline yapisina dogru ilerler.

## Genel Fikir

Modulde uc ana veri tipi islenir:

- Sayisal veri
- Metin verisi
- Log verisi

Bu verilerin her biri icin ayri processor sinifi vardir. Her processor gelen veriyi once dogrular, sonra string formatinda kendi ic kuyruguna ekler. Daha sonra bu islenmis veriler sirayla disari alinabilir.

## Kullanilan Temel Konular

### `ABC` ve Abstract Class

`ABC`, abstract base class olusturmak icin kullanilir. Abstract class dogrudan kullanilmak icin degil, ortak arayuz tanimlamak icin vardir.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    ...
```

`DataProcessor`, tum processor siniflarinin ortak davranisini tanimlar.

### `@abstractmethod`

Alt siniflarin mutlaka yazmasi gereken methodlari belirtir.

```python
@abstractmethod
def validate(self, data: Any) -> bool:
    pass
```

Bu modulde her processor su methodlari kendi veri tipine gore uygular:

- `validate()`
- `ingest()`

### Polymorphism

Farkli siniflar ayni method adlarini kullanir ama farkli davranir. `NumericProcessor`, `TextProcessor` ve `LogProcessor` siniflarinin hepsinde `validate()` ve `ingest()` vardir, fakat her biri kendi veri tipini kontrol eder.

Bu sayede `DataStream`, processor'un detayini bilmeden sadece `processor.validate(data)` ve `processor.ingest(data)` cagirabilir.

### Type Hint ve Union Type

Kodda modern union type yazimi kullanilir:

```python
NumericData = int | float | list[int | float]
TextData = str | list[str]
LogData = dict[str, str] | list[dict[str, str]]
```

Bu ifadeler okunabilir alias'lardir. Ornegin `NumericData`, tek bir `int`, tek bir `float` veya sayilardan olusan bir liste olabilir.

### `Any`

`Any`, herhangi bir tip gelebilir anlamina gelir. Processor'lar once gelen verinin uygun olup olmadigini anlamak zorunda oldugu icin `validate()` parametresi `Any` olarak tanimlanir.

```python
def validate(self, data: Any) -> bool:
```

### Listeyi Kuyruk Gibi Kullanma

`DataProcessor` icinde `_items` listesi islenmis verileri tutar.

```python
self._items: list[tuple[int, str]] = []
```

Her item `(rank, value)` seklinde saklanir. `rank`, verinin kacinci sirada islendiginin bilgisidir.

`output()` methodu ilk elemani cikarir:

```python
return self._items.pop(0)
```

Bu davranis listeyi FIFO kuyruk gibi kullanir: ilk giren ilk cikar.

### Veri Dogrulama

Her processor, kendisine gelen verinin kendi formatina uygun olup olmadigini kontrol eder.

`NumericProcessor`:

- `int`
- `float`
- `int` veya `float` listesi

`TextProcessor`:

- `str`
- `str` listesi

`LogProcessor`:

- `dict[str, str]`
- `dict[str, str]` listesi

Uygun olmayan veri `ValueError` ile reddedilir.

### `Protocol`

`Protocol`, bir sinifin belirli methodlara sahip olmasini bekleyen yapisal tip sistemidir. `ExportPlugin`, cikti plugin'lerinin hangi methodu saglamasi gerektigini anlatir.

```python
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass
```

Bir sinif bu methodu yaziyorsa, export plugin gibi kullanilabilir.

## Egzersizler

### ex0 - `data_processor.py`

Bu dosya temel processor sistemini kurar.

Siniflar:

- `DataProcessor`
- `NumericProcessor`
- `TextProcessor`
- `LogProcessor`

`DataProcessor` icindeki ortak alanlar:

- `name`: Processor adi
- `_items`: Islenmis verilerin tutuldugu liste
- `_next_rank`: Siradaki veriye verilecek rank

`DataProcessor` icindeki ortak methodlar:

- `validate()`: Abstract method, alt sinifta yazilir.
- `ingest()`: Abstract method, alt sinifta yazilir.
- `output()`: Islenmis ilk veriyi dondurur ve listeden siler.
- `_store()`: Veriyi rank ile birlikte saklar.

`NumericProcessor`:

- Sayisal verileri kabul eder.
- Liste geldiyse her elemani ayri ayri saklar.
- Verileri string'e cevirip depolar.

`TextProcessor`:

- String veya string listesi kabul eder.
- Metni oldugu gibi depolar.

`LogProcessor`:

- Key ve value degerleri string olan dictionary verilerini kabul eder.
- `log_level` ve `log_message` varsa `"LEVEL: message"` formatina cevirir.
- Baska log dictionary'lerini `"key: value"` seklinde birlestirir.

Kullanilan ek yapilar:

- `isinstance()`
- `type(data) in (...)`
- `all()`
- `raise ValueError`
- Helper method: `_is_log_entry()`
- Helper method: `_format_log()`

### ex1 - `data_stream.py`

Bu dosya processor'lari yoneten `DataStream` sinifini ekler.

`DataStream` alanlari:

- `_processors`: Kayitli processor listesi

`DataStream` methodlari:

- `register_processor()`: Processor ekler.
- `process_stream()`: Gelen veri listesindeki her elemani uygun processor'a yollar.
- `print_processors_stats()`: Her processor'un istatistiklerini yazdirir.
- `_find_processor()`: Veriyi kabul edebilen ilk processor'u bulur.

`DataProcessor` sinifina eklenen methodlar:

- `remaining()`: Processor icinde bekleyen item sayisini verir.
- `total_processed()`: Toplam islenen item sayisini verir.

Bu egzersizin ana fikri, sistemin processor detaylarini bilmeden veriyi uygun yere yonlendirmesidir. Bu polymorphism sayesinde mumkun olur.

Akis:

1. `DataStream` olusturulur.
2. Processor'lar kaydedilir.
3. Veri listesi stream'e verilir.
4. Her veri uygun processor tarafindan islenir.
5. Istatistikler yazdirilir.

### ex2 - `data_pipeline.py`

Bu dosya export pipeline fikrini ekler. Islenmis veriler artik farkli cikti formatlarina gonderilebilir.

Yeni yapilar:

- `ExportPlugin`
- `CSVExportPlugin`
- `JSONExportPlugin`
- `DataStream.output_pipeline()`

`CSVExportPlugin`:

- Gelen output verilerini virgul ile birlestirir.
- Basit CSV benzeri cikti uretir.

`JSONExportPlugin`:

- Gelen output verilerini JSON benzeri string olarak yazar.
- Rank degerlerini `item_0`, `item_1` gibi key'lere cevirir.
- Ozel karakterler icin `_escape_json()` methodunu kullanir.

`_escape_json()` sunlari kacirir:

- Ters slash `\\`
- Cift tirnak `"`
- Yeni satir `\n`
- Carriage return `\r`
- Tab `\t`

`output_pipeline(nb, plugin)` methodu:

- Her processor'dan en fazla `nb` adet item alir.
- Item varsa verilen plugin'e yollar.
- Plugin'in `process_output()` methodunu cagirir.

Bu egzersizde sistem artik acik genislemeye daha yakindir. Yeni export bicimi eklemek icin `process_output()` methodu olan yeni bir plugin sinifi yazmak yeterlidir.

## Dosyalar Arasindaki Gelisim

- `ex0`: Temel processor yapisi kurulur.
- `ex1`: Processor'lar bir stream yoneticisi altinda birlestirilir.
- `ex2`: Stream'den cikan veriler plugin sistemiyle farkli formatlara aktarilir.

## Calistirma

```bash
python ex0/data_processor.py
python ex1/data_stream.py
python ex2/data_pipeline.py
```

## Dikkat Edilecek Noktalar

- `output()` bos liste uzerinde cagrilirsa `IndexError` olusabilir.
- `NumericProcessor`, `bool` degerlerini sayi olarak kabul etmemek icin `isinstance(data, int)` yerine `type(data) in (int, float)` kullanir. Cunku Python'da `bool`, `int` sinifinin alt turudur.
- `# type: ignore[override]` yorumlari, abstract method imzasi `Any` iken alt siniflarda daha dar tip kullanildigi icin mypy uyarilarini bastirmak amaciyla kullanilir.
- `.mypy_cache` klasoru mypy tarafindan uretilen gecici cache verisidir, kaynak kod degildir.
