# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_na_tools


from .__init__ import bl_info
from bpy.props import BoolProperty, PointerProperty
from bpy.types import Panel, PropertyGroup, Scene
from bpy.utils import register_class, unregister_class
from .arc_3.arc_3 import Arc3
from .connect_loop.connect_loop import ConnectLoop
from .contour_sew.contour_sew import ContourSew
from .corner_fill.corner_fill import CornerFill
from .delaunay_1d_shot.delaunay_voronoi_1d_panel import ui as delaunay_voronoi_1d_ui
from .deloop.deloop import Deloop
from .dlevel.dlevel import DLevel
from .drawing_split.drawing_split import DrawingSplit
from .edges_length.edges_length import EdgesLength
from .f2_snake.f2_snake import F2Snake
from .height_painter.height_painter import HeightPainter
from .import_lst.import_lst import ImportLST
from .knife_imprint.knife_imprint import KnifeImprint
from .material_select.material_1d_select import MaterialSelect
from .mesh_decompose.mesh_decompose import MeshDecompose
from .mesh_split.mesh_split import MeshSplit
from .na_1d_tools_misc.na_1d_tools_misc import NA1DToolsMisc
from .obj_tools.obj_tools import OBJTools
from .planar_edges.planar_edges import Planar
from .quad_bridge.quadbridge_panel import ui as quad_bridge_ui
from .retuber.retuber import Retuber
from .shape_loop.shape_loop import ShapeLoop
from .slope_loop.slope_loop import SlopeLoop
from .stairs_sketcher.stairs_sketcher import StairsSketcher
from .step_extrude.step_extrude import StepExtrude
from .subd_tool.subd_tool import SubdTool
from .un_negative.filter_uniformly_scaled import FilterUniformlyScaled
from .un_negative.rotten_rotation import RottenRotation
from .un_negative.unnegative_scale import UnnegativeScale
from .uv_square.uv_square import UVSquare
from .uv_tools.uv_tools import UVTools
from .vertical.vertical import Vertical
from .vertical_vertices.vertical_vertices import VerticalVertices
from .view_switch.view_switch import Viewswitch
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
	sketch_tools_section = BoolProperty(
		default=False
	)
	gplan_section = BoolProperty(
		default=False
	)
	uv_tools_section = BoolProperty(
		default=False
	)

	# modules
	arc_3 = BoolProperty(
		default=False
	)
	connect_loop = BoolProperty(
		default=False
	)
	contour_sew = BoolProperty(
		default=False
	)
	corner_fill = BoolProperty(
		default=False
	)
	delaunay_1d_shot = BoolProperty(
		default=False
	)
	deloop = BoolProperty(
		default=False
	)
	dlevel = BoolProperty(
		default=False
	)
	drawing_split = BoolProperty(
		default=False
	)
	edges_length = BoolProperty(
		default=False
	)
	filter_uniformly_scaled = BoolProperty(
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
	knife_imprint = BoolProperty(
		default=False
	)
	material_select = BoolProperty(
		default=False
	)
	mesh_decompose = BoolProperty(
		default=False
	)
	mesh_split = BoolProperty(
		default=False
	)
	na_1d_tools_misc = BoolProperty(
		default=False
	)
	obj_tools = BoolProperty(
		default=False
	)
	planar_edges = BoolProperty(
		default=False
	)
	quad_bridge = BoolProperty(
		default=False
	)
	retuber = BoolProperty(
		default=False
	)
	rotten_rotation = BoolProperty(
		default=False
	)
	shape_loop = BoolProperty(
		default=False
	)
	slope_loop = BoolProperty(
		default=False
	)
	stairs_sketcher = BoolProperty(
		default=False
	)
	step_extrude = BoolProperty(
		default=False
	)
	subd_tool = BoolProperty(
		default=False
	)
	unnegative_scale = BoolProperty(
		default=False
	)
	uv_square = BoolProperty(
		default=False
	)
	uv_tools = BoolProperty(
		default=False
	)
	vertical_vertices = BoolProperty(
		default=False
	)
	vertical_uv = BoolProperty(
		default=False
	)
	view_switch = BoolProperty(
		default=False
	)
	vitragen = BoolProperty(
		default=False
	)
	we_crease_from_seam = BoolProperty(
		default=False
	)


class NA_1D_TOOLS_PT_panel(Panel):
	bl_idname = 'NA_1D_TOOLS_PT_panel'
	bl_label = ' '	# will be overridden in draw_header()
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = '1D'

	def draw_header(self, context):
		layout = self.layout
		layout.label(text='NA 1D Tools ' + '.'.join(str(_v) for _v in bl_info['version']))

	def draw(self, context):
		layout = self.layout
		# CONVERT
		convert_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='convert_section',
			label='CONVERT'
		)
		if context.scene.na_1d_tools_ui.convert_section:
			# We Crease from Seam
			PanelsUI.ui_section(
				layout=convert_box,
				context=context,
				prop='we_crease_from_seam',
				label='We Crease from Seam',
				content_box=False
			)
			if context.scene.na_1d_tools_ui.we_crease_from_seam:
				WECFS.ui(layout=convert_box)
			# Obj Tools
			PanelsUI.ui_section(
				layout=convert_box,
				context=context,
				prop='obj_tools',
				label='Obj Shift',
				content_box=False
			)
			if context.scene.na_1d_tools_ui.obj_tools:
				OBJTools.ui(
					layout=convert_box,
					context=context
				)

		# Material 1D Select
		box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='material_select',
			label='Material 1D Select',
			align=False
		)
		if context.scene.na_1d_tools_ui.material_select:
			MaterialSelect.ui(layout=box, context=context)

		# 1D Subd Storage
		box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='subd_tool',
			label='1D Subd Storage'
		)
		if context.scene.na_1d_tools_ui.subd_tool:
			SubdTool.ui(layout=box)

		# SKETCH TOOLS
		sketch_tools_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='sketch_tools_section',
			label='SKETCH TOOLS'
		)
		if context.scene.na_1d_tools_ui.sketch_tools_section:
			# Step Extrude
			box = PanelsUI.ui_section(
				layout=sketch_tools_box,
				context=context,
				prop='step_extrude',
				label='Step Extrude'
			)
			if context.scene.na_1d_tools_ui.step_extrude:
				StepExtrude.ui(
					layout=box,
					context=context
				)
			# 3 Points Arc (Arc_3)
			box = PanelsUI.ui_section(
				layout=sketch_tools_box,
				context=context,
				prop='arc_3',
				label='3 Points Arc'
			)
			if context.scene.na_1d_tools_ui.arc_3:
				Arc3.ui(
					layout=box,
					context=context
				)
			# View Switch
			box = PanelsUI.ui_section(
				layout=sketch_tools_box,
				context=context,
				prop='view_switch',
				label='View Switch'
			)
			if context.scene.na_1d_tools_ui.view_switch:
				Viewswitch.ui(
					layout=box,
					context=context
				)

		# EDIT TOOLS
		edit_tools_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='edit_section',
			label='EDIT TOOLS'
		)
		if context.scene.na_1d_tools_ui.edit_section:
			# Delaunay 1D Shot
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='drawing_split',
				label='Drawing Split'
			)
			if context.scene.na_1d_tools_ui.drawing_split:
				DrawingSplit.ui(layout=box)
			# Retuber
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='retuber',
				label='Retuber'
			)
			if context.scene.na_1d_tools_ui.retuber:
				Retuber.ui(layout=box)
			# Vitragen
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='unnegative_scale',
				label='Unnegative Scale'
			)
			if context.scene.na_1d_tools_ui.unnegative_scale:
				UnnegativeScale.ui(
					layout=box,
					context=context
				)
			# Filter Uniformly Scaled
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='filter_uniformly_scaled',
				label='FilterUniformlyScaled'
			)
			if context.scene.na_1d_tools_ui.filter_uniformly_scaled:
				FilterUniformlyScaled.ui(
					layout=box,
					context=context
				)
			# NA 1D Tools Misc
			box = PanelsUI.ui_section(
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
			# Mesh Decompose
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='mesh_decompose',
				label='Mesh Decompose',
				align=False
			)
			if context.scene.na_1d_tools_ui.mesh_decompose:
				MeshDecompose.ui(
					layout=box,
					context=context
				)
			# Corner Fill
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='corner_fill',
				label='Corner Fill',
				align=False
			)
			if context.scene.na_1d_tools_ui.corner_fill:
				CornerFill.ui(
					layout=box,
					context=context
				)
			# Shape Loop
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='shape_loop',
				label='Shape Loop',
				align=False
			)
			if context.scene.na_1d_tools_ui.shape_loop:
				ShapeLoop.ui(
					layout=box,
					context=context
				)
			# Mesh Split
			box = PanelsUI.ui_section(
				layout=edit_tools_box,
				context=context,
				prop='mesh_split',
				label='Mesh Split',
				align=False
			)
			if context.scene.na_1d_tools_ui.mesh_split:
				MeshSplit.ui(
					layout=box,
					context=context
				)

		# GPLAN TOOLS
		gplan_tools_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='gplan_section',
			label='GPLAN TOOLS'
		)
		if context.scene.na_1d_tools_ui.gplan_section:
			# Edges Length
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='stairs_sketcher',
				label='Stairs Sketcher'
			)
			if context.scene.na_1d_tools_ui.stairs_sketcher:
				StairsSketcher.ui(layout=box)
			# Vertical Vertices
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			box = PanelsUI.ui_section(
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
			# DLevel
			box = PanelsUI.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='dlevel',
				label='DLevel'
			)
			if context.scene.na_1d_tools_ui.dlevel:
				DLevel.ui(
					layout=box,
					context=context
				)
			# Knife Imprint
			box = PanelsUI.ui_section(
				layout=gplan_tools_box,
				context=context,
				prop='knife_imprint',
				label='Knife Imprint'
			)
			if context.scene.na_1d_tools_ui.knife_imprint:
				KnifeImprint.ui(
					layout=box,
					context=context
				)

		# Quad Bridge
		box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='quad_bridge',
			label='Quad Bridge 0.8.2'
		)
		if context.scene.na_1d_tools_ui.quad_bridge:
			quad_bridge_ui(
				layout=box,
				context=context
			)

		# UV TOOLS
		uv_tools_section_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='uv_tools_section',
			label='UV TOOLS'
		)
		if context.scene.na_1d_tools_ui.uv_tools_section:
			# UV Tools
			box = PanelsUI.ui_section(
				layout=uv_tools_section_box,
				context=context,
				prop='uv_tools',
				label='UV Tools'
			)
			if context.scene.na_1d_tools_ui.uv_tools:
				UVTools.ui(
					layout=box,
					context=context,
					area='VIEWPORT'
				)
			# UV Square
			box = PanelsUI.ui_section(
				layout=uv_tools_section_box,
				context=context,
				prop='uv_square',
				label='UV Square'
			)
			if context.scene.na_1d_tools_ui.uv_square:
				UVSquare.ui(
					layout=box,
					context=context,
					area='VIEWPORT'
				)


