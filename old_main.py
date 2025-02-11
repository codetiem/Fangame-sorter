import file_manager
import games_list_manager
import os

# --- functions to actually use ---
# create_fsort_files
# delete_fsort_files
# display_fsort_files
# get_fsort_attributes (uses a text file path)
# find_file_of_type
# open_game (absolute path)
game_directory = "D:\\Fangames\\Games\\_Next up\\I Wanna Be The Co-op"
program_directory = "D:\\Fangames\\Tools\\Fangame_Sort"

def main():

    file_manager.create_fsort_files(game_directory)
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
    games_all = file_manager.create_sortable_array(game_directory)
    
    # found = games_list_manager.search_tags_exclusive(games, ["Cancer", "Joke"])
    
    while(False):
        command = input("enter search")
        games = games_list_manager.search_maker(games_all, command)
        games_list_manager.list_games(games)
        game = choose_game(games)
        
        doing_game = False
        if game != "no":
            doing_game = True
        while (doing_game):
            choice = input("1 to run, 2 to edit, 3 to quit")
            if choice == "1":
                file_manager.open_game(game["ExePath"])
            elif choice == "2":
                print("epic fail")
            else:
                doing_game = False

    # print(games[1])
    
def choose_game(games):
    choice = input("pick a number from the list to select the game (any non valid answer will just cancel)")
    game_selected = "no"
    for num in range(len(games)):
        if choice == str(num):
            game_selected = games[num]
            break
    if game_selected != "no":
        games_list_manager.display_game_attributes(game_selected)
    
    return game_selected

if __name__ == "__main__":
    main()

