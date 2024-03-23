bl_info = {
    "name": "Add Text Drop Shadow",
    "version": (0, 1, 1),
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
        # Iterate over all selected strips
        for strip in context.selected_sequences:
            # Check if the strip is a text strip
            if strip.type == 'TEXT':
                # Set the strip as the active strip
                context.scene.sequence_editor.active_strip = strip
                
                # Duplicate the selected text strip and move it down two channels
                bpy.ops.sequencer.duplicate_move()
                bpy.ops.transform.seq_slide(value=(0, -2))
                
                # Adjust the frame start and end of the duplicate text strip
                duplicate_strip = context.scene.sequence_editor.active_strip
                duplicate_strip.frame_final_start = strip.frame_final_start
                duplicate_strip.frame_final_end = strip.frame_final_end

                # Set the color of the duplicate text strip to black
                duplicate_strip.color = (0, 0, 0, 1)
                
                # Mute duplicate text
                bpy.ops.sequencer.mute(unselected=False)

                # Add a Gaussian blur effect strip and set its size
                bpy.ops.sequencer.effect_strip_add(type='GAUSSIAN_BLUR')
                blur_strip = context.scene.sequence_editor.active_strip
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