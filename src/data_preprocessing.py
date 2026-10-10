import pandas as pd

# Veri setini okuma
veriler = pd.read_csv("data/used_cars.csv")

# Fiyat sütununu sayısal değere dönüştürme
veriler["price"] = (
    veriler["price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

veriler["price"] = pd.to_numeric(veriler["price"], errors="coerce")

# Kilometre sütununu sayısal değere dönüştürme
veriler["milage"] = (
    veriler["milage"]
    .str.replace(" mi.", "", regex=False)
    .str.replace(",", "", regex=False)
)

veriler["milage"] = pd.to_numeric(veriler["milage"], errors="coerce")

# Eksik kategorik verileri doldurma
veriler["fuel_type"] = veriler["fuel_type"].fillna("Bilinmiyor")
veriler["accident"] = veriler["accident"].fillna("Bilinmiyor")
veriler["clean_title"] = veriler["clean_title"].fillna("Bilinmiyor")

# Sayısal dönüşüm sonucunda oluşabilecek eksik kayıtları çıkarma
veriler = veriler.dropna(subset=["price", "milage"])

# Temizlenen veri setini kaydetme
veriler.to_csv("data/temizlenmis_arac_verileri.csv", index=False)

# Sonuçları görüntüleme
print("Veri temizleme işlemi tamamlandı!")

print("\nTemizlenmiş Veri Seti Boyutu:")
print(veriler.shape)

print("\nEksik Veri Sayıları:")
print(veriler.isnull().sum())

print("\nİlk 5 Araç Verisi:")
print(veriler.head())

print("\nVeri Türleri:")
print(veriler.dtypes)