test_list = [{'txt': 'D:\\Fangames\\Games\\trash ngl\\brute of man\\fangameSort.txt', 'ExePath': 'D:\\Fangames\\Games/trash ngl\\brute of man\\I wanna be a brute of a man.exe', 'Name': 'I wanna be a brute of a man', 'Maker(s)': 'Yamizora', 'Tags': ['Needle', 'Impossible', 'Cancer']}, {'txt': 'D:\\Fangames\\Games\\trash ngl\\fuck kamilia\\fangameSort.txt', 'ExePath': 'D:\\Fangames\\Games/trash ngl\\fuck kamilia\\I Wanna Fuck Kamilia.exe', 'Name': 'I Wanna Fuck Kamilia', 'Maker(s)': 'Chris', 'Tags': ['Needle', 'Medley', 'Joke', 'Cancer']}, {'txt': "D:\\Fangames\\Games\\trash ngl\\I don't wanna download this game\\fangameSort.txt", 'ExePath': "D:\\Fangames\\Games/trash ngl\\I don't wanna download this game\\I Don't Wanna Download This Game.exe", 'Name': "I Don't Wanna Download This Game", 'Maker(s)': 'Leehee', 'Tags': 'Joke'}, {'txt': 'D:\\Fangames\\Games\\trash ngl\\i wanna be the chokochoko\\fangameSort.txt', 'ExePath': 'D:\\Fangames\\Games/trash ngl\\i wanna be the chokochoko\\i wanna be the chokochoko.exe', 'Name': 'i wanna be the chokochoko', 'Maker(s)': 'oboro', 'Tags': ['Joke', 'Short']}, {'txt': 'D:\\Fangames\\Games\\trash ngl\\I wanna L\\fangameSort.txt', 'ExePath': 'D:\\Fangames\\Games/trash ngl\\I wanna L\\I wanna L ver1.3.exe', 'Name': 'I wanna L', 'Maker(s)': 'lie', 'Tags': ['Needle', 'L_Needle', 'Cancer']}, {'txt': 'D:\\Fangames\\Games\\trash ngl\\I wanna trial the 100trap\\fangameSort.txt', 'ExePath': 'D:\\Fangames\\Games/trash ngl\\I wanna trial the 100trap\\I wanna trial the 100trap.exe', 'Name': 'I wanna trial the 100trap', 'Maker(s)': 'Yamizora', 'Tags': ['Needle', 'One_Jump', 'Cancer']}]

"Yamizora" in test_list[0]["Maker(s)"]
def search_name(games, name):
    return_list = []
    for game_dict in games:
        if game_dict["Name"] == name:
            return_list.append(game_dict)
    return return_list

def search_maker(games, maker):
    return_list = []
    for game_dict in games:
        # TODO i think this might be broken because makers can be just one value i believe?
        if maker in game_dict["Maker(s)"]:
            return_list.append(game_dict)
    return return_list

def search_tags_inclusive(games, tags):
    return_list = []
    for game_dict in games:
        checking = True
        i = 0
        while checking and i < len(tags):
            if tags[i] in game_dict["Tags"]:
                return_list.append(game_dict)
                checking = False
            i += 1
            
    return return_list

def search_tags_exclusive(games, tags):
    return_list = []
    for game_dict in games:
        contains = True
        for tag in tags:
            if not(tag in game_dict["Tags"]):
                contains = False
                break
        if contains:
            return_list.append(game_dict)
    return return_list

def list_games(games):
    print_string = ""
    i=0
    for game in games:
        print_string += str(i) + "." + game["Name"] + "\n"
        i+=1
    print(print_string) 
    
    
        

def display_game_attributes(game):
    for thing in game:
        if thing != "txt" and thing != "ExePath":
            pstring = thing + ": "
            if type(game[thing]) is list:
                for item in game[thing]:
                    pstring += item + ", "
                pstring = pstring[0:-2]
            else:
                pstring += game[thing]
            print(pstring + "\n")
        
        
        
type(['Needle', 'Medley', 'Joke', 'Cancer'])
type(['Needle', 'Medley', 'Joke', 'Cancer']) == list

# found_games=search_tags(test_list, ["Needle","Joke"])
# for game in found_games:
#     print(game["Name"])