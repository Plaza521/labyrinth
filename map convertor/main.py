import sqlite3
import os


def load_map(mapname: str) -> list:
    with open(mapname, 'r') as mapfile:
        startpos = list(map(int, mapfile.readline().split()))
        filemap = mapfile.readlines()
        gamemap = []
        gamemap.append('#'*(len(filemap[0])+2))
        for line in filemap:
            gamemap.append(f"#{line[:-1]}#")
        gamemap.append('#'*(len(filemap[0])+2))
        return startpos, gamemap


def append_zeros(number: int, outlen: int=5) -> str:
    return f"\"{'0'*(outlen-len(str(number))) + str(number)}\""


def list_to_string(list_in: list) -> str:
    return '"' + "".join([elem + ' ' for elem in list_in])[:-1] + '"'


def main() -> None:
    os.system("del maps.db")

    with open("maplist.cfg", 'r') as maplist1:
        maplist = maplist1.readline().split()

    mapid = 0

    for path in maplist:
        startpos, gamemap = load_map(path)
        outmap = []
        for line in gamemap:
            outmap.append(line.replace(" ", ".").replace("#","A"))

        conn = sqlite3.connect('maps.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS maps(
            mapid INT,
            startx INT,
            starty INT,
            mapinfo TEXT);
        """)
        conn.commit()
        maps_map = (append_zeros(mapid),
                    append_zeros(startpos[0]),
                    append_zeros(startpos[0]),
                    list_to_string(outmap))
        cur.execute("""INSERT INTO maps(mapid, startx, starty, mapinfo)
           VALUES({}, {}, {}, {});""".format('00003',
                                             append_zeros(startpos[0]),
                                             append_zeros(startpos[0]),
                                             list_to_string(outmap)))
        conn.commit()
        mapid += 1

if __name__ == '__main__':
    main()
