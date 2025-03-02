# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools


from bpy.props import BoolProperty, PointerProperty
from bpy.types import Panel, PropertyGroup, Scene
from bpy.utils import register_class, unregister_class
from .connect_loop.connect_loop import ConnectLoop
from .contour_sew.contour_sew import ContourSew
from .delaunay_1d_shot.delaunay_voronoi_1d_panel import ui as delaunay_voronoi_1d_ui
from .deloop.deloop import Deloop
from .drawing_split.drawing_split import DrawingSplit
from .edges_length.edges_length import EdgesLength
from .f2_snake.f2_snake import F2Snake
from .height_painter.height_painter import HeightPainter
from .import_lst.import_lst import ImportLST
from .material_select.material_1d_select import MaterialSelect
from .na_1d_tools_misc.na_1d_tools_misc import NA1DToolsMisc
from .quad_bridge.quadbridge_panel import ui as quad_bridge_ui
from .retuber.retuber import Retuber
from .rotten_rotation.rotten_rotation import RottenRotation
from .planar_edges.planar_edges import Planar
from .slope_loop.slope_loop import SlopeLoop
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
	gplan_section = BoolProperty(
		default=False
	)
	# modules
	connect_loop = BoolProperty(
		default=False
	)
	contour_sew = BoolProperty(
		default=False
	)
	we_crease_from_seam = BoolProperty(
		default=False
	)
	material_select = BoolProperty(
		default=False
	)
	na_1d_tools_misc = BoolProperty(
		default=False
	)
	subd_tool = BoolProperty(
		default=False
	)
	delaunay_1d_shot = BoolProperty(
		default=False
	)
	deloop = BoolProperty(
		default=False
	)
	drawing_split = BoolProperty(
		default=False
	)
	edges_length = BoolProperty(
		default=False
	)
	f2_snake = BoolProperty(
		default=False
	)
	height_painter = BoolProperty(
		default=False
	)
	import_lst = BoolProperty(
		default=False
	)
	planar_edges = BoolProperty(
		default=False
	)
	slope_loop = BoolProperty(
		default=False
	)
	stairs_sketcher = BoolProperty(
		default=False
	)
	retuber = BoolProperty(
		default=False
	)
	rotten_rotation = BoolProperty(
		default=False
	)
	unnegative_scale = BoolProperty(
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
			label='Material 1D Select',
			align=False
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
			# F2 Snake
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='f2_snake',
				label='F2 Snake'
			)
			if context.scene.na_1d_tools_ui.f2_snake:
				F2Snake.ui(
					layout=box,
					context=context
				)
			# Rotten Rotation
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='rotten_rotation',
				label='Rotten Rotation'
			)
			if context.scene.na_1d_tools_ui.rotten_rotation:
				RottenRotation.ui(
					layout=box,
					context=context
				)
			# Unnegative Scale
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='unnegative_scale',
				label='Unnegative Scale'
			)
			if context.scene.na_1d_tools_ui.unnegative_scale:
				RottenRotation.ui(
					layout=box,
					context=context
				)
			# NA 1D Tools Misc
			box = self.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='na_1d_tools_misc',
				label='Misc',
				align=False
			)
			if context.scene.na_1d_tools_ui.na_1d_tools_misc:
				NA1DToolsMisc.ui(
					layout=box,
					context=context
				)

		# GPLAN TOOLS
		gplan_tools_box = self.ui_section(
			layout=layout,
			context=context,
			prop='gplan_section',
			label='GPLAN TOOLS'
		)
		if context.scene.na_1d_tools_ui.gplan_section:
			# Edges Length
			box = self.ui_section(
				layout=gplan_tools_box,
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
				layout=gplan_tools_box,
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
				layout=gplan_tools_box,
				context=context,
				prop='stairs_sketcher',
				label='Stairs Sketcher'
			)
			if context.scene.na_1d_tools_ui.stairs_sketcher:
				StairsSketcher.ui(layout=box)
			# Vertical Vertices
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='vertical_vertices',
				label='Vertical Vertices'
			)
			if context.scene.na_1d_tools_ui.vertical_vertices:
				VerticalVertices.ui(
					layout=box,
					context=context
				)
			# Deloop
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='deloop',
				label='Deloop'
			)
			if context.scene.na_1d_tools_ui.deloop:
				Deloop.ui(
					layout=box,
					context=context
				)
			# Slope Loop
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='slope_loop',
				label='Slope Loop'
			)
			if context.scene.na_1d_tools_ui.slope_loop:
				SlopeLoop.ui(
					layout=box,
					context=context
				)
			# Contour Sew
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='contour_sew',
				label='Contour Sew'
			)
			if context.scene.na_1d_tools_ui.contour_sew:
				ContourSew.ui(
					layout=box,
					context=context
				)
			# Planar Edges
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='planar_edges',
				label='Select Planar Edges'
			)
			if context.scene.na_1d_tools_ui.planar_edges:
				Planar.ui(
					layout=box,
					context=context
				)
			# Connect Loop
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='connect_loop',
				label='Connect Loop'
			)
			if context.scene.na_1d_tools_ui.connect_loop:
				ConnectLoop.ui(
					layout=box,
					context=context
				)
			# Import LST
			box = self.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='import_lst',
				label='Import LST'
			)
			if context.scene.na_1d_tools_ui.import_lst:
				ImportLST.ui(
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
	def ui_section(layout, context, prop, label, content_box=True, align=True):
		# row = layout.row()
		icon = 'DOWNARROW_HLT' if getattr(context.scene.na_1d_tools_ui, prop) else 'RIGHTARROW'
		layout.prop(
			context.scene.na_1d_tools_ui,
			prop,
			icon=icon,
			text=label
		)
		if content_box and icon == 'DOWNARROW_HLT':
			box = layout.box().column(align=align)
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
