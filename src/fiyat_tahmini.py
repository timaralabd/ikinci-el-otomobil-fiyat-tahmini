import pandas as pd
import joblib

# Eğitilmiş modeli yükleme
model = joblib.load("models/otomobil_fiyat_modeli.pkl")

# Veri setindeki özellikleri okuma
veriler = pd.read_csv("data/temizlenmis_arac_verileri.csv")

ozellikler = veriler.drop(columns=["price"])

print("İKİNCİ EL OTOMOBİL FİYAT TAHMİN SİSTEMİ")
print("---------------------------------------")

# Kullanıcıdan araç bilgilerini alma
marka = input("Araç Markası: ")
arac_modeli = input("Araç Modeli: ")
model_yili = int(input("Model Yılı: "))
kilometre = int(input("Kilometre: "))
yakit_turu = input("Yakıt Türü: ")
motor = input("Motor Özellikleri: ")
vites = input("Vites Türü: ")
dis_renk = input("Dış Renk: ")
ic_renk = input("İç Renk: ")
kaza = input("Kaza Durumu: ")
temiz_belge = input("Temiz Araç Belgesi: ")

# Kullanıcı bilgilerini tabloya dönüştürme
yeni_arac = pd.DataFrame([{
    "brand": marka,
    "model": arac_modeli,
    "model_year": model_yili,
    "milage": kilometre,
    "fuel_type": yakit_turu,
    "engine": motor,
    "transmission": vites,
    "ext_col": dis_renk,
    "int_col": ic_renk,
    "accident": kaza,
    "clean_title": temiz_belge
}])

# Sütun sıralamasını veri setiyle eşleştirme
yeni_arac = yeni_arac[ozellikler.columns]

# Fiyat tahmini yapma
tahmini_fiyat = model.predict(yeni_arac)[0]

print("\nTahmin Sonucu")
print("----------------------")
print(f"Tahmini Araç Fiyatı: {tahmini_fiyat:,.2f} USD")

if tahmini_fiyat < 2000 or tahmini_fiyat > 150000:
    print("Uyarı: Tahmin, modelin eğitim fiyat aralığı dışındadır.")