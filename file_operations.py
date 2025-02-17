import os



# returns a list of the paths of all files that end with the type string
def find_file_of_type(path, type) -> list:
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