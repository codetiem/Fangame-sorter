import sqlite3

def main():
    con = sqlite3.connect('fangame_sort.db')
    cur = con.cursor()

if __name__ == "__main__":
    main()