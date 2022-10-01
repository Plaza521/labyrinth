def load_map(mapname):
	with open(mapname,'r') as mapfile:
		startpos = list(map(int,mapfile.readline().split()))
		filemap = mapfile.readlines()
		gamemap = []
		gamemap.append('#'*(len(filemap[0])+2))
		for line in filemap:
			gamemap.append(f"#{line[:-1]}#")
		gamemap.append('#'*(len(filemap[0])+2))
		return startpos,gamemap

def load_maplist():
	with open("maplist.cfg", 'r') as maplist:
		return maplist.readline().split()