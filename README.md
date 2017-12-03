# Automount_Drives
Automaticly mount drives on server startup

This script will automount HDD at startup, this script was made for my ubuntu server 16.04 here are the steps to take 
for this script to work.

1: copy the script to the /bin directory

    sudo cp -i /path/to/script/automount.py /bin
    
2: edit crontab

    sudo crontab -e
    
3: add the .py script to the bottom of the crontab

    @reboot /bin/automount.py &
    
4: then reboot and let the automount.py do its job

    sudo reboot
  
  
