import Tkinter as tk
from tkFileDialog import askopenfilename
import os, csv


#open/id obj file
root = tk.Tk()
root.withdraw()
obj_file_path = askopenfilename(filetypes=[("Wavefront","*.obj"),("All Files","*.*")]) # Open dialog box
print obj_file_path

#load the first n lines of the file
f = open(obj_file_path, 'r')   #open file in read mode open('D:/MeshLabgreekSlave.final.div1.obj')
print f
x = 1
while x == 1:
    last_pos = f.tell()
    current_line_in_obj=f.readline()
    print current_line_in_obj
    if current_line_in_obj.startswith("v"):
        x += 1
        f.seek(last_pos)

pline_count=0
v_line_count=0
vn_line_count=0
f_line_count=0
vt_line_count=0
extra_line_count=0
context_lines=0
y = 1

for line in f:
    if y ==1:
        print "not relivent, nor line above",line
        y+=1
    if context_lines < 4:
        print line
        context_lines+=1
    line_count +=1
    if line.startswith("v "):
        v_line_count +=1
    elif line.startswith("vn "):
        vn_line_count +=1
    elif line.startswith("f "):
        f_line_count +=1
    elif line.startswith("vt "):
        vt_line_count +=1
    else:
        print line
        extra_line_count +=1
        context_lines=0
    
#    if line_count%5000 == 0:
#        print line_count
print "v ",v_line_count
print "vn ",vn_line_count
print "f ",f_line_count
print "vt ",vt_line_count
#    if line_count%1000 == 0:
#        print line_count
print line_count
print v_line_count+vn_line_count+vt_line_count+f_line_count+extra_line_count

#break the header of obj file in to variables 
#see if the obj points at an mtl if so brake in to variables
#else see is an mtl of the same name is in the dir ask to use that
#else ask if want to use n existing mtl as refrence or create later
#if ant of the above mtl are used then brake into variabes and check for image file
# populate a screen with all the possible variables in text field and fill in the ones we have
# prefilled in fields have an associated reset button
#image file(s) can be written in or found by an open file dilouge
#image fill states pixel by pixel dimensions
##color patch showing what vales look like
##button on screen for advanced inspection 
##lines in file
#user can save an individual field
#save and save as option
#refresh option
