# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools


from bpy.types import Panel
from bpy.utils import register_class, unregister_class
from .we_crease_from_seam.we_crease_from_seam import WECFS


class NA_1D_TOOLS_PT_panel(Panel):
	bl_idname = 'NA_1D_TOOLS_PT_panel'
	bl_label = 'NA 1D Tools'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'NA 1D TOOLS'

	def draw(self, context):
		WECFS.ui(layout=self.layout)


def register():
	register_class(NA_1D_TOOLS_PT_panel)


def unregister():
	unregister_class(NA_1D_TOOLS_PT_panel)
