#Wallselector-rev.2 - initial setup component Copyright (c) 2016 JJ Posti <techtimejourney.net> 
#The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
#This is a simple wallpaper switching program, which seeks to replace the older Wallselector done with Zenity and Bash.

mkdir /home/$USER/.wall
echo "\n $(cat ~/.xinitrc)"  > ~/.xinitrc
echo "sh /home/$USER/.wall/wall.sh & $(cat ~/.xinitrc)" > ~/.xinitrc
