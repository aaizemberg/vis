```sql
SELECT a.cod_dine, b.cod_dine
FROM ideign_departamentos as a, ideign_departamentos as b
WHERE a.cod_dine LIKE '02%' AND b.cod_dine LIKE '02%'
  AND ST_Touches(a.geom, b.geom)
  AND a.cod_dine < b.cod_dine
```
