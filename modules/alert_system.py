def alarm_kontrol(df, esik=6.0):
    ciddi_depremler = df[df["Büyüklük"] >= esik]
    if not ciddi_depremler.empty:
        print("⚠️ Uyarı! Büyük deprem(ler) tespit edildi:")
        print(ciddi_depremler[["Yer", "Büyüklük", "Zaman"]])
    else:
        print("✅ Şu an için büyük bir deprem yok.")
