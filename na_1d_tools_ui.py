# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools


from bpy.props import BoolProperty
from bpy.types import Panel, Scene
from bpy.utils import register_class, unregister_class
from .we_crease_from_seam.we_crease_from_seam import WECFS


class NA_1D_TOOLS_PT_panel(Panel):
	bl_idname = 'NA_1D_TOOLS_PT_panel'
	bl_label = 'NA 1D Tools'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'NA 1D TOOLS'

	def draw(self, context):
		layout = self.layout
		# CONVERT
		self.ui_section(
			layout=layout,
			context=context,
			prop='na_1d_tools_opts_ui_convert_section',
			label='CONVERT'
		)
		if context.scene.na_1d_tools_opts_ui_convert_section:
			# we crease from seam
			WECFS.ui(layout=layout)
		# Material 1D Select
		

		# EDIT TOOLS
		self.ui_section(
			layout=layout,
			context=context,
			prop='na_1d_tools_opts_ui_edit_section',
			label='EDIT TOOLS'
		)
		if context.scene.na_1d_tools_opts_ui_edit_section:
			# we crease from seam
			# WECFS.ui(layout=layout)
			pass

	@staticmethod
	def ui_section(layout, context, prop, label):
		row = layout.row()
		icon = 'TRIA_DOWN' if getattr(context.scene, prop) else 'TRIA_RIGHT'
		row.prop(
			context.scene,
			prop,
			icon=icon,
			text=label
		)


def register():
	Scene.na_1d_tools_opts_ui_convert_section = BoolProperty(
		default=False
	)
	Scene.na_1d_tools_opts_ui_edit_section = BoolProperty(
		default=False
	)
	register_class(NA_1D_TOOLS_PT_panel)


def unregister():
	unregister_class(NA_1D_TOOLS_PT_panel)
	del Scene.na_1d_tools_opts_ui_edit_section
	del Scene.na_1d_tools_opts_ui_convert_section
