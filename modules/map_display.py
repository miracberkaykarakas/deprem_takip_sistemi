import folium
from folium.plugins import MarkerCluster

def haritada_goster(df, out_file="data/deprem_haritasi.html"):
    harita = folium.Map(location=[38.0, 35.0], zoom_start=3)
    marker_cluster = MarkerCluster().add_to(harita)

    for _, row in df.iterrows():
        popup = f"{row['Yer']}<br>Büyüklük: {row['Büyüklük']}<br>Zaman: {row['Zaman']}"
        folium.Marker(
            location=[row["Enlem"], row["Boylam"]],
            popup=popup
        ).add_to(marker_cluster)

    harita.save(out_file)
    print(f"🗺️ Harita oluşturuldu: {out_file}")
