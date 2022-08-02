from batchrender import batch_render
from genvideo import gen_video
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="renderlapse",
                                     description="Create timelapse video from Minecraft world backups",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(help='sub-command help')
    parser_ren = subparsers.add_parser("render", help="renders given world backups and creates a batch of images",
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter, aliases=['ren'])
    parser_gen = subparsers.add_parser("genvideo", help="generates video by concatenating rendered images",
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter, aliases=['vid'])

    parser.add_argument('--chunky-root', help="root directory of Chunky", required=True)
    parser.add_argument('--chunky-jar', help="jre executable of Chunky", default="ChunkyLauncher.jar")
    parser.add_argument('--scene-dir', help="where Chunky scenes are saved", default="scenes")
    parser.add_argument('--scene-name', help="template scene name you've created", required=True)

    parser_ren.add_argument('--backup-dir', help="where your world backups are located", required=True)
    parser_ren.add_argument('--world', help="your world name", required=True)
    parser_ren.add_argument('--jre-path', help="JRE path", default="java")
    parser_ren.add_argument('--jre-mem', help="memory allocated to JRE, in GB", default=4, type=int)
    parser_ren.add_argument('--jre-arg', help="additional JRE arguments")
    parser_ren.add_argument('--chunky-arg', help="additional Chunky arguments")
    parser_ren.set_defaults(func=batch_render)

    parser_gen.add_argument('--ffmpeg-path', help="ffmpeg path", default="ffmpeg")
    parser_gen.add_argument('--ffmpeg-arg', help="additional ffmpeg arguments", default="-pix_fmt yuv420p")
    parser_gen.add_argument('--framerate', help="framerate of the video", default=60, type=int)
    parser_gen.add_argument('--vid-path', help="output video path", default="output.mp4")
    parser_gen.add_argument('--frame-duration', help="duration of each frame", default=0.1, type=float)
    parser_gen.add_argument('--sync', help="multiplies each frame's duration in proportion to "
                                           "the dates between each two backups, "
                                           "therefore more accurate", action="store_true")
    parser_gen.set_defaults(func=gen_video)

    args = parser.parse_args()
    print(args)
    args.func(args)
