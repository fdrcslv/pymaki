from xml.dom import minidom
import os, inspect

def get_data():
    with open(os.path.join(__file__, "rating.json")) as f:
        o = json.load(f)
    return o


class MakiIcon(object):
    """docstring for MakiIcon."""
    package = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    svg = 'svg'

    def __init__(self, name, sizeclass=15):
        super(MakiIcon, self).__init__()
        self.name = name
        self.sizeclass = sizeclass
        self.tail = '{}-{}.svg'.format(name, sizeclass)

    def get_svg(self):
        with open(os.path.join(self.package, self.svg, self.tail)) as file:
            svg = minidom.parse(file)
        return svg
