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
#        print "OBJ instance "+self+"created"
#        self.bounding_box_max = #bounding_box_max # 3 float varible list
#        self.bounding_box_min = bounding_box_min # 3 float varible list
#        self.uv_bounding_box_max = uv_bounding_box_max #2 float varible list
#        self.uv_bounding_box_min = uv_bounding_box_min #2 float varible list
#        self.truncated_OBJ = truncated_OBJ # text file
#        self.vertices_count = vertices_count
#        self.faces_count = faces_count
#        self.uv_vertices_count = uv_vertices_count
#        self.vertex_normals_count = vertex_normals_count
#        self.other_csv_count = other_csv_count
#        self.other_csv_names = other_csv_names
#        self.objects = objects # list of stirngs
#        self.groups = groups # list of stirngs
#        self.mtl_file = mtl_file # list of stirngs ./file name, same as obj
#        self.materials = materials # list of string

        #if a path was not passed to the class defineing the path for the truncated file
        #then the file name will default ot bj_path[:-4]+"truncated_path.txt"
        if truncated_path == False:
            truncated_path = obj_path[:-4]+"truncated_path.txt"
#        print truncated_path

        #create a writeable file to write the truncated file to
        truncated_obj_file = open(truncated_path, 'w')

        #set up nesscary varibles
        current_line_type = 'none'
        pervious_line_type = 'none'
        grometry_line_type = 'none'
        geometry_line_type_repeated = 0
        obj_file = open(obj_path, 'r') #open file in read mode
#        print (str(obj_file)+" opened")

        #itterate over the obj file
        for line in obj_file:
            #write line to the truncated file unless its a geometry line that has
            #repeted for more than 3 lines
            if geometry_line_type_repeated < 3:
                truncated_obj_file.write(line)
            elif geometry_line_type_repeated == 3:
                truncated_obj_file.write('...\n')

            #parse what type of line the current line is
            if line.startswith('#'): ####This section can be compressed
#                current_line_type = "#" #example should be in all compressed itteratoins
                s
                geometry_line_type_repeated = 0
            elif line.startswith('mtllib'):
                geometry_line_type_repeated = 0
            elif line.startswith('usemtl'):
                geometry_line_type_repeated = 0
            elif line.startswith('o'):
                geometry_line_type_repeated = 0
            elif line.startswith('g'):
                geometry_line_type_repeated = 0
            elif line.startswith('s 1'):
                geometry_line_type_repeated = 0
            elif line.startswith('s off'):
                geometry_line_type_repeated = 0
            else:
                current_line_type = line[:2]

                #figure out if we need to increase geometry_line_type_repeated
                #TODO add a switch so any geometry lines can increase 
                ##geometry_line_type_repeated, to work around MeshLabs formating
                if current_line_type == pervious_line_type:
                    geometry_line_type_repeated += 1
#                    print 'line same as previous'
#                    print geometry_line_type_repeated
                else:
                    geometry_line_type_repeated = 0
#                    print current_line_type
#                    print pervious_line_type
#                    print 'no repeat'
                
            pervious_line_type = current_line_type

#            if line.startswith("v "):  

        obj_file.close
        truncated_obj_file.close

#obj_file_path = 'D:\OBJ test files for OBJinspect\MeshLab\MeshLabgreekSlave.final.div1.obj'
#obj_file_object = OBJ_inspect.LoadOBJ(obj_path)
