# fstab 
## Mounting ntfs disks
I've been using arch linux (my extensively used linux) since more than an year now yet I faced issues using shared disks between arch and windows (my dual boot PC)
In my first month of usage I edited the fstab file, saved it and reboot my PC only to find that grub is spurting weird errors and I cant boot. Ever since then i've been kinda scared of editing the fstab file since it took me a long while to fix those grub errors due to lack of knowledge. 
I was explicitly mounting the disks whenever I had to use them which was very time taking, so much that i often rather restarted my computer just to watch anime which lies in some ntfs disk. 
I've finally educated myself with fstab (partly, I still dont understand most of it)
It was pretty simply and I was scared for no reason. 

`/etc/fstab`
``` sh
[200~# Static information about the filesystems.
# See fstab(5) for details.

# <file system> <dir> <type> <options> <dump> <pass>
# UUID=<>
/dev/sdc4           	/         	ext4      	rw,relatime,data=ordered	0 1

# UUID=<>
/dev/sdc3           	none      	swap      	defaults,pri=-2	0 0

#Entertainent
UUID=<> /home/timetraveller/Entertainment ntfs rw,auto,users,exec,nls=utf8,umask=003,gid=985,uid=1000    0   0

#Media
UUID=<> /home/timetraveller/Media ntfs rw,auto,users,exec,nls=utf8,umask=003,gid=985,uid=1000    0   0

#Software
UUID=<> /home/timetraveller/Software+Stuff ntfs rw,auto,users,exec,nls=utf8,umask=003,gid=985,uid=1000    0   0

#Work
UUID=<> /home/timetraveller/Work ntfs rw,auto,users,exec,nls=utf8,umask=003,gid=985,uid=1000    0   0
```

Points to notice:
- Find disk UUID using `sudo blkid`
- Replace disk id above
- Find user and group id using id
- Make sure /home/timetraveller/anything exists
- MAKE SURE TO RUN `sudo mount -a` before rebooting
- If no errors, reboot and its all safe

What happened months ago was that the directory I mounted my disks to didn't exist. I didn't checked for the errors and restarted the OS which led to disrupt the fstab and eventually grub would not let me boot. 

MORAL: Educate yourself (atleast a little) with what you're doing rather than just reading a guide off the internet.
 
https://help.ubuntu.com/community/Fstab
https://askubuntu.com/questions/46588/how-to-automount-ntfs-partitions

tbh the answer above is most of my "education" 