class NA_1D_TOOLS_PT_panel_uv(Panel):
	bl_idname = 'NA_1D_TOOLS_PT_panel_uv'
	bl_label = ' '	# will be overridden in draw_header()
	bl_space_type = 'IMAGE_EDITOR'
	bl_region_type = 'TOOLS'
	bl_category = '1D'

	def draw_header(self, context):
		layout = self.layout
		layout.label(text='NA 1D Tools ' + '.'.join(str(_v) for _v in bl_info['version']))

	def draw(self, context):
		layout = self.layout

		# UV TOOLS
		uv_tools_section_box = PanelsUI.ui_section(
			layout=layout,
			context=context,
			prop='uv_tools_section',
			label='UV TOOLS'
		)
		if context.scene.na_1d_tools_ui.uv_tools_section:
			# UV Tools
			box = PanelsUI.ui_section(
				layout=uv_tools_section_box,
				context=context,
				prop='uv_tools',
				label='UV Tools'
			)
			if context.scene.na_1d_tools_ui.uv_tools:
				UVTools.ui(
					layout=box,
					context=context,
					area='UV'
				)


class PanelsUI:

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
	register_class(NA_1D_TOOLS_PT_panel_uv)


def unregister():
	unregister_class(NA_1D_TOOLS_PT_panel_uv)
	unregister_class(NA_1D_TOOLS_PT_panel)
	del Scene.na_1d_tools_ui
	unregister_class(NA_1D_TOOLS_UI)
