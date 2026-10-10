
import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path

import pandas as pd
import joblib


# ==================================================
# PROJE DOSYALARI
# ==================================================

PROJE_KLASORU = Path(__file__).resolve().parent.parent

VERI_YOLU = (
    PROJE_KLASORU
    / "data"
    / "temizlenmis_arac_verileri.csv"
)

MODEL_YOLU = (
    PROJE_KLASORU
    / "models"
    / "otomobil_fiyat_modeli.pkl"
)

# Veri setini ve eğitilmiş modeli yükleme
veriler = pd.read_csv(VERI_YOLU)
model = joblib.load(MODEL_YOLU)

sutunlar = veriler.drop(
    columns=["price"]
).columns.tolist()


# ==================================================
# RENKLER VE TASARIM
# ==================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ARKA_PLAN = "#F1F5F9"
BEYAZ = "#FFFFFF"
KART = "#FFFFFF"
ACIK_GRI = "#F8FAFC"
KENARLIK = "#E2E8F0"

MAVI = "#4F8DF7"
KOYU_MAVI = "#2563EB"
ACIK_MAVI = "#EFF6FF"

BASLIK = "#1E293B"
METIN = "#475569"
SOLUK_METIN = "#94A3B8"


# ==================================================
# ANA PENCERE
# ==================================================

pencere = ctk.CTk()

pencere.title(
    "İkinci El Otomobil Fiyat Tahmin Sistemi"
)

pencere.geometry("1100x800")
pencere.minsize(900, 650)
pencere.configure(fg_color=ARKA_PLAN)

# Pencere tamamen okunaklı kalır.
pencere.attributes("-alpha", 1.0)


# ==================================================
# KAYDIRILABİLİR ANA ALAN
# ==================================================

ana_alan = ctk.CTkScrollableFrame(
    pencere,
    fg_color=ARKA_PLAN,
    corner_radius=0
)

ana_alan.pack(
    fill="both",
    expand=True
)

icerik = ctk.CTkFrame(
    ana_alan,
    fg_color="transparent"
)

icerik.pack(
    fill="x",
    padx=35,
    pady=25
)


# ==================================================
# ÜST BAŞLIK
# ==================================================

ust_alan = ctk.CTkFrame(
    icerik,
    fg_color="transparent"
)

ust_alan.pack(
    fill="x",
    pady=(0, 20)
)

ctk.CTkLabel(
    ust_alan,
    text="OTOMOBİL FİYAT TAHMİNİ",
    font=("Segoe UI", 27, "bold"),
    text_color=BASLIK
).pack(anchor="w")

ctk.CTkLabel(
    ust_alan,
    text=(
        "Yapay zekâ destekli ikinci el "
        "otomobil fiyat tahmin sistemi"
    ),
    font=("Segoe UI", 13),
    text_color=METIN
).pack(
    anchor="w",
    pady=(5, 0)
)


# ==================================================
# BİLGİ KARTI
# ==================================================

bilgi_karti = ctk.CTkFrame(
    icerik,
    fg_color=ACIK_MAVI,
    corner_radius=16,
    border_width=1,
    border_color="#DBEAFE"
)

bilgi_karti.pack(
    fill="x",
    pady=(0, 20)
)

ctk.CTkLabel(
    bilgi_karti,
    text="🚘  Akıllı Araç Değerleme",
    font=("Segoe UI", 16, "bold"),
    text_color=KOYU_MAVI
).pack(
    anchor="w",
    padx=22,
    pady=(15, 4)
)

ctk.CTkLabel(
    bilgi_karti,
    text=(
        "Aracınızın özelliklerini seçin. "
        "Eğitilmiş makine öğrenmesi modeli "
        "tahmini satış fiyatını hesaplasın."
    ),
    font=("Segoe UI", 12),
    text_color=METIN,
    wraplength=850,
    justify="left"
).pack(
    anchor="w",
    padx=22,
    pady=(0, 15)
)


# ==================================================
# ARAÇ BİLGİLERİ KARTI
# ==================================================

form_karti = ctk.CTkFrame(
    icerik,
    fg_color=KART,
    corner_radius=20,
    border_width=1,
    border_color=KENARLIK
)

