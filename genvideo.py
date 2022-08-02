import glob
import subprocess
import datetime

txt_path = "list.txt"


def gen_txt(args):
    glob_str = args.chunky_root + '\\' + args.scene_dir + '\\' + args.scene_name + "\\snapshots\\*.png"
    imgs = sorted(glob.glob(glob_str), key=lambda x: x[-10:])

    if args.sync is True:
        dates, date_deltas = [], []
        for img_name in imgs:
            dates.append(datetime.date(
                int("20" + img_name[-10:-8]), int(img_name[-8:-6]), int(img_name[-6:-4])))

        for i in range(len(dates) - 1):
            date_deltas.append((dates[i + 1] - dates[i]).days)

        date_deltas.append(1)

    with open(txt_path, "w") as f:
        for i in range(len(imgs)):
            f.write("file " + imgs[i].replace('\\', '/') + '\n')
            if args.sync is True:
                f.write("outpoint " + str(args.frame_duration * date_deltas[i]) + '\n')
            else:
                f.write("outpoint " + str(args.frame_duration) + '\n')


def gen_video(args):
    gen_txt(args)
    gen_command = "{} -safe 0 -f concat -i {} -r {} {} {}".format(
        args.ffmpeg_path, txt_path, args.framerate, args.ffmpeg_arg, args.vid_path)
    subprocess.call(gen_command, shell=True)
