import os

def find_file_of_type(path, type):
    found_files = []
    
    for root, dirs, files in os.walk(path):
    # select file name
        for file in files:
            # check the extension of files
            if file.endswith(type):
                
                # checks if file contains a excluded string
                # excluded = False
                # for name in exclusions:
                #     if name in file:
                #         excluded = True
                        
                found_files.append(os.path.join(root, file))

    return found_files
                
def create_fsort_files(paths):
    rootFolders = []
    for game_path in paths:
        rootFolders.append(find_main_folder(game_path))
    
    i = 0
    for path in rootFolders:
        if len(find_file_of_type(path, "fangameSort.txt")) <= 0:
            name = input("What is the games name?(n to not create a sort file) Exe: " + paths[i])
            
            if (name != "n"):
                f = open(path+"/fangameSort.txt", "w")
                f.write("Name: " + name + "\n")
                
        i += 1

# tries to find the root folder for a game. 
# This is because db helper usually burries 
# the exe file in an extra folder and i'd 
# rather have the sort file be in the root
def find_main_folder(path):
    
    bottom_folder_exe_amount = 0
    for files in os.listdir(path+"/.."):
        if files.endswith(".exe"):
            bottom_folder_exe_amount += 1
            
    multiple_exe = False
    
    while (not multiple_exe):
        if (len(find_file_of_type(path, ".exe")) > bottom_folder_exe_amount):
            multiple_exe = True
        path += "\.."
            
    return path[0:-6]

def delete_fsort_files(path):
    

    for root, dirs, files in os.walk(path):
    # select file name
        for file in files:
            # check the extension of files
            if file == "fangameSort.txt":
                
                os.remove(os.path.join(root, file))
                
def create_fsort_files_in_path(path):
    games = find_file_of_type(path, ".exe")
    create_fsort_files(games)
    
    
def display_fsort_files(path):
    fsorts = find_file_of_type(path, "fangameSort.txt")
    for fsort in fsorts:
        f = open(fsort)
        print(f.read())