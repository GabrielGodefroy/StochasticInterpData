


NB_RULES = [2,3,4,5]
NB_LINES = [3,4,5,6]


def convert_to_xzy(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    x_val = str("{0:.3f}".format((float(x)-29000.)/1000.));
    y_val = str("{0:.3f}".format((float(y)-120000.)/1000.));
    z_val = str("{0:.3f}".format(0.));
    return x_val, y_val, z_val

def get_reference(names, coord):
    result = "Ref_"+str(nb_rule)+"_"+str(nb_line) + " = [\n";

    for ind1 in range(len(names)):
        for ind2 in range(ind1, len(names)):
            n1, n2 = names[ind1][18:], names[ind2][18:]
            if (n1 == n2):
                result+="[" +   str(coord[ind1][0]) + ", "   +\
                                str(coord[ind1][1]) + ", "  +\
                                str(coord[ind1][2]) + ",\t" +\
                                str(coord[ind2][0]) + ", " +\
                                str(coord[ind2][1]) + ", " +\
                                str(coord[ind2][2]) + "],\n"
    result += "];\n"
    return result ;



def get_coordinates(input_content):
    c_result = ""    
    names    = []
    coord    = []
    last_line = None

    all_coord = []
    c_result += "Barycent_"+str(nb_rule)+"_"+str(nb_line) + " = [\n";

    for l_number, line in enumerate(input_content):
        if line[0:5] == "Inter":
            split = line.split()
            names.append(split[0])
            x,y,z = convert_to_xzy(split[1], split[2], split[3])
            all_coord.append([float(x),float(y),float(z)])
            c_result += "\t"+x+", "+y+", "+z+",\n"
            last_line = l_number;

    c_result += "];\n"

    return c_result, names, all_coord, last_line;



def process_file(filename):

    FILE_IN = open(filename, "r")
    input_content = FILE_IN.read().split("\n")
    FILE_IN.close()

    result="";
    
    c_result, names, coord, last_line = get_coordinates(input_content)
    nb_obs = len(names)
    result+=c_result;

    result+=get_reference(names, coord)

    

    result += "GraphA_"+str(nb_rule)+"_"+str(nb_line) + " = [\n";
    for ind1 in range(nb_obs):
        l_number = last_line+3+ind1
        line = input_content[l_number]
        line = line.split()
        assert(len(line)==nb_obs)            
        for ind2 in range(nb_obs):
            elem = line[ind2]
            if(ind1==ind2):
                assert(elem=='-1')
            if(float(elem)>0):
                result += '[' + str(coord[ind1][0]) + ", "   +\
                                str(coord[ind1][1]) + ", "  +\
                                str(coord[ind1][2]) + ",\t" +\
                                str(coord[ind2][0]) + ", " +\
                                str(coord[ind2][1]) + ", " +\
                                str(coord[ind2][2]) + "],\n"
    result += "];\n"


    result += "GraphB_"+str(nb_rule)+"_"+str(nb_line) + " = [\n";
    for ind1 in range(nb_obs):
        l_number = last_line+nb_obs+5+ind1
        print(l_number)
        print(line)
        line = input_content[l_number]
        line = line.split()
        assert(len(line)==nb_obs)            
        for ind2 in range(nb_obs):
            elem = line[ind2]
            print(ind1, ind2, line)
            if(ind1==ind2):
                assert(elem=='-1')
            if(float(elem)>0):
                result += '[' + str(coord[ind1][0]) + ", "   +\
                                str(coord[ind1][1]) + ", "  +\
                                str(coord[ind1][2]) + ",\t" +\
                                str(coord[ind2][0]) + ", " +\
                                str(coord[ind2][1]) + ", " +\
                                str(coord[ind2][2]) + "],\n"
    result += "];\n"


    FILE_OUT = open("js/Fig6b_"+str(nb_rule)+"_"+str(nb_line)+".js", "w")
    FILE_OUT.write(result)
    FILE_OUT.close()






for nb_rule in NB_RULES:
    for nb_line in NB_LINES:
        process_file("raw_graph/Fig6b_"+str(nb_rule)+"_"+str(nb_line)+"_3600_0_0_2_0_.txt")





