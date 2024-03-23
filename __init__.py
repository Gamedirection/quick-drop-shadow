bl_info = {
    "name": "Add Text Drop Shadow",
    "version": (0, 1, 3),
    "author": "Ian Letarte, GameDirection",
    "blender": (4, 0, 0),
    "description": "Add a nice drop shadow to your text strips in the VSE",
    "category": "Sequencer",
}


import bpy

class AddTextDropShadowOperator(bpy.types.Operator):
    bl_idname = "vse.add_text_drop_shadow"
    bl_label = "Add Text Drop Shadow"

    def execute(self, context):
        sequences = context.scene.sequence_editor.sequences
        selected_text_strips = [strip for strip in sequences if strip.type == 'TEXT' and strip.select]

        for strip in selected_text_strips:
            # Enhanced check: Verify if a blur effect specifically tagged for this strip exists
            blur_exists = any(s for s in sequences if s.type == 'GAUSSIAN_BLUR' and s.name == f"Blur_{strip.name}")

            if not blur_exists:
                original_channel = strip.channel
                target_duplicate_channel = max(1, original_channel - 2)
                target_gaussian_channel = target_duplicate_channel + 1

                # Duplicate the text strip
                bpy.ops.sequencer.select_all(action='DESELECT')
                strip.select = True
                context.scene.sequence_editor.active_strip = strip
                bpy.ops.sequencer.duplicate()
                duplicate_strip = context.scene.sequence_editor.active_strip
                duplicate_strip.channel = target_duplicate_channel

                duplicate_strip.color = (0, 0, 0, 1)  # Set color to black
                duplicate_strip.mute = True  # Mute the duplicate strip

                # Add a Gaussian blur effect strip
                bpy.ops.sequencer.select_all(action='DESELECT')
                duplicate_strip.select = True
                context.scene.sequence_editor.active_strip = duplicate_strip
                bpy.ops.sequencer.effect_strip_add(type='GAUSSIAN_BLUR', channel=target_gaussian_channel)
                blur_strip = context.scene.sequence_editor.active_strip
                blur_strip.name = f"Blur_{strip.name}"  # Ensuring a unique, specific name for the blur strip
                blur_strip.size_x = 30
                blur_strip.size_y = 30

        return {'FINISHED'} 

def menu_func(self, context):
    self.layout.operator("vse.add_text_drop_shadow")

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
    bpy.types.SEQUENCER_MT_strip.append(menu_func)

def unregister():
    bpy.utils.unregister_class(AddTextDropShadowOperator)
    bpy.utils.unregister_class(TEXTDROPSHADOW_PT_panel)
    bpy.types.SEQUENCER_MT_strip.remove(menu_func)

if __name__ == "__main__":
    register()