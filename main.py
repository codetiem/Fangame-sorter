import os
import file_operations
from game import Game
import pickle_shit
import subprocess
games = []
excluded_exe = []
tags = set()
config = {
    "root" : ""
}


def main():
    try:
        load_data()
    except:
        print("No save data found! make sure to scan before anything!")
    menu()


def open_game(abs_path):
    subprocess.Popen(f"explorer /select,{abs_path}", cwd = os.path.join(abs_path, os.pardir))

#### menu functions
def menu():
    running = True
    while running:
        print("\n\nMenu!"+"*"*20+"Menu!")
        print("0 : all games")
        print("1 : select by name")
        print("2 : select by creator")
        print("3 : select by tags")
        print("4 : scan for new games!")
        print("5 : configure settings!")
        print("6 : stop running")

        selected_games = []
        ans = input("Choice: ")
        match ans:
            case "0":
                selected_games = games
            case "1":
                ans = input("Enter game name: ")
                selected_games = games_by_name(ans)
            case "2":
                creators = []
                ans = "the"
                while ans:
                    ans = input("Enter creator(s) (empty to cancel): ")
                    if ans:
                        creators.append(ans)
                selected_games = games_by_creator(creators)
            case "3":
                tag_list = []
                input_tags = set()
                print("Existing tags: ")
                for i, tag in enumerate(tags):
                    print(f"{i} {tag}")
                    tag_list.append(tag)

                ans = "the"
                while ans:
                    ans = input("Select tags by number (empty to cancel): ")
                    if ans:
                        input_tags.add(tag_list[int(ans)])
                selected_games = games_by_tags(input_tags)
            case "4":
                scan_games()
                save_data()
            case "5":
                config_menu()
            case "6":
                running = False

        if selected_games:
            for i, game in enumerate(selected_games):
                print("="*20 + "\n "+str(i))
                print(game)

            ans = input("Select a game! use number")
            try:
                ans = int(ans)
            except:
                print("that wasnt an integer!")
                ans = -1
            if ans >= 0 and ans < len(selected_games):
                game_actions(selected_games[(ans)])
        
        save_data()

def config_menu():
    print(f"Current root: {config["root"]}")
    set_root()


def game_actions(game):
    
    running = True
    while running:
        print("\nGame chosen is: ")
        print(game)
        print("\nChoose what to do with the game!: ")
        print("0 : run it")
        print("1 : remove it")
        print("2 : reset name")
        print("3 : reset creators")
        print("4 : reset tags")
        print("5: return to menu")
        ans = input("make choice")

        match ans:
            case "0":
                open_game(os.path.join(config["root"], game.exe_path))
            case "1":
                games.remove(game)
                running = False
            case "2":
                game.name = add_name(game.exe_path)
            case "3":
                game.creator = add_creators()
            case "4":
                game.tags = add_tags()
            case "5":
                running = False




def games_by_name(name):
    re = []
    for game in games:
        if name.lower().strip() in game.name.lower():
            re.append(game)

    return re

def games_by_creator(name):
    re = []
    for game in games:
        for creator in game.creator:
            for creator_search in name:
                if creator_search.lower().strip() in creator.lower():
                    re.append(game)

    return re

def games_by_tags(tags):
    re = []
    for game in games:
        if tags.intersection(game.tags):
            re.append(game)

    return re



#### general functions
def set_root():
    global config
    ans = input("set new path (empty to cancel):")
    if ans:
        config["root"] = os.path.abspath(ans)

def game_exists(path):
    for game in games:
        try: 
            if os.path.samefile(os.path.join(config["root"], game.exe_path), os.path.join(config["root"], path)):
                return True
        except:
            return False


    return False

def game_excluded(path):
    for excluded_path in excluded_exe:
        if os.path.samefile(excluded_path, path):
            return True
    return False

def add_game(path):
    relative_path = os.path.relpath(path, start=config["root"])
    game = Game(relative_path)

    name = add_name(path)
    game.name = name


    new_creator = add_creators()
    game.creator = new_creator

    new_tags = add_tags()
    game.tags = (new_tags)
    

    games.append(game)

def add_name(path):
    out = ""
    name = input("Enter name (defaults to filename): ")
    if name:
        out = name
    else: 
        # the filename without exe extension
        name = os.path.basename(path)[:-4]
        out = name
    return out


def add_creators():
    creators_out = set()
    creator = "the"
    while creator:
        creator = input("Enter creator(s) (empty to cancel): ")
        if creator:
            creators_out.add(creator)
    return creators_out
def add_tags():
    game_tags = set()
    tag_list = []
    print("Existing tags: ")
    for i, tag in enumerate(tags):
        print(f"{i} {tag}")
        tag_list.append(tag)

    ans = "the"
    while ans:
        ans = input("Add existing tag by number (empty to cancel): ")
        if ans:
            game_tags.add(tag_list[int(ans)])   

    ans = "the"
    while ans:
        ans = (input("Add new tags! (empty to cancel) "))
        if ans:
            game_tags.add(ans)
        
    tags.update(game_tags)
    return game_tags        


def yes(input):
    if input.lower().strip() == "y":
        return True
    return False

def scan_games():
    while not config["root"]:
        print("no root folder set! please set it so it can be scanned.")
        set_root()
    found = file_operations.find_file_of_type(config["root"], "exe")
    new_games = []
    for game_path in found:
        if not game_exists(game_path) and not game_excluded(game_path):
            new_games.append(game_path)
    
    if new_games:
        print(f"{len(new_games)} new games found.")

        for path in new_games:
            ans = input(f"Add this exe ?():  {os.path.basename(path)}")
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

##### loading data
def save_data():
    data = {
        "games" : games,
        "excluded" : excluded_exe,
        "tags" : tags,
        "config" : config,
    }
    pickle_shit.save_data(data)

def load_data():
    global games, excluded_exe, tags, config
    data = pickle_shit.load_data()

    games = data["games"]
    excluded_exe = data["excluded"]
    tags = data["tags"]
    config = data["config"]





if __name__ == "__main__":
    main()