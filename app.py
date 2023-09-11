from flask import Flask, render_template
from geopandas import GeoDataFrame
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
import os
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
    giudizi = df['giudizio'].value_counts(normalize=True) * 100
    labels = df['localita']
    dati = df['giudizio']
    fig, ax = plt.subplots(figsize=(10,8))
    ax.bar(labels, dati, label='numero di luoghi per ogni inquinamento')
    ax.set_ylabel('localita')
    ax.set_title('luoghi per ogni inquinamento')
    ax.set_xticklabels(labels) 
    ax.legend()
    
    plt.figure(figsize=(22, 10))
    plt.pie(dati, labels=labels, autopct='%1.1f%%')
    dir = "static/images"
    file_name = "graf3.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 150)

    return render_template('scelta3.html', giudizi=giudizi)


@app.route('/Scelta4', methods=['GET'])
def Scelta4():
    df = pd.read_excel('GdL_GV_2021.xlsx')
    localita_con_spiaggia = df[df['localita'].str.contains('spiaggia', case=False)]['giudizio']
    
    return render_template("scelta4.html",localita_con_spiaggia=localita_con_spiaggia)


@app.route('/Scelta5', methods=['GET'])
def Scelta5():
     return render_template("home.html")


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