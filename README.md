# LMap: A simple map marker tool.

## Install

```
$ pip install .
```

## Example Usage

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
