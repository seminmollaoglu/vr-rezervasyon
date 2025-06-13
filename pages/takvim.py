import streamlit as st
from db import rezervasyonlari_getir
import pandas as pd
from datetime import datetime, timedelta

st.title("📅 VR Gözlük Rezervasyon Takvimi")

data = rezervasyonlari_getir()

if not data:
    st.info("Henüz hiçbir rezervasyon yapılmamış.")
else:
    rezervasyon_listesi = []
    for id, birim, etkinlik, baslangic, bitis, gozluk in data:
        start_date = datetime.fromisoformat(baslangic).date()
        end_date = datetime.fromisoformat(bitis).date()
        days_range = pd.date_range(start=start_date, end=end_date)
        for day in days_range:
            rezervasyon_listesi.append({
                "Tarih": day,
                "Birim": birim,
                "Etkinlik": etkinlik,
                "Gözlük": gozluk
            })

    df = pd.DataFrame(rezervasyon_listesi)
    pivot = df.pivot_table(index="Tarih", aggfunc="first")

    st.dataframe(pivot)

