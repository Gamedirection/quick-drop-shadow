

bl_info = {
    "name": "Add Text Drop Shadow",
    "version": (0, 1, 0),
    "author": "Ian Letarte",
    "blender": (4, 0, 0),
    "description": "Add a nice drop shadow to your text strips in the VSE",
    "category": "Sequencer",
}


import bpy

class AddTextDropShadowOperator(bpy.types.Operator):
    bl_idname = "vse.add_text_drop_shadow"
    bl_label = "Add Text Drop Shadow"

    def execute(self, context):
        # Check if there's a selected strip and if it's a text strip
        selected_strip = context.scene.sequence_editor.active_strip
        if selected_strip and selected_strip.type == 'TEXT':
            # Duplicate the selected text strip and move it down two channels
            bpy.ops.sequencer.duplicate_move()
            bpy.ops.transform.seq_slide(value=(0, -2))
            
            # Adjust the frame start and end of the duplicate text strip
            duplicate_strip = context.active_sequence_strip
            duplicate_strip.frame_final_start = selected_strip.frame_final_start
            duplicate_strip.frame_final_end = selected_strip.frame_final_end

            # Set the color of the duplicate text strip to black
            context.active_sequence_strip.color = (0, 0, 0, 1)
            
            #mute duplicate text
            bpy.ops.sequencer.mute(unselected=False)


            # Add a Gaussian blur effect strip and set its size
            bpy.ops.sequencer.effect_strip_add(type='GAUSSIAN_BLUR')
            context.active_sequence_strip.size_x = 30
            context.active_sequence_strip.size_y = 30
            



        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator("vse.add_text_drop_shadow")

def register():
    bpy.utils.register_class(AddTextDropShadowOperator)
    bpy.types.SEQUENCER_MT_strip.append(menu_func)

def unregister():
    bpy.utils.unregister_class(AddTextDropShadowOperator)
    bpy.types.SEQUENCER_MT_strip.remove(menu_func)

if __name__ == "__main__":
    register()
