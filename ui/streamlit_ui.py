import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from modules.global_tracker import global_deprem_verileri
from modules.tr_tracker import turkiye_deprem_verileri

st.set_page_config(page_title="Deprem Takip Sistemi", layout="wide")
st.title("📡 Deprem Takip Sistemi")

secim = st.radio("Veri kaynağını seç:", ["Global (USGS)", "Türkiye (Kandilli)"])

if secim == "Global (USGS)":
    df = global_deprem_verileri()
else:
    df = turkiye_deprem_verileri()

st.write("Son 10 Deprem Kaydı")
st.dataframe(df.head(10))
