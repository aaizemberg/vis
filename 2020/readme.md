# VEGA-spec

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "data": {"url": "https://raw.githubusercontent.com/aaizemberg/vis/gh-pages/2020/gartner.tsv"},
  "mark": {"type": "line", "point": true},
  "encoding": {
    "x": {
      "field": "x", "type": "quantitative", "axis": null,
        "scale": {"domain": [250,500]}
    },
    "y": {
      "field": "y1", "type": "quantitative", "axis":null,
        "scale": {"domain": [250,450]}
    },
    "order": {"field": "year", "type": "temporal"},
    "color": {"field": "product", "type": "nominal"}
  }
}
```
