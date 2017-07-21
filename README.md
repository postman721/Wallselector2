# Wallselector2
Program for wallpaper changing

![wallselec2](https://user-images.githubusercontent.com/29865797/28453990-3261c55c-6e02-11e7-890f-2a0904e65616.jpg)

Wallselector2 is a Python Gtk2 dialog program, which enables you to choose a background. After background is selected then the tool writes changes to .wall/wall.sh within user´s home directory. Currently, jpg and png formats are supported. You will need python and feh installed in order to use this program properly.

#Wallselector-rev.2 Copyright (c) 2016 JJ Posti <techtimejourney.net>
#Wallselector-rev.2 comes with ABSOLUTELY NO WARRANTY;
#for details see: http://www.gnu.org/copyleft/gpl.html.
#This is free software, and you are welcome to redistribute it under
#GPL Version 2, June 1991″)
#This is a simple wallpaper switching program, which seeks to replace the older Wallselector done with Zenity and Bash.

You should also add this line(or similar) to your autostart file, so that wallpaper will resume correctly upon desktop reboot.

sh /home/$USER/.wall/wall.sh &

Note. The winit script  should place the above line automatically to the .xinitrc file.

___________________________________
Original post is at:
http://www.techtimejourney.net/wallselector2/
