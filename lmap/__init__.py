import re
from pathlib import Path

template_dir = Path(Path(__file__).parent, "template")


def fill(template, **kwargs):
    for placeholder in re.findall(r"({%.+?%})", template):
        key = placeholder.split("%")[1].strip()
        if key in kwargs:
            template = template.replace(placeholder, str(kwargs[key]))
    return template


def load_template(filename, **kwargs):
    with open(Path(template_dir, filename), "r") as f:
        template = f.read()
    return fill(template, **kwargs)


class LMap:
    def __init__(self, title):
        self._title = title
        self.reset()

    @property
    def title(self):
        return self._title

    def reset(self):
        self.body = load_template("body.html", title=self.title)
        self.markers = []

    def add_marker(self, name, long, lat, content):
        m = load_template("marker.js", name=name, long=long, lat=lat, content=content)
        self.markers.append(m)

    def render(self, path):
        with open(path, "w") as f:
            f.write(str(self))

    def __str__(self):
        return fill(self.body, markers="\n\n".join(self.markers))
