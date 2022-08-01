import glob
import subprocess
import datetime


def gen_txt():
    imgs = sorted(glob.glob("*.png"), key=lambda x:x[-10:])
    dates, date_deltas = [], []
    for imgname in imgs:
        dates.append(datetime.date(
            int("20" + imgname[-10:-8]), int(imgname[-8:-6]), int(imgname[-6:-4])))
    
    for i in range(len(dates) - 1):
        date_deltas.append((dates[i + 1] - dates[i]).days)
    
    date_deltas[0] = 300
    date_deltas.append(300)

    with open("list.txt", "w") as f:
        for i in range(len(imgs)):
            f.write("file " + imgs[i] + '\n')
            f.write("outpoint " + str(0.02 * date_deltas[i]) + '\n')


def gen_video():
    pass


gen_txt()
