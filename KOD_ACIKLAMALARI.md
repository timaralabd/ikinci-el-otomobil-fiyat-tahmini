# KOD AÇIKLAMALARI

## Proje: İkinci El Otomobil Fiyat Tahmin Sistemi

Bu dosyada projede kullanılan Python kodlarının görevleri ve önemli fonksiyonları açıklanmaktadır.

## 1. data_analysis.py – Veri Analizi

**Amaç:** Otomobil veri setinin yapısını incelemek, eksik ve tekrarlanan verileri kontrol etmek ve araç fiyatlarını analiz etmek.

### Kullanılan Kodlar

| Kod | Açıklama |
|---|---|
| `pd.read_csv()` | CSV dosyasındaki verileri okur. |
| `head()` | İlk 5 satırı gösterir. |
| `shape` | Satır ve sütun sayısını verir. |
| `columns.tolist()` | Sütun isimlerini listeler. |
| `info()` | Veri tiplerini ve genel bilgileri gösterir. |
| `isnull().sum()` | Eksik verileri sayar. |
| `duplicated().sum()` | Tekrarlanan kayıtları sayar. |
| `describe()` | Fiyatların istatistiksel özetini verir. |
| `sort_values()` | Araçları fiyatlarına göre sıralar. |
| `quantile()` | Fiyatların yüzdelik dağılımını hesaplar. |

### Sonuç

Bu dosya, veri setinin özelliklerini anlamamızı ve makine öğrenmesi öncesinde veri kalitesini değerlendirmemizi sağlar.
## 2. data_preprocessing.py – Veri Ön İşleme

**Amaç:** Veri setindeki eksik ve hatalı bilgileri temizlemek, fiyat ve kilometre değerlerini sayısal hâle getirerek verileri model eğitimine hazırlamak.

### Kullanılan Kodlar

| Kod | Açıklama |
|---|---|
| `pd.read_csv()` | Ham otomobil verilerini okur. |
| `str.replace()` | Fiyat ve kilometre bilgilerindeki sembolleri kaldırır. |
| `pd.to_numeric()` | Fiyat ve kilometre değerlerini sayıya dönüştürür. |
| `fillna("Bilinmiyor")` | Eksik kategorik bilgileri doldurur. |
| `dropna()` | Fiyat veya kilometre değeri eksik olan kayıtları siler. |
| `to_csv()` | Temizlenmiş verileri yeni bir CSV dosyasına kaydeder. |
| `shape` | Temizlenmiş veri setinin boyutunu gösterir. |
| `isnull().sum()` | Kalan eksik verileri kontrol eder. |
| `head()` | İlk 5 kaydı gösterir. |
| `dtypes` | Sütunların veri türlerini gösterir. |

### Sonuç

Bu dosya, ham otomobil verilerini temizleyerek `temizlenmis_arac_verileri.csv` dosyasını oluşturur ve makine öğrenmesi modelinin eğitimine uygun hâle getirir.
## 3. model_training.py – Makine Öğrenmesi Modelinin Eğitimi

**Amaç:** Temizlenmiş otomobil verilerini kullanarak Random Forest algoritmasıyla fiyat tahmin modeli oluşturmak, performansını değerlendirmek ve eğitilmiş modeli kaydetmek.

### Kullanılan Kodlar

| Kod | Açıklama |
|---|---|
| `pd.read_csv()` | Temizlenmiş otomobil verilerini okur. |
| `price >= 2000 & price <= 150000` | Belirlenen fiyat aralığındaki araçları seçer. |
| `drop(columns=["price"])` | Fiyat dışındaki özellikleri giriş verisi olarak belirler. |
| `train_test_split()` | Verileri %80 eğitim ve %20 test olarak ayırır. |
| `OneHotEncoder()` | Kategorik bilgileri modelin işleyebileceği sayısal biçime dönüştürür. |
| `ColumnTransformer()` | Kategorik ve sayısal sütunlara uygun ön işleme uygular. |
| `Pipeline()` | Ön işleme ve model eğitimini birleştirir. |
| `RandomForestRegressor()` | 100 karar ağacı kullanarak fiyat tahmin modeli oluşturur. |
| `model.fit()` | Modeli eğitim verileriyle eğitir. |
| `model.predict()` | Test verileri için fiyat tahmini yapar. |
| `mean_absolute_error()` | Tahminlerin ortalama mutlak hatasını hesaplar. |
| `r2_score()` | Modelin açıklama gücünü ölçer. |
| `joblib.dump()` | Eğitilmiş modeli `.pkl` dosyasına kaydeder. |

