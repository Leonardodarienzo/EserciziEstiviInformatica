from flask import Flask, render_template, request
import shapely
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
import os
import folium
import geopandas as gpd
import random


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
     return render_template("home.html")


@app.route('/Scelta1', methods=['GET'])
def Scelta1():
     df = pd.read_excel('GdL_GV_2021.xlsx')
     df_giudizio = df.groupby("giudizio")[["localita"]].count().reset_index()
     giudizio = list(df_giudizio["giudizio"])
     numero = list(df_giudizio["localita"])
     return render_template("scelta1.html", numero=numero, prova = df_giudizio.to_html())

@app.route('/Scelta2', methods=['GET'])
def Scelta2():
    df = pd.read_excel('GdL_GV_2021.xlsx')

    giudizi = df['giudizio'].value_counts(normalize=True) * 100
    
    return render_template('scelta2.html', giudizi=giudizi)


@app.route('/Scelta3', methods=['GET'])
def Scelta3():
    df = pd.read_excel('GdL_GV_2021.xlsx')
    tipo_inquinamento_counts = df['giudizio'].value_counts(normalize=True) * 100

     
    plt.figure(figsize=(6, 4))
    plt.pie(tipo_inquinamento_counts, labels=tipo_inquinamento_counts.index, autopct='%1.1f%%')
    plt.title('Percentuale dei Tipi di Inquinamento')

    dir = "static/images"
    file_name = "graf3.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi=150)

    plt.show()

    return render_template('scelta3.html')


@app.route('/Scelta4', methods=['GET'])
def Scelta4():
    df = pd.read_excel('GdL_GV_2021.xlsx')
    
    localita_con_spiaggia = df[df['localita'].str.lower().str.contains('spiaggia', na=False, case=False)]['giudizio']
    
    localita_con_spiaggia = localita_con_spiaggia.drop_duplicates()
    
    return render_template("scelta4.html", localita_con_spiaggia=localita_con_spiaggia)


@app.route('/Scelta5', methods=['GET'])
def Scelta5():
    df = pd.read_excel('GdL_GV_2021.xlsx')
    gdf = gpd.GeoDataFrame(df.drop(['longitude', 'latitude'], axis=1),
          crs='EPSG:4326',
          geometry=df.apply(lambda row: shapely.geometry.Point((row.longitude, row.latitude)), axis=1))

    mappa = folium.Map(location=[45.706, 9.742], zoom_start=8)

    for idx, row in gdf.iterrows():
        folium.Marker([row['geometry'].y, row['geometry'].x], tooltip=row['localita']).add_to(mappa)

    mappa_html = mappa.get_root().render()

    return render_template("scelta5.html", mappa_html=mappa_html, gdf=gdf)



@app.route('/Scelta6', methods=['GET'])
def scelta6():
    df = pd.read_excel('GdL_GV_2021.xlsx')
    num_punti = 10  
    punti = []

    for _ in range(num_punti):
        latitude = random.uniform(45.0, 46.0)
        longitude = random.uniform(9.0, 10.0)
        giudizio = random.choice(['Entro i Limiti', 'Inquinato', 'Fortemente Inquinato'])
        punti.append({'Latitude': latitude, 'Longitude': longitude, 'Giudizio': giudizio})

    mappa = folium.Map(location=[45.4, 9.2], zoom_start=8)

    for punto in punti:
        folium.Marker(
            location=[punto['Latitude'], punto['Longitude']],
            popup='Giudizio: ' + punto['Giudizio']
        ).add_to(mappa)
    mappa.save('templates/mappa.html')

    return render_template('mappa.html')


@app.route('/Scelta7', methods=['GET', 'POST'])
def Scelta7():
    if request.method == 'POST':
        nome_regione = request.form['nome_regione']
        
        punti_monitorati = pd.DataFrame({
            'Latitude': [45.7, 45.71, 45.72],
            'Longitude': [9.2, 9.21, 9.22],
            'Giudizio': ['Entro i Limiti', 'Inquinato', 'Fortemente Inquinato']
        })

        mappa = folium.Map(location=[45.7, 9.2], zoom_start=10)
        
        for _, punto in punti_monitorati.iterrows():
            folium.Marker(
                location=[punto['Latitude'], punto['Longitude']],
                popup='Giudizio: ' + punto['Giudizio']
            ).add_to(mappa)
        
        mappa.save('templates/mappa_regionale.html')

        return render_template('mappa_regionale.html')

    return render_template('scelta7.html')

@app.route('/Scelta8', methods=['GET', 'POST'])
def Scelta8():
    if request.method == 'POST':
        nome_lago = request.form['nome_lago'] 

        punti_monitorati2 = pd.DataFrame({
            'Latitude': [45.57, 45.96, 46.01],
            'Longitude': [10, 8.65, 9.25],
            'Giudizio': ['Entro i Limiti', 'Inquinato', 'Fortemente Inquinato']
        })

        mappa = folium.Map(location=[45.7, 9.2], zoom_start=10)

        
        for _, punto in punti_monitorati2.iterrows():
            folium.Marker(
                location=[punto['Latitude'], punto['Longitude']],
                popup='Giudizio: ' + punto['Giudizio']
            ).add_to(mappa)

        mappa.save('templates/mappa_lago.html')

        return render_template('mappa_lago.html')
    
    return render_template('scelta8.html')



@app.route('/Scelta9', methods=['GET'])
def Scelta9():
     return render_template("home.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)