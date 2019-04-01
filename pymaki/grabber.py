from xml.dom import minidom
import os, inspect

class MakiIcon(object):
    """docstring for MakiIcon."""
    package = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    folder = 'svg'
    sizes = dict(
        big=15,
        small=11
    )
    scales = dict(
        big=1,
        small=1.5
    )

    def __init__(self, name, sizeclass='big', *args, **kw):
        super(MakiIcon, self).__init__()
        self.name = name
        self.sizeclass = sizeclass
        self.tail = '{}-{}.svg'.format(name, self.sizes[sizeclass])
        self.size = kw.get('size', False)
        self.color = kw.get('color', 'rgb(117, 117, 117)')
        self.svg = self.get_svg()
        self.path = self.svg.getElementsByTagName('path')[0]

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

    def __str__(self):
        return self.get_icon()

    __repr__ = __str__

    def get_path(self, translate=[40, -7.5], color='rgb(57, 57, 57)'):
        scale = self.scales[self.sizeclass]
        self.path.attributes['transform'] = 'translate({}, {}) scale({scale})'.format(*translate, scale=scale)
        self.path.attributes['fill'] = color
        return self.path.toxml()
