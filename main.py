import file_manager
import os

# --- functions to actually use ---
# create_fsort_files
# delete_fsort_files
# display_fsort_files
# get_fsort_attributes (uses a text file path)
# find_file_of_type
# open_game (absolute path)
game_directory = "D:\Fangames\Games\\trash ngl"

def main():

    
    # file_manager.create_fsort_files(program_directory)    
    # file_manager.delete_fsort_files(program_directory)
    # file_manager.display_fsort_files(game_directory)
    # # os.startfile("D:\Fangames\Games/trash ngl/brute of man\I wanna be a brute of a man.exe")
    # # fsorts = file_manager.find_file_of_type(program_directory, "fangameSort.txt")
    # # attributes = file_manager.get_fsort_attributes(fsorts[0])
    # # print(attributes)
    # # os.startfile(attributes[0][0])
    # # os.startfile(os.path.join("D:\Fangames\Games\\trash ngl\\brute of man\I wanna be a brute of a man.exe"), cwd = "D:\Fangames\Games\\trash ngl\\brute of man\I wanna be a brute of a man.exe/..")
    # directory = "D:\Fangames\Games\\trash ngl\\brute of man\I wanna be a brute of a man.exe"
    # file_manager.open_game(directory)
    games = file_manager.create_sortable_array(game_directory)
    print(games)
    

if __name__ == "__main__":
    main()
