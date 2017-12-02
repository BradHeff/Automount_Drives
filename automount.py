#!/sur/bin/env python3

import os


class Mountdrive():
    def __init__(self):
        try:
            print("Mounting /dev/sdb1 - /media/tv")
            os.system("mount /dev/sdb1 /media/tv")
        except:
            print("No drive /dev/sdb1")
        try:
            print("Mounting /dev/sdc1 - /media/movie")
            os.system("mount /dev/sdc1 /media/movie")
        except:
            print("No drive /dev/sdc1")
        try:
            print("Mounting /dev/sdd1 - /media/external")
            os.system("mount /dev/sdd1 /media/external")
        except:
            print("No drive /dev/sdd1")
        try:
            print("Mounting /dev/sde1 - /media/SAMSUNG")
            os.system("mount /dev/sde1 /media/SAMSUNG")
        except:
            print("No drive /dev/sdr1")


if __name__ == '__main__':
    Mountdrive()