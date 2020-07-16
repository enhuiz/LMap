# LMap: A Map Marker Tool based on Amap

## Installation

```
$ pip install .
```

## Usage

```python
from lmap import LMap

lmap = LMap("My Markers")
lmap.add_marker(
    name="HKUST",
    long=114.268,
    lat=22.332,
    content="<button onclick=\"location.href='https://www.ust.hk/home'\">Details</button>",
)
lmap.render("index.html")
```

Open the index.html, you will get:

![](img/2020-07-16-21-38-43.png)
