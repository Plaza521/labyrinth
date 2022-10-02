from settings import *
from mapinclude import load_map

class Player:
	def __init__(self):
		self.xpos = 1
		self.ypos = 1
	@property
	def pos(self):
		return (self.xpos,self.ypos)

	def load_map(self,mapname):
		pos, self.gamemap = load_map(mapname)
		self.xpos = pos[0]
		self.ypos = pos[1]

	def tick(self, action):
		gamemap = self.gamemap
		if action in ACT_UP:
			if '#' != gamemap[self.ypos-1][self.xpos]:
				self.ypos -= 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action in ACT_DOWN:
			if '#' != gamemap[self.ypos+1][self.xpos]:
				self.ypos += 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action in ACT_LEFT:
			if '#' != gamemap[self.ypos][self.xpos-1]:
				self.xpos -= 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action in ACT_RIGHT:
			if '#' != gamemap[self.ypos][self.xpos+1]:
				self.xpos += 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action == ACT_EXIT:
			return ACT_EXIT
		return "Error :(. Use command \"up\"('u'), \"down\"('d'), \"left\"('l') or \"right\"('r'). Also use \"exit\" command to leave from game"

	def view_around(self):
		gamemap = self.gamemap

		to_print_ln = 0
		to_print = ["","",""]
		for line in range(self.ypos-1,self.ypos+2):
			for column in range(self.xpos-1,self.xpos+2):
				if gamemap[line][column] == "#": to_print[to_print_ln] += "██"
				elif gamemap[line][column] == "W": to_print[to_print_ln] += "WN"
				else: to_print[to_print_ln] += '  '
			to_print_ln+=1
		return to_print