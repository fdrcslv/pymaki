from xml.dom import minidom
import os, inspect

class MakiIcon(object):
    """docstring for MakiIcon."""
    package = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    folder = 'svg'
    color = 'rgb(115,134,154)'
    sizes = dict(
        big=15,
        small=11
    )

    def __init__(self, name, sizeclass='big', *args, **kw):
        super(MakiIcon, self).__init__()
        self.name = name
        self.sizeclass = sizeclass
        self.tail = '{}-{}.svg'.format(name, self.sizes[sizeclass])
        self.size = kw.get('size', False)
        self.svg = self.get_svg()

    def get_svg(self):
        with open(os.path.join(self.package, self.folder, self.tail)) as file:
            svg = minidom.parse(file)
        return svg.firstChild

    def get_icon(self):
        self.set_size()
        self.set_color()
        return self.svg.toxml()

    def set_size(self):
        if self.size:
            s = '{}px'.format(self.size)
            self.svg.attributes['height'].nodeValue = s
            self.svg.attributes['width'].nodeValue = s

    def set_color(self):
        self.svg.setAttribute('fill', self.color)
