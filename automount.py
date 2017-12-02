#!/sur/bin/env python3

import os

class mountdrive():
    def __init__(self):
        print("Mounting /dev/sdb1 - /media/tv")
        os.system("mount /dev/sdb1 /media/tv")
        print("Mounting /dev/sdc1 - /media/movie")
        os.system("mount /dev/sdc1 /media/movie")
        print("Mounting /dev/sdd1 - /media/external")
        os.system("mount /dev/sdd1 /media/external")
        print("Mounting /dev/sde1 - /media/SAMSUNG")
        os.system("mount /dev/sde1 /media/SAMSUNG")

if __name__ == '__main__':
    mountdrive()