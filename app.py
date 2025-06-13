import streamlit as st
from db import init_db, rezervasyon_ekle
from datetime import date

st.set_page_config(page_title="VR Gözlük Rezervasyonu", layout="centered")
init_db()

st.title("🎮 VR Gözlük Rezervasyon Formu")

with st.form("rezervasyon_formu"):
    birim = st.text_input("Birim Adı", placeholder="Örn: Lise Kampı")
    etkinlik = st.text_input("Etkinlik Adı", placeholder="Örn: Bilim Günü")
    baslangic = st.date_input("Etkinlik Başlangıç Tarihi", min_value=date.today())
    bitis = st.date_input("Etkinlik Bitiş Tarihi", min_value=baslangic)
    gozluk = st.multiselect("Hangi Gözlük(ler)?", ["Meta Quest 3", "Meta Quest 3s"])

    submitted = st.form_submit_button("Rezervasyonu Kaydet")
    if submitted:
        if not (birim and etkinlik and gozluk):
            st.warning("Lütfen tüm alanları doldurun.")
        else:
            rezervasyon_ekle(birim, etkinlik, baslangic.isoformat(), bitis.isoformat(), ", ".join(gozluk))
            st.success("Rezervasyon kaydedildi!")
