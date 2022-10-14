import sqlite3
from sqlite3 import Error


def load_sqlite3_maps(path: str) -> list:
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")
    cur = connection.cursor()

    cur.execute("SELECT * FROM maps;")
    maps = cur.fetchmany(65535)
    outmaplist = []

    for mapid in range(len(maps)):
        insertlist = []
        current_map = maps[mapid]
        insertlist.append(tuple([current_map[1], current_map[1]]))
        gamemap = current_map[3].split()
        outline = []
        for line in gamemap:
            outline.append(line.replace('.', ' '))
        insertlist.append(outline)
        outmaplist.append(insertlist)
    return outmaplist
