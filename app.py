from flask import Flask
import folium
import map


app = Flask(__name__)


@app.route('/')
def index():
    folium_map = map.m
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
