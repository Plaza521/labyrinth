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
		if action == ACT_UP:
			if '#' != gamemap[self.ypos-1][self.xpos]:
				self.ypos -= 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action == ACT_DOWN:
			if '#' != gamemap[self.ypos+1][self.xpos]:
				self.ypos += 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action == ACT_LEFT:
			if '#' != gamemap[self.ypos][self.xpos-1]:
				self.xpos -= 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		if action == ACT_RIGHT:
			if '#' != gamemap[self.ypos][self.xpos+1]:
				self.xpos += 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("
		return "Error :(. Use command \"up\", \"down\", \"left\" or \"down\""

	def view_around(self):
		gamemap = self.gamemap
		to_print = ["","",""]
		if gamemap[self.ypos-1][self.xpos-1] == "#": to_print[0]  = "██"
		elif gamemap[self.ypos-1][self.xpos-1] == "W": to_print[0]  = "WN"
		else: to_print[0]  = '  '
		if gamemap[self.ypos-1][self.xpos] == "#": to_print[0] += "██"
		elif gamemap[self.ypos-1][self.xpos] == "W": to_print[0] += "WN"
		else: to_print[0] += '  '
		if gamemap[self.ypos-1][self.xpos+1] == "#": to_print[0] += '██'
		elif gamemap[self.ypos-1][self.xpos+1] == "W": to_print[0] += 'WN'
		else: to_print[0] += '  '
		if gamemap[self.ypos][self.xpos-1] == "#": to_print[1] += '██'
		elif gamemap[self.ypos][self.xpos-1] == "W": to_print[1] += 'WN'
		else: to_print[1] += '  '
		if gamemap[self.ypos][self.xpos] == "#": to_print[1] += '██'
		elif gamemap[self.ypos][self.xpos] == "W": to_print[1] += 'WN'
		else: to_print[1] += '  '
		if gamemap[self.ypos][self.xpos+1] == "#": to_print[1] += '██'
		elif gamemap[self.ypos][self.xpos+1] == "W": to_print[1] += 'WN'
		else: to_print[1] += '  '
		if gamemap[self.ypos+1][self.xpos-1] == "#": to_print[2] += '██'
		elif gamemap[self.ypos+1][self.xpos-1] == "W": to_print[2] += 'WN'
		else: to_print[2] += '  '
		if gamemap[self.ypos+1][self.xpos] == "#": to_print[2] +='██'
		elif gamemap[self.ypos+1][self.xpos] == "W": to_print[2] +='WN'
		else: to_print[2] += '  '
		if gamemap[self.ypos+1][self.xpos+1] == "#": to_print[2] += '██'
		elif gamemap[self.ypos+1][self.xpos+1] == "W": to_print[2] += 'WN'
		else: to_print[2] += '  '
		return to_print