import pandas as pd

# İkinci el otomobil veri setini okuma
veriler = pd.read_csv("data/used_cars.csv")

# Veri setindeki ilk 5 satırı görüntüleme
print("İlk 5 Araç Verisi:")
print(veriler.head())

# Veri setindeki satır ve sütun sayısını görüntüleme
print("\nVeri Setinin Boyutu:")
print(veriler.shape)

# Veri setindeki sütun adlarını görüntüleme
print("\nSütun Adları:")
print(veriler.columns.tolist())

# Veri seti hakkında genel bilgiler
print("\nVeri Seti Bilgileri:")
veriler.info()# Eksik verilerin sayısını kontrol etme
print("\nEksik Veri Sayıları:")
print(veriler.isnull().sum())

# Tekrarlanan kayıtları kontrol etme
print("\nTekrarlanan Kayıt Sayısı:")
print(veriler.duplicated().sum())

# Fiyat sütunundaki ilk 10 değeri görüntüleme
print("\nİlk 10 Araç Fiyatı:")
print(veriler["price"].head(10))# Temizlenmiş veri setini okuma
temiz_veriler = pd.read_csv("data/temizlenmis_arac_verileri.csv")

# Araç fiyatlarının istatistiksel analizi
print("\nFiyat İstatistikleri:")
print(temiz_veriler["price"].describe())

# En yüksek fiyatlı 10 aracı görüntüleme
print("\nEn Yüksek Fiyatlı 10 Araç:")
print(
    temiz_veriler[
        ["brand", "model", "model_year", "milage", "price"]
    ].sort_values(by="price", ascending=False).head(10)
)

# Fiyat dağılımını inceleme
print("\nFiyat Aralıkları:")
print(temiz_veriler["price"].quantile([0.25, 0.50, 0.75, 0.95, 0.99]))