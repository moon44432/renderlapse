import json
import glob
import os
import subprocess


def get_scene_spp(json_path):
    with open(json_path, 'r') as f:
        config = json.load(f)
        return config['sppTarget']


def get_world_list(args):
    return sorted(glob.glob(args.backup_dir + '\\' + args.world + "-*\\" + args.world)[:8], reverse=True)


def change_target_world(world_dir, json_path):
    with open(json_path, 'r') as f:
        config = json.load(f)
        config['world']['path'] = world_dir

    os.remove(json_path)
    with open(json_path, 'w') as f:
        json.dump(config, f, indent=4)


def render(args):
    render_command = "{} -Xmx{}G {} -jar {}\\{} -scene-dir {} -render {} -f {}".format(
        args.jre_path, args.jre_mem, args.jre_arg, args.chunky_root, args.chunky_jar,
        args.chunky_root + '\\' + args.scene_dir, args.scene_name, args.chunky_arg
    )
    subprocess.call(render_command, shell=True)


def batch_render(args):
    scene_folder = args.chunky_root + '\\' + args.scene_dir + '\\' + args.scene_name
    json_path = scene_folder + "\\" + args.scene_name + ".json"

    for world in get_world_list(args):
        change_target_world(world, json_path)
        render(args)
        
        for dump in glob.glob(scene_folder + "\\" + "*.dump"):
            os.remove(dump)
        for octree2 in glob.glob(scene_folder + "\\" + "*.octree2"):
            os.remove(octree2)

        pngname = scene_folder + "\\snapshots\\" + args.scene_name + '-' + str(get_scene_spp(json_path))

        os.rename(pngname + ".png", pngname + "_{}.png".format(world.split("\\")[-2].split('-')[1]))
