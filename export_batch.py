import bpy
import os

project_dir = "{your_project_dir_goes_here}"
mesh_import_dir = "{sub_dir}"

objects_dir = project_dir + mesh_import_dir + "{objs_sub_dir}"

objects_collection = bpy.data.collections["{collection_name}"]
    

def export_collection_batch(col, output_dir, filename_prefix):    
    for mesh in col.objects:
        print(mesh.name)
        mesh.select_set(True)
        x = mesh.location.x
        y = mesh.location.y
        z = mesh.location.z
        mesh.location = (0,0,0)
        save_path = os.path.join(output_dir, filename_prefix + mesh.name + '.glb')
        bpy.ops.export_scene.gltf(filepath=save_path, export_image_format='AUTO',export_materials='NONE', export_apply=True, use_selection=True)
        mesh.location = (x,y,z)
        mesh.select_set(False)
    

bpy.ops.object.select_all(action='DESELECT')

export_collection_batch(objects_collection, objects_dir, "")
print("Done")
