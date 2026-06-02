# Python File Handling

### **Ex00 için Bilinmesi Gerekenler**

- `file = open(file_name)` yaptığımız zaman dosyayı otomatik olarak **read** modunda açar.
- `file_content: str = file.read()` şeklinde tüm dosyadaki veriyi `str` olarak okur ve `file_content` değişkenine atarız.
- İşimiz bittikten sonra her dosyada olduğu gibi `file.close()` ile kapatırız. Kapatmazsak işletim sistemi seviyesinde dosya descriptor'ı açık kalır ve kaynak sızıntısına yol açar.

---

### **Ex01 için Bilinmesi Gerekenler**

- `recover_file(file_name: str) -> tuple[bool, str]` fonksiyonunda tuple içerisinde `bool` kullanmamızın sebebi işlemin başarılı olup olmadığını kontrol dahilinde tutmaktır. İkinci değer ise okunan içeriktir. Örneğin dosya açılamazsa `(False, "")`, başarılıysa `(True, content)` döner.
- `transform_data()` içindeki şu kontrol:

*python*

    `if content != "" and content[-1] != "\n":
        transformed += "#"`

Dosyaların son satırının newline ile **bitmeme** durumuna karşı yapılır. Yani **`"Merhaba\nDunya"`** gibi bir string döndüğünde `Dunya`'nın sonunda da `#` olmalıdır. Aynı zamanda içerik zaten `\n` ile bitiyorsa fazladan bir `#` eklenmesini de bu kontrol engeller.

- `save_data(file_name: str, content: str) -> None` fonksiyonu bir dosya adı ve içerik alır, içeriği dosyaya yazar. Burada `open(file_name, "w")` kullanırız çünkü amacımız **yazma** işlemidir. Örnek akış:

*python*

   `file = open("out.txt", "w")  # write modunda aç
    file.write("hello")          # içerik yaz
    file.close()                 # kapat`

### Ex2 İçin Bilinmesi Gerekenler: Python Çekirdeğindeki İletişim Kanalları (`sys`)

Python'da sistem seviyesindeki 3 temel iletişim kanalı `sys` kütüphanesi aracılığıyla erişilebilir hale gelir. Bunlar C'deki standart stream'lerin Python'daki karşılıklarıdır. ~ bunu yaparken claude’dan bilgilerimi ve yazdiklarimi duzenlemesi konusunda claude’dan yardim aldim

---

### 1. `sys.stdout` — Standart Çıktı

Açılımı **standard output**'tur. C'deki karşılıklarıyla kıyaslamak gerekirse:

- `sys.stdout.write()` → `write(1, ...)` gibi davranır, ham yazma işlemi yapar
- `print()` → `printf()` gibi davranır, biçimlendirme ve `\n` ekleme gibi kolaylıklar sağlar

Gerçekten de Python'daki `print()` fonksiyonunun iç implementasyonuna bakıldığında `sys.stdout.write()` çağırdığı görülür.

*python*

`sys.stdout.write("merhaba\n")  # ham yazma, \n otomatik gelmez
print("merhaba")               # \n otomatik eklenir, aynı sonuç`

---

### 2. `sys.stderr` — Standart Hata

Açılımı **standard error**'dır. C'de `write(2, ...)` ile `stderr`'e yazmaya eşdeğerdir. Mesajları normal çıktı kanalından **ayrı** bir hata kanalına gönderir, bu sayede program çıktısı ile hata mesajları birbirine karışmaz ve debug işlemi kolaylaşır.

*python*

`sys.stderr.write("Hata: dosya bulunamadı\n")

# ya da print ile:
print("Hata: dosya bulunamadı", file=sys.stderr)`

*bash*

# terminalde ikisini birbirinden ayırabilirsin:
`python script.py > cikti.txt 2> hatalar.txt
#                ^ stdout     ^ stderr`

---

### 3. `sys.stdin` — Standart Girdi

Açılımı **standard input**'tur. C'de `read(0, ...)` ile okumaya eşdeğerdir. Kullanıcıdan veya pipe'tan gelen veriyi okur.

python

`sys.stdin.readline()  # tek satır okur, \n dahil gelir` 

`*sys.stdin.readline.strip("\n")`  kullanarak sondaki newline'i silebilirdik*
`sys.stdin.read()      # EOF'a kadar tümünü okur`

`input()` fonksiyonu arka planda `sys.stdin`'i kullanır, fakat birkaç farkı vardır:

python

`input()              # \n'yi keser, EOF'ta EOFError fırlatır
sys.stdin.readline() # \n'yi kesmez, EOF'ta "" döner`

---

### Genel Karşılaştırma Tablosu

| Python | C karşılığı | FD | Yön |
| --- | --- | --- | --- |
| `sys.stdin` | `read(0, ...)` | `0` | Girdi |
| `sys.stdout` | `write(1, ...)` | `1` | Çıktı |
| `sys.stderr` | `write(2, ...)` | `2` | Hata çıktısı |

Bu üç kanal, işletim sisteminin her process'e varsayılan olarak açtığı stream'lerdir — Python bunları `sys` modülü üzerinden erişilebilir kılar.

#### Ex4 İçin Bilinmesi Gerekenler:

- `with open(file_name, "r") as archive_file: content = archive_file.read()`  bu kod sununla ayni isleve sahip
    
    `archive_file = open(file_name, "r")
    content = archive_file.read()
    archive_file.close()`
    

Zaten bunun disinda cok da onemli bir sey yok.