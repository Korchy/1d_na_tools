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
from .edges_length.edges_length import EdgesLength
from .height_painter.height_painter import HeightPainter
from .material_select.material_1d_select import MaterialSelect
from .quad_bridge.quadbridge_panel import ui as quad_bridge_ui
from .retuber.retuber import Retuber
from .stairs_sketcher.stairs_sketcher import StairsSketcher
from .subd_tool.subd_tool import SubdTool
from .vertical.vertical import Vertical
from .vertical_vertices.vertical_vertices import VerticalVertices
from .vitragen.vitragen import Vitragen
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
	edges_length = BoolProperty(
		default=False
	)
	height_painter = BoolProperty(
		default=False
	)
	stairs_sketcher = BoolProperty(
		default=False
	)
	retuber = BoolProperty(
		default=False
	)
	vitragen = BoolProperty(
		default=False
	)
	vertical_vertices = BoolProperty(
		default=False
	)
	vertical_uv = BoolProperty(
		default=False
	)
	quad_bridge = BoolProperty(
		default=False
	)


class NA_1D_TOOLS_PT_panel(Panel):
	bl_idname = 'NA_1D_TOOLS_PT_panel'
	bl_label = 'NA 1D Tools'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = '1D'

	def draw(self, context):
		layout = self.layout
		# CONVERT
		convert_box = self.ui_section(
			layout=layout,
			context=context,
			prop='convert_section',
			label='CONVERT'
		)
		if context.scene.na_1d_tools_ui.convert_section:
			# We Crease from Seam
			self.ui_section(
				layout=convert_box,
				context=context,
				prop='we_crease_from_seam',
				label='We Crease from Seam',
				content_box=False
			)
			if context.scene.na_1d_tools_ui.we_crease_from_seam:
				WECFS.ui(layout=convert_box)

		# Material 1D Select
		box = self.ui_section(
			layout=layout,
			context=context,
			prop='material_select',
			label='Material 1D Select'
		)
		if context.scene.na_1d_tools_ui.material_select:
			MaterialSelect.ui(layout=box, context=context)

		# 1D Subd Storage
		box = self.ui_section(
			layout=layout,
			context=context,
			prop='subd_tool',
			label='1D Subd Storage'
		)
		if context.scene.na_1d_tools_ui.subd_tool:
			SubdTool.ui(layout=box)

		# EDIT TOOLS
		edit_tools_box = self.ui_section(
			layout=layout,
			context=context,
			prop='edit_section',
			label='EDIT TOOLS'
		)
		if context.scene.na_1d_tools_ui.edit_section:
			# Delaunay 1D Shot
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='delaunay_1d_shot',
				label='Delaunay 1D Shot 1.0.1'
			)
			if context.scene.na_1d_tools_ui.delaunay_1d_shot:
				delaunay_voronoi_1d_ui(
					layout=box,
					context=context
				)
			# Drawing Split
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='drawing_split',
				label='Drawing Split'
			)
			if context.scene.na_1d_tools_ui.drawing_split:
				DrawingSplit.ui(layout=box)
			# Edges Length
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='edges_length',
				label='Edges Length'
			)
			if context.scene.na_1d_tools_ui.edges_length:
				EdgesLength.ui(
					layout=box,
					context=context
				)
			# Height Painter
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='height_painter',
				label='Height Painter'
			)
			if context.scene.na_1d_tools_ui.height_painter:
				HeightPainter.ui(
					layout=box,
					context=context
				)
			# Stairs Sketcher
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='stairs_sketcher',
				label='Stairs Sketcher'
			)
			if context.scene.na_1d_tools_ui.stairs_sketcher:
				StairsSketcher.ui(layout=box)
			# Retuber
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='retuber',
				label='Retuber'
			)
			if context.scene.na_1d_tools_ui.retuber:
				Retuber.ui(layout=box)
			# Vitragen
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='vitragen',
				label='Vitragen'
			)
			if context.scene.na_1d_tools_ui.vitragen:
				Vitragen.ui(
					layout=box,
					context=context
				)
			# Vertical Vertices
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='vertical_vertices',
				label='Vertical Vertices'
			)
			if context.scene.na_1d_tools_ui.vertical_vertices:
				VerticalVertices.ui(
					layout=box,
					context=context
				)
			# Vertical
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='vertical_uv',
				label='Vertical UV'
			)
			if context.scene.na_1d_tools_ui.vertical_uv:
				Vertical.ui(
					layout=box,
					context=context
				)

		# Quad Bridge
		box = self.ui_section(
			layout=layout,
			context=context,
			prop='quad_bridge',
			label='Quad Bridge 0.8.0'
		)
		if context.scene.na_1d_tools_ui.quad_bridge:
			quad_bridge_ui(
				layout=box,
				context=context
			)

	@staticmethod
	def ui_section(layout, context, prop, label, content_box=True):
		# row = layout.row()
		icon = 'DOWNARROW_HLT' if getattr(context.scene.na_1d_tools_ui, prop) else 'RIGHTARROW'
		layout.prop(
			context.scene.na_1d_tools_ui,
			prop,
			icon=icon,
			text=label
		)
		if content_box and icon == 'DOWNARROW_HLT':
			box = layout.box().column(align=True)
			return box
		else:
			return layout


def register():
	register_class(NA_1D_TOOLS_UI)
	Scene.na_1d_tools_ui = PointerProperty(type=NA_1D_TOOLS_UI)
	register_class(NA_1D_TOOLS_PT_panel)


def unregister():
	unregister_class(NA_1D_TOOLS_PT_panel)
	del Scene.na_1d_tools_ui
	unregister_class(NA_1D_TOOLS_UI)
