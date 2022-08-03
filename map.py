import folium
import pandas as pd
import os

states = (os.path.join('data', 'us_states.json'))

m = folium.Map(location=[39.83, -98.58], zoom_start=3)

m.choropleth(
    geo_data=states,
    name='choropleth',
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.1,
    line_opacity=0.2,
)

folium.LayerControl().add_to(m)

m.save('maps/map.html')
