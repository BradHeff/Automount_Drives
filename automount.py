#!/sur/bin/env python3

import os


class Mountdrive():
    def __init__(self):
        print("================================================")
        print("==============Auto Mount Activated==============")
        print("================================================")
        try:
            print("Mounting /dev/sdb1 - /media/tv")
            os.system("mount /dev/sdb1 /media/tv")
            self.seperator("/dev/sdb1")
        except:
            self.errortext("/dev/sdb1")
        try:
            print("Mounting /dev/sdc1 - /media/movie")
            os.system("mount /dev/sdc1 /media/movie")
            self.seperator("/dev/sdc1")
        except:
            self.errortext("/dev/sdc1")
        try:
            print("Mounting /dev/sdd1 - /media/SAMSUNG")
            os.system("mount /dev/sdd1 /media/SAMSUNG")
            self.seperator("/dev/sdd1")
        except:
            self.errortext("/dev/sdd1")
        try:
            print("Mounting /dev/sde1 - /media/external")
            os.system("mount /dev/sde1 /media/external")
            self.seperator("/dev/sde1")
        except:
            self.errortext("/dev/sde1")

    @staticmethod
    def seperator(text):
        print(text + " mount Success")
        print("==================================")

    @staticmethod
    def errortext(text):
        print("No mount point " + text)
        print("==================================")


if __name__ == '__main__':
    Mountdrive()
