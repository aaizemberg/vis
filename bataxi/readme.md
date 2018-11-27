# subiendo el archivo bataxi.tsv a Postgresql

```SQL
CREATE TABLE bataxi
(
  id_viaje_r text,
  id_taxista_r text,
  fecha_inicio timestamp without time zone,
  fecha_fin timestamp without time zone,
  duracion numeric,
  origen_viaje_x numeric,
  origen_viaje_y numeric,
  destino_viaje_x numeric,
  destino_viaje_y numeric,
  cantidad_pasajeros numeric
);

COPY bataxi FROM '/tmp/bataxi.tsv' DELIMITER ',' CSV HEADER
```

# Generando un solo archivo de coordenadas (origen o destino)

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/aaizemberg/vis/gh-pages/bataxi/bataxi.csv")

df1 = df[['origen_viaje_x','origen_viaje_y']]
df1.columns = ['x', 'y']

df2 = df[['destino_viaje_x','destino_viaje_y']]
df2.columns = ['x', 'y']

df3 = pd.concat([df1, df2])

from google.colab import files
df3.to_csv('origen_y_destino.csv', index=False)
files.download('origen_y_destino.csv')
```

Algunas graficos que hice con este dataset:

1. http://bl.ocks.org/aaizemberg/7564a4523660cfa6554a9ee55ae5bbb5
2. https://twitter.com/aaizemberg/status/923252352072724480
3. https://bl.ocks.org/aaizemberg/raw/dfd9400061c3c4d03bb451002f0b4a72/
4. ....
