import folium
import pandas as pd
from folium.plugins import MarkerCluster


#convertir el archivo csv en un dataframe
data_frame=pd.read_csv('Book1.csv')
data_frame.columns = data_frame.columns.str.strip()
data_frame.head()

#n es la cantidad de datos que tiene en el Data frame
subset_of_df=data_frame.sample(n=28) 

#crear el mapara con los datos fracionado donde x = longitud y = latidtud 
some_map = folium.Map(location=[subset_of_df['x'].mean(), subset_of_df['y'].mean()],zoom_start=8)

#recorrer el closter e ir pintando las localidaddes
for row  in subset_of_df.itertuples():
    some_map.add_child(folium.Marker(location=[row.x,row.y],popup=row.municipio))

#guardar el erchivo para crear el mapa ext .html
some_map.save('C:\\Users\\Marlon\\Desktop\\proyecto1\\my-map.html')

#mapa 2 con el cluster
some_map2 = folium.Map(location=[subset_of_df['x'].mean(), subset_of_df['y'].mean()],zoom_start=8)

#de clarar el cluster
mc = MarkerCluster()

#recorrer el closter e ir pintando las localidaddes
for row  in subset_of_df.itertuples():
    mc.add_child(folium.Marker(location=[row.x,row.y],popup=row.municipio))

#asignarle al mapa al cluster 
some_map2.add_child(mc)

#guardar el archivo para crear el segundo mapa con el cluster ext .html
some_map2.save('C:\\Users\\Marlon\\Desktop\\proyecto1\\my-map2.html')