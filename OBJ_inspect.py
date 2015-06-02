import obj_line_tool

class LoadOBJ ():
    """Looks through OBJ file and extracts key information including
    3D bounding box
    UV bounding box
    truncated version of obj file
    number of vertices
    number of faces
    number of uv vertices
    number of vertex normals
    number of other CSV values
    types of other CSV valuse
    objects
    groups
    refrenced material libarys
    materials
    """

    def __init__ (self, obj_path,truncated_path = False):
        print self
#        print "OBJ instance " + u(self) + " created"
#        self.bounding_box_max = #bounding_box_max # 3 float variable list
#        self.bounding_box_min = bounding_box_min # 3 float variable list
#        self.uv_bounding_box_max = uv_bounding_box_max #2 float variable list
#        self.uv_bounding_box_min = uv_bounding_box_min #2 float variable list
#        self.truncated_OBJ = truncated_OBJ # text file
#        self.vertices_count = vertices_count
#        self.faces_count = faces_count
#        self.uv_vertices_count = uv_vertices_count
#        self.vertex_normals_count = vertex_normals_count
#        self.other_csv_count = other_csv_count
#        self.other_csv_names = other_csv_names
#        self.objects = objects # list of stirngs
#        self.groups = groups # list of stirngs
#        self.mtl_file = mtl_file # list of strings ./file name, same as obj
#        self.materials = materials # list of strings

        #if a path was not passed to the class defineing the path for the truncated file
        #then the file name will default ot bj_path[:-4]+"truncated_path.txt"
        if truncated_path == False:
            truncated_path = obj_path[:-4]+"truncated_path.txt"
#        print truncated_path

        #create a writeable file to write the truncated file to
        truncated_obj_file = open(truncated_path, 'w')

        #set up neceesary varibles
        current_line_type = 'none'
        pervious_line_type = 'none'
        geometry_line_type = 'none'
        geometry_line_type_repeated = 0
        obj_file = open(obj_path, 'r') #open file in read mode

        #functions to act on each line type
        def comment():
            geometry_line_type_repeated = 0
            print 'comment'
        def mtllib():
            geometry_line_type_repeated = 0
            print 'mtlib'
        def usemtl():
            geometry_line_type_repeated = 0
            print 'usemtl'
        def geo_object():
            geometry_line_type_repeated = 0
            print 'geo_object'
        def group():
            geometry_line_type_repeated = 0
        def s():
            geometry_line_type_repeated = 0
        def v():
            pass
        def vn():
            pass
        def f():
            pass
        def vt():
            pass

        #dictionary to call functions based on line flag
        dictionary = {
            '#': comment,
            'mtllib': mtllib,
            'usemtl': usemtl,
            'o': geo_object,
            'g': group,
            's': s,
            'v': v,
            'vn': vn,
            'f': f,
            'vt': vt
            }

        #itterate over the obj file line by line
        for line in obj_file:
            #find the type of the current line
            #by spliting the line on whitespace and calling the first element
            current_line_type = line.split()[0]
            #call the function based on the line type
            #TODO should the functions be in a different file?
            dictionary[current_line_type]()
            


            #write line to the truncated file unless its a geometry line
            #that has repeted for more than 3 lines
            #TODO only write a new type of geometry line once, reset
            #count after each non-geometry line is called
            # TODO effeciency can be gained by the if statement being
            #for values > 3, thus skipping the other 2 steps most of the tiem
            #even better don't increment past a certain poirnt
            #save the add and possibly more expensive comparison?
            if geometry_line_type_repeated < 3:
                truncated_obj_file.write(line)
            elif geometry_line_type_repeated == 3:
                truncated_obj_file.write('...\n')




##TODO add a switch so any geometry lines can increase 
##geometry_line_type_repeated, to work around MeshLabs formating
##only list the first instance of a geometry type in the truncated file, then ...
##keep track of how many instances there are of each
##the section should look like:
##
##f 345 264 347
##...
##v 234 253 3452
##...
##vt 343 234 345
##...
##The section had:
##456 face (f) lines
##345 vertice (v) lines
            #figure out if we need to increase geometry_line_type_repeated
            if current_line_type == pervious_line_type:
                geometry_line_type_repeated += 1
#                print 'line same as previous'
#                print geometry_line_type_repeated
            else:
                geometry_line_type_repeated = 0
#                    print current_line_type
#                    print pervious_line_type
                print 'no repeat'
                
            pervious_line_type = current_line_type


        obj_file.close
        truncated_obj_file.close

#obj_file_path = 'D:\OBJ test files for OBJinspect\MeshLab\MeshLabgreekSlave.final.div1.obj'
#obj_file_object = OBJ_inspect.LoadOBJ(obj_path)
