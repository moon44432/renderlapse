import json
import sys
import glob
import os
import subprocess
import time
import datetime
import argparse

chunky_path = "ChunkyLauncher.jar"
scene_dir = "scenes"
scene_name = "msv4"
java_path = "java"
java_arg = "-Xmx8G"
chunky_arg = ""
output_png = "msv4-64"
backup_dir = "D:\\Backups\\ServerBackup"


def get_world_list():
    return sorted(glob.glob(backup_dir + "\\MoonServer-*\\MoonServer")[:8], reverse=True)


def change_target_world(world_dir):
    json_path = scene_dir + "\\" + scene_name + "\\" + scene_name + ".json"
    with open(json_path, 'r') as f:
        config = json.load(f)
        config['world']['path'] = world_dir

    os.remove(json_path)
    with open(json_path, 'w') as f:
        json.dump(config, f, indent=4)


def render(world_dir):
    render_command = "{} {} -jar {} -scene-dir {} -render {} -f {}".format(
        java_path, java_arg, chunky_path, scene_dir, scene_name, chunky_arg
    )
    subprocess.call(render_command, shell=True)


def batch_render():
    scene_path = scene_dir + "\\" + scene_name

    for world in get_world_list():
        change_target_world(world)
        render(world)
        
        for dump in glob.glob(scene_path + "\\" + "*.dump"):
            os.remove(dump)
        for octree2 in glob.glob(scene_path + "\\" + "*.octree2"):
            os.remove(octree2)

        os.rename(scene_path + "\\snapshots\\" + output_png + ".png", 
        scene_path + "\\snapshots\\" + output_png + "_{}.png"
        .format(world.split("\\")[-2].split('-')[1]))


if __name__ == "__main__":
    batch_render()