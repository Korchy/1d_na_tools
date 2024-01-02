# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools


from bpy.props import BoolProperty, PointerProperty
from bpy.types import Panel, PropertyGroup, Scene
from bpy.utils import register_class, unregister_class
from .delaunay_1d_shot.delaunay_voronoi_1d_panel import ui as delaunay_voronoi_1d_ui
from .drawing_split.drawing_split import DrawingSplit
from .material_select.material_1d_select import MaterialSelect
from .subd_tool.subd_tool import SubdTool
from .we_crease_from_seam.we_crease_from_seam import WECFS


# UI
class NA_1D_TOOLS_UI(PropertyGroup):
	# sections
	convert_section = BoolProperty(
		default=False
	)
	edit_section = BoolProperty(
		default=False
	)
	# modules
	we_crease_from_seam = BoolProperty(
		default=False
	)
	material_select = BoolProperty(
		default=False
	)
	subd_tool = BoolProperty(
		default=False
	)
	delaunay_1d_shot = BoolProperty(
		default=False
	)
	drawing_split = BoolProperty(
		default=False
	)


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
			prop='convert_section',
			label='CONVERT'
		)
		if context.scene.na_1d_tools_ui.convert_section:
			# We Crease from Seam
			self.ui_section(
				layout=layout,
				context=context,
				prop='we_crease_from_seam',
				label='We Crease from Seam'
			)
			if context.scene.na_1d_tools_ui.we_crease_from_seam:
				WECFS.ui(layout=layout)

		# Material 1D Select
		self.ui_section(
			layout=layout,
			context=context,
			prop='material_select',
			label='Material 1D Select'
		)
		if context.scene.na_1d_tools_ui.material_select:
			MaterialSelect.ui(layout=layout, context=context)

		# 1D Subd Storage
		self.ui_section(
			layout=layout,
			context=context,
			prop='subd_tool',
			label='1D Subd Storage'
		)
		if context.scene.na_1d_tools_ui.subd_tool:
			SubdTool.ui(layout=layout)

		# EDIT TOOLS
		self.ui_section(
			layout=layout,
			context=context,
			prop='edit_section',
			label='EDIT TOOLS'
		)
		if context.scene.na_1d_tools_ui.edit_section:
			# Delaunay 1D Shot
			self.ui_section(
				layout=layout,
				context=context,
				prop='delaunay_1d_shot',
				label='Delaunay 1D Shot'
			)
			if context.scene.na_1d_tools_ui.delaunay_1d_shot:
				delaunay_voronoi_1d_ui(
					layout=layout,
					context=context
				)
			# Drawing Split
			self.ui_section(
				layout=layout,
				context=context,
				prop='drawing_split',
				label='Drawing Split'
			)
			if context.scene.na_1d_tools_ui.drawing_split:
				DrawingSplit.ui(layout=layout)

	@staticmethod
	def ui_section(layout, context, prop, label):
		row = layout.row()
		icon = 'TRIA_DOWN' if getattr(context.scene.na_1d_tools_ui, prop) else 'TRIA_RIGHT'
		row.prop(
			context.scene.na_1d_tools_ui,
			prop,
			icon=icon,
			text=label
		)


def register():
	register_class(NA_1D_TOOLS_UI)
	Scene.na_1d_tools_ui = PointerProperty(type=NA_1D_TOOLS_UI)
	register_class(NA_1D_TOOLS_PT_panel)


def unregister():
	unregister_class(NA_1D_TOOLS_PT_panel)
	del Scene.na_1d_tools_ui
	unregister_class(NA_1D_TOOLS_UI)