### Sonuç

Bu dosya, otomobil fiyatlarını tahmin eden makine öğrenmesi modelini eğitir, test verileri üzerinde değerlendirir ve `models/otomobil_fiyat_modeli.pkl` dosyasına kaydeder.
## 4. fiyat_tahmini.py – Araç Fiyat Tahmini

**Amaç:** Eğitilmiş makine öğrenmesi modelini kullanarak kullanıcının girdiği otomobil özelliklerine göre tahmini araç fiyatını hesaplamak.

### Kullanılan Kodlar

| Kod | Açıklama |
|---|---|
| `joblib.load()` | Önceden eğitilmiş fiyat tahmin modelini yükler. |
| `pd.read_csv()` | Temizlenmiş veri setini okur. |
| `drop(columns=["price"])` | Modelin kullandığı giriş sütunlarını belirler. |
| `input()` | Kullanıcıdan araç bilgilerini alır. |
| `int()` | Model yılı ve kilometre bilgilerini tam sayıya dönüştürür. |
| `pd.DataFrame()` | Girilen araç bilgilerini tablo biçimine dönüştürür. |
| `yeni_arac[ozellikler.columns]` | Giriş sütunlarını eğitim verisiyle aynı sıraya getirir. |
| `model.predict()` | Girilen araç özelliklerine göre fiyat tahmini yapar. |
| `print()` | Tahmini fiyatı USD cinsinden ekranda gösterir. |
| `if` | Tahmin eğitimde kullanılan fiyat aralığının dışındaysa uyarı verir. |

### Sonuç

Bu dosya, kullanıcıdan alınan araç bilgilerini eğitilmiş modele göndererek tahmini otomobil fiyatını USD cinsinden terminal ekranında gösterir.
## 5. arayuz.py – Kullanıcı Arayüzü

**Amaç:** Kullanıcının otomobil özelliklerini seçerek yapay zekâ modeli aracılığıyla tahmini araç fiyatını öğrenebileceği masaüstü arayüzünü oluşturmak.

### Kullanılan Kodlar

| Kod | Açıklama |
|---|---|
| `customtkinter` | Modern masaüstü kullanıcı arayüzünü oluşturur. |
| `Path()` | Veri seti ve model dosyalarının yollarını belirler. |
| `pd.read_csv()` | Araç bilgilerini içeren veri setini yükler. |
| `joblib.load()` | Eğitilmiş fiyat tahmin modelini yükler. |
| `CTk()` | Ana uygulama penceresini oluşturur. |
| `CTkScrollableFrame()` | Kaydırılabilir arayüz alanını oluşturur. |
| `CTkFrame()` | Bilgi, giriş ve sonuç kartlarını oluşturur. |
| `CTkComboBox()` | Araç özellikleri için seçim alanları oluşturur. |
| `CTkEntry()` | Kilometre bilgisinin girilmesini sağlar. |
| `modelleri_guncelle()` | Seçilen markaya göre araç modellerini günceller. |
| `fiyat_tahmin_et()` | Girilen bilgileri kontrol ederek fiyat tahminini gerçekleştirir. |
| `model.predict()` | Eğitilmiş model ile tahmini fiyatı hesaplar. |
| `messagebox` | Hatalı girişlerde veya belirli uyarı durumlarında kullanıcıyı bilgilendirir. |
| `CTkButton()` | Fiyat tahmin işlemini başlatan butonu oluşturur. |
| `mainloop()` | Uygulama penceresinin açık ve etkileşimli kalmasını sağlar. |

### Sonuç

Bu dosya, kullanıcıdan araç bilgilerini alır, eksik veya hatalı girişleri kontrol eder ve makine öğrenmesi modeliyle hesaplanan tahmini fiyatı USD cinsinden kullanıcı arayüzünde gösterir.