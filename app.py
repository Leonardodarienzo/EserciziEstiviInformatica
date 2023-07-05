from flask import Flask, render_template
from geopandas import GeoDataFrame
from shapely.geometry import Point
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
     return render_template("home.html")


@app.route('/Scelta1', methods=['GET'])
def Scelta1():
     return render_template("home.html")

@app.route('/Scelta2', methods=['GET'])
def Scelta2():
     return render_template("home.html")


@app.route('/Scelta3', methods=['GET'])
def Scelta3():
     return render_template("home.html")


@app.route('/Scelta4', methods=['GET'])
def Scelta4():
     return render_template("home.html")


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