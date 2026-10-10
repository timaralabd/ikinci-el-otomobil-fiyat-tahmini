# 🚗 İkinci El Otomobil Fiyat Tahmin Sistemi

## 📌 Proje Hakkında

Bu proje, ikinci el otomobillerin teknik ve fiziksel özelliklerini kullanarak tahmini satış fiyatlarını hesaplayan makine öğrenmesi tabanlı bir masaüstü uygulamasıdır.

Python ile geliştirilen sistem, araç bilgilerini analiz ederek **Random Forest Regression** algoritması aracılığıyla fiyat tahmini yapmaktadır.

## 🎯 Projenin Amacı

İkinci el otomobil fiyatlarının belirlenmesinde araç markası, modeli, üretim yılı, kilometresi, yakıt türü, motor özellikleri ve kaza durumu gibi faktörlerden yararlanarak tahmini fiyat hesaplayan bir sistem geliştirmektir.

## 🛠️ Kullanılan Teknolojiler

- **Python:** Programlama dili
- **Pandas:** Veri işleme ve temizleme
- **Scikit-learn:** Makine öğrenmesi ve model eğitimi
- **Random Forest Regressor:** Fiyat tahmin algoritması
- **Joblib:** Eğitilmiş modelin kaydedilmesi
- **CustomTkinter:** Modern masaüstü kullanıcı arayüzü

## 📊 Veri Seti

Projede Kaggle platformundan alınan **Used Car Price Prediction Dataset** kullanılmaktadır.

Veri seti 4.009 araç kaydından ve 12 sütundan oluşmaktadır.

Veri seti bağlantısı:

https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset

Veri ön işleme aşamasında eksik değerler düzenlenmiş, fiyat ve kilometre bilgileri sayısal verilere dönüştürülmüştür.

Model eğitiminde 2.000–150.000 USD fiyat aralığındaki 3.891 araç kaydı kullanılmıştır.

**Not:** Veri dosyaları boyut nedeniyle GitHub deposuna yüklenmemektedir.

## 🤖 Makine Öğrenmesi Modeli

Fiyat tahmini için Random Forest Regressor algoritması kullanılmıştır.

Veri seti %80 eğitim ve %20 test olarak ayrılmıştır.

Modelin filtrelenmiş test verileri üzerindeki sonuçları:

| Performans Ölçütü | Sonuç |
|---|---|
| MAE | 9.539,62 USD |
| R² Skoru | 0,6865 |

Bu sonuçlar filtrelenmiş veri setine aittir ve gerçek piyasa fiyatları için kesin doğruluk garantisi vermez.

## 🖥️ Masaüstü Arayüzü

CustomTkinter kullanılarak açık gri ve mavi tonlarında modern bir kullanıcı arayüzü geliştirilmiştir.

Kullanıcı araç markası, modeli, üretim yılı, kilometresi ve diğer özelliklerini seçerek tahmini satış fiyatını USD cinsinden görüntüleyebilir.

## 📁 Proje Yapısı

```text
ikinci-el-otomobil-fiyat-tahmini/
│
├── data/
│   ├── used_cars.csv
│   └── temizlenmis_arac_verileri.csv
│
├── models/
│   └── otomobil_fiyat_modeli.pkl
│
├── notebooks/
│
├── src/
│   ├── data_analysis.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── fiyat_tahmini.py
│   └── arayuz.py
│
├── README.md
├── .gitignore
└── requirements.txt
```

`data/` klasörü GitHub'da bulunmaz. Uygulamanın çalıştırılması için veri dosyalarının yerel bilgisayarda bulunması gerekir.

## 🚀 Kurulum ve Çalıştırma

**1. Projeyi klonlayın:**

```bash
git clone https://github.com/timaralabd/ikinci-el-otomobil-fiyat-tahmini.git
```

**2. Proje klasörüne geçin:**

```bash
cd ikinci-el-otomobil-fiyat-tahmini
```

**3. Gerekli kütüphaneleri yükleyin:**

```bash
python -m pip install pandas numpy scikit-learn joblib matplotlib customtkinter
```

**4. Veri dosyalarını hazırlayın:**

Kaggle veri setini indirip `data/used_cars.csv` konumuna yerleştirin.

Ardından veri ön işleme ve model eğitimi dosyalarını çalıştırın:

```bash
python src/data_preprocessing.py
python src/model_training.py
```

**5. Masaüstü arayüzünü başlatın:**

```bash
python src/arayuz.py
```

## 📌 Proje Durumu

- [x] Veri setinin seçilmesi
- [x] Veri analizi
- [x] Veri temizleme ve ön işleme
- [x] Makine öğrenmesi modelinin eğitilmesi
- [x] Model performansının değerlendirilmesi
- [x] Fiyat tahmin fonksiyonunun geliştirilmesi
- [x] Masaüstü kullanıcı arayüzünün oluşturulması
- [ ] Model performansının iyileştirilmesi
- [ ] Uygulamanın test edilmesi ve son düzenlemeler

## 👩‍💻 Proje Ekibi

Bu proje, üç kişilik bir Bilgisayar Mühendisliği öğrenci ekibi tarafından geliştirilmektedir.

## 📄 Açıklama

Bu uygulama eğitim amaçlı geliştirilmiştir. Tahmin edilen fiyatlar gerçek satış fiyatlarından farklı olabilir.
