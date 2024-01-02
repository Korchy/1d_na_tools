# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools

from .we_crease_from_seam import we_crease_from_seam
from .material_select import material_1d_select
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
    na_1d_tools_ui.register()


def unregister():
    na_1d_tools_ui.unregister()
    material_1d_select.unregister(ui=False)
    we_crease_from_seam.unregister(ui=False)


if __name__ == "__main__":
    register()
