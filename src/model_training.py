import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

# Temizlenmiş veri setini okuma
veriler = pd.read_csv("data/temizlenmis_arac_verileri.csv")

# Belirlenen fiyat aralığındaki araçları seçme
veriler = veriler[
    (veriler["price"] >= 2000) &
    (veriler["price"] <= 150000)
].copy()

print("Seçilen Araç Sayısı:", len(veriler))

# Girdi özellikleri ve hedef değişken
ozellikler = veriler.drop(columns=["price"])
hedef_fiyat = veriler["price"]

# Kategorik ve sayısal sütunları belirleme
kategorik_sutunlar = ozellikler.select_dtypes(
    include=["object", "str"]
).columns.tolist()

sayisal_sutunlar = ozellikler.select_dtypes(
    include=["number"]
).columns.tolist()

# Eğitim ve test verilerini ayırma
X_egitim, X_test, y_egitim, y_test = train_test_split(
    ozellikler,
    hedef_fiyat,
    test_size=0.20,
    random_state=42
)

# Kategorik özellikleri dönüştürme
on_isleme = ColumnTransformer([
    (
        "kategorik",
        OneHotEncoder(handle_unknown="ignore"),
        kategorik_sutunlar
    ),
    (
        "sayisal",
        "passthrough",
        sayisal_sutunlar
    )
])

# Random Forest regresyon modeli
model = Pipeline([
    ("on_isleme", on_isleme),
    ("regresyon", RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ))
])

# Modeli eğitme
print("Model eğitiliyor...")
model.fit(X_egitim, y_egitim)

# Tahminleri oluşturma
tahminler = model.predict(X_test)

# Performans sonuçları
print("\nModel Eğitimi Tamamlandı!")
print("Eğitim Veri Sayısı:", len(X_egitim))
print("Test Veri Sayısı:", len(X_test))
print(
    "Ortalama Mutlak Hata (USD):",
    round(mean_absolute_error(y_test, tahminler), 2)
)
print(
    "R² Değeri:",
    round(r2_score(y_test, tahminler), 4)
)# Eğitilmiş modeli kaydetme
Path("models").mkdir(exist_ok=True)

joblib.dump(model, "models/otomobil_fiyat_modeli.pkl")

print("\nModel başarıyla kaydedildi!")