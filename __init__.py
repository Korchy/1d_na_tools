# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools

from .we_crease_from_seam import we_crease_from_seam
from .material_select import material_1d_select
from .subd_tool import subd_tool
from . import delaunay_1d_shot
from .drawing_split import drawing_split
from .edges_length import edges_length
from . import na_1d_tools_ui

bl_info = {
    'name': 'NA 1D Tools',
    'category': 'All',
    'author': 'Nikita Akimov, Paul Kotelevets',
    'version': (1, 0, 0),
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

    na_1d_tools_ui.register()


def unregister():
    na_1d_tools_ui.unregister()

    edges_length.unregister(ui=False)
    drawing_split.unregister(ui=False)
    delaunay_1d_shot.unregister(ui=False)
    subd_tool.unregister(ui=False)
    material_1d_select.unregister(ui=False)
    we_crease_from_seam.unregister(ui=False)


if __name__ == "__main__":
    register()
