import os
from fileinput import filename



filename = "C:\\Users\\845160\\Downloads\\Python\\wipeout.txt"
destinationfilename="C:\\Users\\845160\\Downloads\\Python\\newname.txt"
os.rename(filename,destinationfilename)