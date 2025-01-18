# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools

from . import delaunay_1d_shot
from . import quad_bridge
from .connect_loop import connect_loop
from .contour_sew import contour_sew
from .deloop import deloop
from .drawing_split import drawing_split
from .edges_length import edges_length
from .f2_snake import f2_snake
from .height_painter import height_painter
from .material_select import material_1d_select
from .planar_edges import planar_edges
from .retuber import retuber
from .rotten_rotation import rotten_rotation
from .slope_loop import slope_loop
from .stairs_sketcher import stairs_sketcher
from .subd_tool import subd_tool
from .vertical import vertical
from .vertical_vertices import vertical_vertices
from .vitragen import vitragen
from .we_crease_from_seam import we_crease_from_seam
from . import na_1d_tools_ui

bl_info = {
    'name': 'NA 1D Tools',
    'category': 'All',
    'author': 'Nikita Akimov, Paul Kotelevets',
    'version': (1, 4, 1),
    'blender': (2, 79, 0),
    'location': 'The 3D_View window - T-panel - NA 1D Tools',
    'wiki_url': 'https://github.com/Korchy/1d_na_tools',
    'tracker_url': 'https://github.com/Korchy/1d_na_tools',
    'description': 'NA 1D Tools'
}


def register():
    material_1d_select.register(ui=False)
    subd_tool.register(ui=False)
    connect_loop.register(ui=False)
    contour_sew.register(ui=False)
    delaunay_1d_shot.register(ui=False)
    deloop.register(ui=False)
    drawing_split.register(ui=False)
    edges_length.register(ui=False)
    f2_snake.register(ui=False)
    height_painter.register(ui=False)
    planar_edges.register(ui=False)
    slope_loop.register(ui=False)
    stairs_sketcher.register(ui=False)
    retuber.register(ui=False)
    rotten_rotation.register(ui=False)
    vitragen.register(ui=False)
    vertical_vertices.register(ui=False)
    vertical.register(ui=False)
    quad_bridge.register(ui=False)
    we_crease_from_seam.register(ui=False)

    na_1d_tools_ui.register()


def unregister():
    na_1d_tools_ui.unregister()

    we_crease_from_seam.unregister(ui=False)
    quad_bridge.unregister(ui=False)
    vertical.unregister(ui=False)
    vertical_vertices.unregister(ui=False)
    vitragen.unregister(ui=False)
    rotten_rotation.unregister(ui=False)
    retuber.unregister(ui=False)
    stairs_sketcher.unregister(ui=False)
    slope_loop.unregister(ui=False)
    planar_edges.unregister(ui=False)
    height_painter.unregister(ui=False)
    f2_snake.unregister(ui=False)
    edges_length.unregister(ui=False)
    drawing_split.unregister(ui=False)
    deloop.unregister(ui=False)
    delaunay_1d_shot.unregister(ui=False)
    contour_sew.unregister(ui=False)
    connect_loop.unregister(ui=False)
    subd_tool.unregister(ui=False)
    material_1d_select.unregister(ui=False)


if __name__ == "__main__":
    register()
