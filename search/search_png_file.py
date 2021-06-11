import os
import string
import platform
import shutil

#this script collects the imgs with .png .jpeg and .jpg extension and mode to another folder

path_to_save = 'C:/Users/rodri/OneDrive/Desktop/Scripts/imgs'

if platform.system() == "Windows":
    pd_names = string.ascii_uppercase
    vd_names = []
    for each_drive in pd_names:
        if os.path.exists(each_drive+":\\"):
            # print(each_drive)
            vd_names.append(each_drive+":\\")
    print(vd_names)
    for each_drive in vd_names:
        for r, d, f in os.walk(each_drive):
            for each_f in f:
                if each_f.endswith(".png") or each_f.endswith(".jpg") or each_f.endswith(".jpeg") :
                    #copy imgs to another folder
                    newPath = shutil.copy(os.path.join(r, each_f), path_to_save)    
                    #store the path in file
                    f = open("results.txt", "a")
                    f.write(os.path.join(r, each_f))
                    f.write("\n")
                    f.close()


else:
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_f.endswith(".png") or each_f.endswith(".jpg") or each_f.endswith(".jpeg") :
                    #copy imgs to another folder
                    newPath = shutil.copy(os.path.join(r, each_f), path_to_save)    
                    #store the path in file
                    f = open("results.txt", "a")
                    f.write(os.path.join(r, each_f))
                    f.write("\n")
                    f.close()
