#### doku: https://www.freecadweb.org/wiki/Python_scripting_tutorial ####


# create a new document
testdoc = FreeCAD.newDocument()
# create a box
box = testdoc.addObject("Part::Box","myBox")
# recompute document
testdoc.recompute()

##check doc functions
testdoc.

#check box functions
box.


#######

def createBox(a,b,c):
   a = 3
   b = 3   
   c = 3
   boxdoc = FreeCAD.newDocument()
   box = boxdoc.addObject("Part::Box","myBox")
   boxdoc.recompute()
   box.Height = a
   box.Length = b
   box.Width = c
   boxdoc.recompute()
