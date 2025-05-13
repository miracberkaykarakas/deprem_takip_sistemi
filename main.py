from modules.global_tracker import global_deprem_verileri
from modules.tr_tracker import turkiye_deprem_verileri
from modules.map_display import haritada_goster
from modules.alert_system import alarm_kontrol

if __name__ == "__main__":
    print("📡 Deprem Takip Sistemi Başlatıldı\n")

    global_df = global_deprem_verileri()
    tr_df = turkiye_deprem_verileri()

    print("🌍 Son Global Depremler:")
    print(global_df.head(5), "\n")

    print("🇹🇷 Son Türkiye Depremleri:")
    print(tr_df.head(5), "\n")

    alarm_kontrol(global_df)
    haritada_goster(global_df)
