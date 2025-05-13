import requests
import pandas as pd

def global_deprem_verileri(min_magnitude=4.5):
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{min_magnitude}_day.geojson"
    response = requests.get(url)
    data = response.json()

    depremler = []
    for feature in data['features']:
        yer = feature['properties']['place']
        buyukluk = feature['properties']['mag']
        zaman = pd.to_datetime(feature['properties']['time'], unit='ms')
        koordinat = feature['geometry']['coordinates']

        depremler.append({
            'Yer': yer,
            'Büyüklük': buyukluk,
            'Zaman': zaman,
            'Enlem': koordinat[1],
            'Boylam': koordinat[0],
            'Derinlik (km)': koordinat[2]
        })

    return pd.DataFrame(depremler)
