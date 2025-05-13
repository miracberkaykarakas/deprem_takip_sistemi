import requests
import pandas as pd
from bs4 import BeautifulSoup

def turkiye_deprem_verileri():
    url = "http://www.koeri.boun.edu.tr/scripts/lst8.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pre = soup.find("pre")

    if not pre:
        print("❌ Veri alınamadı.")
        return pd.DataFrame()

    satirlar = pre.text.strip().split("\n")[7:]
    veriler = []

    for satir in satirlar:
        elemanlar = satir.split()
        if len(elemanlar) >= 9:
            try:
                tarih = elemanlar[0]
                saat = elemanlar[1]
                enlem = float(elemanlar[2])
                boylam = float(elemanlar[3])
                derinlik = float(elemanlar[4])
                buyukluk = float(elemanlar[6])
                yer = " ".join(elemanlar[8:])
                zaman = pd.to_datetime(f"{tarih} {saat}")

                veriler.append({
                    "Yer": yer,
                    "Büyüklük": buyukluk,
                    "Zaman": zaman,
                    "Enlem": enlem,
                    "Boylam": boylam,
                    "Derinlik (km)": derinlik
                })
            except Exception as e:
                print(f"⚠️ Satır hatası: {e}")

    return pd.DataFrame(veriler)
