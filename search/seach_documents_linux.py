import os
import string
import platform
import shutil

#script to for linux/mac
#open a path origin and search files withends .pdf .docx .doc .txt

#path to begning the search, its recursively
#path_origin='/'
path_origin = '/Users/rodrigodutra/Downloads/atividade3/'

#path to save the results
path_to_save = '/Users/rodrigodutra/Desktop/pdfs-atividade3/'



def count_files_in_directory(path):
    DIR = path
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])



print("\nOpen a path origin and search files withends .pdf .docx .doc .txt \n")

print("1 - Run script\n2 - Clear results")
op = input("> ")

if(op == '1'):
    
    #verify is logs directory exists
    try:
         f = open(f"{path_to_save}/logs/results.txt", "a")
    
    except:
        parent_dir = path_to_save
        directory = 'logs'
        path = os.path.join(parent_dir, directory)
        os.mkdir(path) 
    

    #search the files in origin path and copy to path_to_save
    for r, d, f in os.walk(path_origin):
        for each_file in f:
            if each_file.endswith(".pdf") or each_file.endswith(".doc") or each_file.endswith(".txt") or each_file.endswith(".docx") :
                    #copy imgs to another folder
                    newPath = shutil.copy(os.path.join(r, each_file), path_to_save) 
                    #store the path in file
                    f = open(f"{path_to_save}/logs/results.txt", "a")
                    f.write(os.path.join(r, each_file))
                    f.write("\n")
    f.close() 
    
    
    print("Total Files in end directory: " + str(count_files_in_directory(path_to_save)))

               
                    
elif(op == '2'):
    #delete all files in folder result
    folder = path_to_save
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))    
    
    print("Folder is clear !")
