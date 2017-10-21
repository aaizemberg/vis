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

COPY bataxi FROM '/tmp/bataxi.csv' DELIMITER ';' CSV HEADER
```
