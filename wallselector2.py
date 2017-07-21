#Wallselector-rev.2 Copyright (c) 2016 JJ Posti <techtimejourney.net> 
#Wallselector-rev.2  comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
#This is a simple wallpaper switching program, which seeks to replace the older Wallselector done with Zenity and Bash.

#!/usr/bin/env python

####Defining the dialog
import sys, os
import pygtk, subprocess, gtk, getpass
from subprocess import Popen
pygtk.require('2.0')


dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialog.set_default_response(gtk.RESPONSE_OK)

png = gtk.FileFilter()
png.set_name("Png images")
png.add_pattern("*.png")
dialog.add_filter(png)

jpg = gtk.FileFilter()
jpg.set_name("Jpg images")
jpg.add_pattern("*.jpg")
dialog.add_filter(jpg)

response = dialog.run()
##########################

#Defining filename variable and changing background with Feh

filename=str(dialog.get_filename())
if response == gtk.RESPONSE_OK:
	print filename
	subprocess.Popen(['feh', '--bg-scale', filename])
	name=getpass.getuser()
	uhome="/home/"
	wall="/.wall/wall.sh"        
	combine=uhome + name + wall
	folder=uhome+name 
	print combine
	fehcommand="feh --bg-scale "
	subprocess.Popen(['rm', '-r' , combine])
	subprocess.Popen(['touch', combine])
	os.chdir(folder)
	print folder 
	f = open(combine, 'a')
	f.write(fehcommand )
	f.write(filename)
	f.write('\n')
	f.write('\n')
	f.close() 
elif response == gtk.RESPONSE_CANCEL:
    print 'Closed,since no selection.'
dialog.destroy()