form_karti.pack(
    fill="x",
    pady=(0, 20)
)

form_baslik = ctk.CTkFrame(
    form_karti,
    fg_color="transparent"
)

form_baslik.pack(
    fill="x",
    padx=25,
    pady=(22, 5)
)

ctk.CTkLabel(
    form_baslik,
    text="Araç Bilgileri",
    font=("Segoe UI", 19, "bold"),
    text_color=BASLIK
).pack(anchor="w")

ctk.CTkLabel(
    form_baslik,
    text="Lütfen aşağıdaki alanları doldurun.",
    font=("Segoe UI", 11),
    text_color=SOLUK_METIN
).pack(
    anchor="w",
    pady=(3, 0)
)


# ==================================================
# ALAN BAŞLIKLARI
# ==================================================

etiketler = {
    "brand": "Marka",
    "model": "Model",
    "model_year": "Model Yılı",
    "milage": "Kilometre",
    "fuel_type": "Yakıt Türü",
    "engine": "Motor Özellikleri",
    "transmission": "Vites Türü",
    "ext_col": "Dış Renk",
    "int_col": "İç Renk",
    "accident": "Kaza Durumu",
    "clean_title": "Temiz Araç Belgesi"
}

giris_alanlari = {}


# ==================================================
# MARKAYA GÖRE MODEL GÜNCELLEME
# ==================================================

