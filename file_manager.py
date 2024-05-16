import os
import subprocess

# returns a list of the paths of all files that end with the type string
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

     
     
def create_fsort_files_at_path(paths):
    rootFolders = []
    for game_path in paths:
        rootFolders.append(find_main_folder(game_path))
    
    i = 0
    for path in rootFolders:
        if len(find_file_of_type(path, "fangameSort.txt")) <= 0:
            # checks if you want to create an fsort for that exe, and if so adds name
            name = input("What is the games name?(n to not create a sort file) Exe: " + paths[i])
            
            if (name.lower() == "n"):
                i += 1
                continue
            
                
            f = open(path+"/fangameSort.txt", "w")
            # adds game path 
            f.write("ExePath:" + paths[i] + "\n")
                
            f.write("Name:" + name + "\n")
            
            # adds the maker name(s)
            makers = ""
            
            maker_input = input("What is the games maker(s)?(s to stop adding makers) Exe: " + paths[i])
            while maker_input.lower() != "s":
                if len(makers) > 0:
                    makers += ","
                makers += maker_input
                maker_input = input("What is the games maker(s)?(s to stop adding makers) Exe: " + paths[i])

            f.write("Maker(s):" + makers + "\n")
           
           # adds tags     
            tags = input("Add a tag?(s to stop adding tags) Exe: " + paths[i])
            
            tag_input = input("Add a tag?(s to stop adding tags) Exe: " + paths[i])
            while tag_input.lower() != "s":
                if len(tags) > 0:
                    tags += ","
                tags += tag_input
                tag_input = input("Add a tag?(s to stop adding tags) Exe: " + paths[i])
                
            f.write("Tags:" + tags + "\n")
                
            
            f.close()        
        i += 1
    

# tries to find the root folder for a game. 
# This is because db helper usually burries 
# the exe file in an extra folder and i'd 
# rather have the sort file be in the root['D:\\Fangames\\Games\\_Next up\\I Wanna Be The Co-op\\dxwebsetup.exe\\..']
def find_main_folder(path):
    bottom_folder_exe_amount = 0
    for files in os.listdir(os.path.join(path, os.pardir)):
        if files.endswith(".exe"):
            bottom_folder_exe_amount += 1
            
    multiple_exe = False
    
    while (not multiple_exe):
        if (len(find_file_of_type(path, ".exe")) > bottom_folder_exe_amount):
            multiple_exe = True
        path = os.path.join(path, os.pardir)
            
    return path[0:-6]

def delete_fsort_files(path):
    

    for root, dirs, files in os.walk(path):
    # select file name
        for file in files:
            # check the extension of files
            if file == "fangameSort.txt":
                
                os.remove(os.path.join(root, file))
                
def create_fsort_files(path):
    games = find_file_of_type(path, ".exe")

    create_fsort_files_at_path(games)
    
    
def display_fsort_files(path):
    fsorts = find_file_of_type(path, "fangameSort.txt")
    for fsort in fsorts:
        f = open(fsort)
        # print(f.read())
        f.readline()
        print(f.readline()[0:-1])
        print(f.readline()[0:-1])
        print(f.readline())
        

def parse_fsort_line(line):
    data = []
    i = -1
    for char in line:
        if i < 0:
            if char == ":":
                i = 0
        else:
            if char == ",":
                i += 1
            else:
                if len(data) <= i:
                    data.append("")   
                if char != "\n" :
                    data[i] += char 
    
    if len(data) == 1:
        data = data[0]
    return data  
 
def get_fsort_attributes(txt_file_path):
    data_list = {}
    f = open(txt_file_path, "r")
    
    for line in f:
        key = ""
        idx = 0
        for char in line:
            idx += 1
            if char == ":":
                key = line[:idx-1]
                break
        
        data = parse_fsort_line(line)
        data_list[key] = data
        
    return data_list

def open_game(abs_path):
    subprocess.Popen(abs_path, cwd = os.path.join(abs_path, os.pardir))
        
# creates dictionary objects that can be easily used by the program by reading and parsing fsort files
def create_sortable_array(path):
    games_list = []
    fsorts = find_file_of_type(path, "fangameSort.txt")
    
    for fsort in fsorts:
        data = {"txt": fsort}
        data.update( get_fsort_attributes(fsort))
        if not os.path.exists(data["ExePath"]):
            data["ExePath"] = exe_path_fix(data)
            # TODO edit the actual files exe path to be write, and make a function to allow editing a fsort file value of course.
        
        games_list.append(data)
         
    return games_list

# attempts tp set a new exe path value, by going to the txt file and finding an exe with the same name in the files
def exe_path_fix(game_dict):
    folder_path = os.path.join(game_dict["txt"], os.pardir)
    game_name = os.path.basename(game_dict["ExePath"])
    
    
    for root, dirs, files in os.walk(folder_path):
    # select file name
        for file in files:
            # check if the name is the name
            if file == game_name:
    
                        
                return (os.path.join(root, file))

    print("exe not found. oh no")
     
        
        
        
        
# string = "Name: I Wanna Save My Boy"
# print(string[6:])
# print(get_fsort_attributes(r"D:\Fangames\Games\trash ngl\brute of man\fangameSort.txt"))