import os
import file_operations
from game import Game
games = []
excluded_exe = []
root = os.path.abspath(r"C:\Users\slime\Fangames\I wanna")

def main():
    scan_games()
    for game in games:
        print(game)

def game_exists(path):
    for game in games:
        if os.path.samefile(game.path, path):
            return True
    return False

def game_excluded(path):
    for excluded_path in excluded_exe:
        if os.path.samefile(excluded_path, path):
            return True
    return False

def add_game(path):
    relative_path = os.path.relpath(path, start=root)
    game = Game(relative_path)

    name = input("Enter name: ")
    if name:
        game.name = name

    creator = input("Enter creator: ")
    if creator:
        game.creator = creator
    

    games.append(game)


def yes(input):
    if input.lower().strip() == "y":
        return True
    return False

def scan_games():
    found = file_operations.find_file_of_type(root, "exe")
    new_games = []
    for game_path in found:
        if not game_exists(game_path) and not game_excluded(game_path):
            new_games.append(game_path)
    
    if new_games:
        print(f"{len(new_games)} new games found.")

        for path in new_games:
            ans = input(f"Add this exe ?(y/n):  {os.path.basename(path)}")
            if yes(ans):
                add_game(path)
            else:
                ans = input("Add to excluded? (y/n)")
                if yes(ans):
                    excluded_exe.append(path)
                
            exit = input("Stop loop? (y/n)")
            if yes(exit):
                break
    else:
        print("No new games found")






if __name__ == "__main__":
    main()