def modelleri_guncelle(secilen_marka=None):

    if secilen_marka is None:
        secilen_marka = giris_alanlari["brand"].get()

    modeller = sorted(
        veriler.loc[
            veriler["brand"] == secilen_marka,
            "model"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    model_alani = giris_alanlari["model"]

    model_alani.configure(
        values=modeller if modeller else [""]
    )

    if modeller:
        model_alani.set(modeller[0])
    else:
        model_alani.set("")


# ==================================================
# FORM ALANLARI
# ==================================================

form_alanlari = ctk.CTkFrame(
    form_karti,
    fg_color="transparent"
)

form_alanlari.pack(
    fill="x",
    padx=18,
    pady=(12, 25)
)

form_alanlari.grid_columnconfigure(
    0,
    weight=1,
    uniform="sutun"
)

form_alanlari.grid_columnconfigure(
    1,
    weight=1,
    uniform="sutun"
)


for sira, sutun in enumerate(sutunlar):

    sutun_no = sira % 2
    satir_no = sira // 2

    alan_kutusu = ctk.CTkFrame(
        form_alanlari,
        fg_color="transparent"
    )

    alan_kutusu.grid(
        row=satir_no,
        column=sutun_no,
        sticky="ew",
        padx=10,
        pady=9
    )

    ctk.CTkLabel(
        alan_kutusu,
        text=etiketler.get(sutun, sutun),
        font=("Segoe UI", 12, "bold"),
        text_color=METIN
    ).pack(
        anchor="w",
        pady=(0, 7)
    )

    if sutun == "milage":

        alan = ctk.CTkEntry(
            alan_kutusu,
            height=42,
            corner_radius=10,
            fg_color=ACIK_GRI,
            border_color=KENARLIK,
            border_width=1,
            text_color=BASLIK,
            font=("Segoe UI", 12),
            placeholder_text="Örn: 50000"
        )

        alan.insert(0, "50000")

    else:

        if sutun == "model":
            secenekler = [""]

        elif sutun == "model_year":
            secenekler = [
                str(int(yil))
                for yil in sorted(
                    veriler[sutun]
                    .dropna()
                    .unique()
                    .tolist(),
                    reverse=True
                )
            ]

        else:
            secenekler = sorted(
                veriler[sutun]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        alan = ctk.CTkComboBox(
            alan_kutusu,
            values=secenekler,
            height=42,
            corner_radius=10,
            fg_color=ACIK_GRI,
            border_color=KENARLIK,
            border_width=1,
            button_color="#DBEAFE",
            button_hover_color="#BFDBFE",
            dropdown_fg_color=BEYAZ,
            dropdown_text_color=BASLIK,
            text_color=BASLIK,
            font=("Segoe UI", 12),
            state="readonly"
        )

        if secenekler and secenekler[0]:
            alan.set(secenekler[0])

    alan.pack(fill="x")

    giris_alanlari[sutun] = alan


# Marka seçimine göre model listesini bağlama
giris_alanlari["brand"].configure(
    command=modelleri_guncelle
)

modelleri_guncelle()


# ==================================================
# FİYAT TAHMİN FONKSİYONU
# ==================================================

def fiyat_tahmin_et():

    try:
        yeni_arac = {}

        for sutun in sutunlar:

            deger = giris_alanlari[sutun].get().strip()

            if not deger:
                raise ValueError(
                    f"{etiketler.get(sutun, sutun)} "
                    "boş bırakılamaz."
                )

            if sutun in ["model_year", "milage"]:
                deger = int(deger)

            yeni_arac[sutun] = deger

        if yeni_arac["milage"] < 0:
            raise ValueError(
                "Kilometre negatif olamaz."
            )

        # Tahmin için araç tablosu oluşturma
        arac_tablosu = pd.DataFrame(
            [yeni_arac],
            columns=sutunlar
        )

        # Eğitilmiş modelden fiyat tahmini alma
        tahmini_fiyat = float(
            model.predict(arac_tablosu)[0]
        )

        # Sonucu ekranda gösterme
        sonuc_degeri.configure(
            text=f"${tahmini_fiyat:,.2f}"
        )

        sonuc_aciklama.configure(
            text="Tahmin başarıyla tamamlandı."
        )

        if (
            tahmini_fiyat < 2000
            or tahmini_fiyat > 150000
        ):
            messagebox.showwarning(
                "Uyarı",
                "Tahmin, modelin eğitim fiyat "
                "aralığı dışındadır."
            )

    except ValueError as hata:

        messagebox.showerror(
            "Giriş Hatası",
            str(hata)
        )

    except Exception as hata:

        messagebox.showerror(
            "Tahmin Hatası",
            str(hata)
        )


# ==================================================
# TAHMİN BUTONU
# ==================================================

tahmin_butonu = ctk.CTkButton(
    icerik,
    text="FİYAT TAHMİN ET  →",
    command=fiyat_tahmin_et,
    height=52,
    corner_radius=13,
    fg_color=MAVI,
    hover_color=KOYU_MAVI,
    text_color=BEYAZ,
    font=("Segoe UI", 15, "bold")
)

tahmin_butonu.pack(
    fill="x",
    pady=(0, 20)
)


# ==================================================
# SONUÇ KARTI
# ==================================================

sonuc_karti = ctk.CTkFrame(
    icerik,
    fg_color=BEYAZ,
    corner_radius=20,
    border_width=1,
    border_color=KENARLIK
)

sonuc_karti.pack(
    fill="x",
    pady=(0, 15)
)

ctk.CTkLabel(
    sonuc_karti,
    text="TAHMİNİ ARAÇ FİYATI",
    font=("Segoe UI", 12, "bold"),
    text_color=METIN
).pack(pady=(22, 6))

sonuc_degeri = ctk.CTkLabel(
    sonuc_karti,
    text="— USD",
    font=("Segoe UI", 34, "bold"),
    text_color=KOYU_MAVI
)

sonuc_degeri.pack(pady=(0, 6))

sonuc_aciklama = ctk.CTkLabel(
    sonuc_karti,
    text="Tahmin yapmak için araç bilgilerini girin.",
    font=("Segoe UI", 12),
    text_color=SOLUK_METIN
)

sonuc_aciklama.pack(pady=(0, 22))


# ==================================================
# ALT BİLGİ
# ==================================================

ctk.CTkLabel(
    icerik,
    text=(
        "Bu sistem makine öğrenmesi ile tahmini "
        "fiyat hesaplar. Sonuçlar USD cinsindendir "
        "ve kesin piyasa değeri değildir."
    ),
    font=("Segoe UI", 10),
    text_color=SOLUK_METIN,
    wraplength=850
).pack(pady=(5, 15))


# ==================================================
# UYGULAMAYI BAŞLATMA
# ==================================================

pencere.mainloop()
