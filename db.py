import sqlite3
from datetime import datetime

DB_PATH = "postgres.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS rezervasyon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            birim TEXT,
            etkinlik TEXT,
            baslangic TEXT,
            bitis TEXT,
            gozluk TEXT
        )
    """)
    conn.commit()
    conn.close()

def rezervasyon_ekle(birim, etkinlik, baslangic, bitis, gozluk):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO rezervasyon (birim, etkinlik, baslangic, bitis, gozluk) VALUES (?, ?, ?, ?, ?)",
              (birim, etkinlik, baslangic, bitis, gozluk))
    conn.commit()
    conn.close()

def rezervasyonlari_getir():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM rezervasyon")
    rows = c.fetchall()
    conn.close()
    return rows
