from flask import Flask, render_template
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
import os
import folium
import pandas as gpd
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
    df1 = pd.read_excel('GdL_GV_2021.xlsx')
    localita_con_spiaggia = df1[df1['localita'].str.lower().str.contains('spiaggia', na=False, case=False)]
    geometry1 = [Point(xy) for xy in zip(localita_con_spiaggia['longitude'], localita_con_spiaggia['latitude'])]
    gdf1 = gpd.GeoDataFrame(localita_con_spiaggia, geometry=geometry1)
    gdf1.crs = 'EPSG:4326'

    gdf_totale = gpd.GeoDataFrame(pd.concat([gdf1, gdf2, gdf3], ignore_index=True), crs=gdf1.crs)
    
    mappa = folium.Map(location=[45.706, 9.742], zoom_start=8)
    
    for idx, row in gdf_totale.iterrows():
        folium.Marker([row['geometry'].y, row['geometry'].x], tooltip=row['localita']).add_to(mappa)
    
    mappa_html = mappa.get_root().render()
    
    return render_template("scelta5.html", risultato_totale=gdf_totale, mappa_html=mappa_html)



@app.route('/Scelta6', methods=['GET'])
def Scelta6():
     return render_template("home.html")



@app.route('/Scelta7', methods=['GET'])
def Scelta7():
     return render_template("home.html")


@app.route('/Scelta8', methods=['GET'])
def Scelta8():
     return render_template("home.html")


@app.route('/Scelta9', methods=['GET'])
def Scelta9():
     return render_template("home.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)