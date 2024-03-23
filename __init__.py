bl_info = {
    "name": "Add Text Drop Shadow",
    "version": (0, 1, 4),
    "author": "Ian Letarte, GameDirection",
    "blender": (4, 0, 0),
    "description": "Add a nice drop shadow to your text strips in the VSE",
    "category": "Sequencer",
}


import bpy
from bpy.props import IntProperty, FloatVectorProperty, EnumProperty, FloatProperty

class AddTextDropShadowOperator(bpy.types.Operator):
    bl_idname = "vse.add_text_drop_shadow"
    bl_label = "Add Text Drop Shadow"

    blur_amount: IntProperty(
        name="Blur Amount",
        description="Amount of Gaussian Blur",
        default=30,
        min=0,
        max=100
    )

    shadow_color: FloatVectorProperty(
        name="Shadow Color",
        description="Color of the text shadow",
        subtype='COLOR',
        size=4,
        min=0.0,
        max=1.0,
        default=(0.0, 0.0, 0.0, 1.0)
    )

    shadow_opacity: FloatProperty(
        name="Shadow Opacity",
        description="Opacity of the shadow",
        min=0.0,
        max=1.0,
        default=1.0
    )

    blend_modes = [
        ('REPLACE', "Replace", ""),
        ('OVER_DROP', "Over Drop", ""),
        ('ALPHA_OVER', "Alpha Over", ""),
        ('ADD', "Add", ""),
    ]

    blend_mode: EnumProperty(
        name="Blend Mode",
        description="Blend mode for the shadow",
        items=blend_modes,
        default='ALPHA_OVER',
    )

    def execute(self, context):
        sequences = context.scene.sequence_editor.sequences
        selected_text_strips = [strip for strip in sequences if strip.type == 'TEXT' and strip.select]

        for strip in selected_text_strips:
            blur_exists = any(s for s in sequences if s.type == 'GAUSSIAN_BLUR' and s.name == f"Blur_{strip.name}")

            if not blur_exists:
                original_channel = strip.channel
                target_duplicate_channel = max(1, original_channel - 2)
                target_gaussian_channel = target_duplicate_channel + 1

                bpy.ops.sequencer.select_all(action='DESELECT')
                strip.select = True
                context.scene.sequence_editor.active_strip = strip
                bpy.ops.sequencer.duplicate()
                duplicate_strip = context.scene.sequence_editor.active_strip
                duplicate_strip.channel = target_duplicate_channel

                # Set color and opacity
                shadow_color = self.shadow_color[:3] + (self.shadow_opacity,)
                duplicate_strip.color = shadow_color
                duplicate_strip.blend_type = self.blend_mode
                duplicate_strip.mute = True

                bpy.ops.sequencer.select_all(action='DESELECT')
                duplicate_strip.select = True
                context.scene.sequence_editor.active_strip = duplicate_strip
                bpy.ops.sequencer.effect_strip_add(type='GAUSSIAN_BLUR', channel=target_gaussian_channel)
                blur_strip = context.scene.sequence_editor.active_strip
                blur_strip.name = f"Blur_{strip.name}"
                blur_strip.size_x = self.blur_amount
                blur_strip.size_y = self.blur_amount

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class TEXTDROPSHADOW_PT_panel(bpy.types.Panel):
    bl_label = "Text Drop Shadow"
    bl_idname = "TEXTDROPSHADOW_PT_panel"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("vse.add_text_drop_shadow")

def register():
    bpy.utils.register_class(AddTextDropShadowOperator)
    bpy.utils.register_class(TEXTDROPSHADOW_PT_panel)