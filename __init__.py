# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools

from .we_crease_from_seam import we_crease_from_seam
from .material_select import material_1d_select
from .subd_tool import subd_tool
from . import delaunay_1d_shot
from . import quad_bridge
from .drawing_split import drawing_split
from .edges_length import edges_length
from .height_painter import height_painter
from .retuber import retuber
from .stairs_sketcher import stairs_sketcher
from .vertical import vertical
from .vertical_vertices import vertical_vertices
from .vitragen import vitragen
from . import na_1d_tools_ui

bl_info = {
    'name': 'NA 1D Tools',
    'category': 'All',
    'author': 'Nikita Akimov, Paul Kotelevets',
    'version': (1, 0, 2),
    'blender': (2, 79, 0),
    'location': 'The 3D_View window - T-panel - NA 1D Tools',
    'wiki_url': 'https://github.com/Korchy/1d_na_tools',
    'tracker_url': 'https://github.com/Korchy/1d_na_tools',
    'description': 'NA 1D Tools'
}


def register():
    we_crease_from_seam.register(ui=False)
    material_1d_select.register(ui=False)
    subd_tool.register(ui=False)
    delaunay_1d_shot.register(ui=False)
    drawing_split.register(ui=False)
    edges_length.register(ui=False)
    height_painter.register(ui=False)
    stairs_sketcher.register(ui=False)
    retuber.register(ui=False)
    vitragen.register(ui=False)
    vertical_vertices.register(ui=False)
    vertical.register(ui=False)
    quad_bridge.register(ui=False)

    na_1d_tools_ui.register()


def unregister():
    na_1d_tools_ui.unregister()

    quad_bridge.unregister(ui=False)
    vertical.unregister(ui=False)
    vertical_vertices.unregister(ui=False)
    vitragen.unregister(ui=False)
    retuber.unregister(ui=False)
    stairs_sketcher.unregister(ui=False)
    height_painter.unregister(ui=False)
    edges_length.unregister(ui=False)
    drawing_split.unregister(ui=False)
    delaunay_1d_shot.unregister(ui=False)
    subd_tool.unregister(ui=False)
    material_1d_select.unregister(ui=False)
    we_crease_from_seam.unregister(ui=False)


if __name__ == "__main__":
    register()
