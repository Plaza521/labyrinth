from settings import *

class Player:
	def __init__(self):
		self.xpos = 1
		self.ypos = 1
	@property
	def pos(self):
		return (self.xpos,self.ypos)

	def load_map(self,current_map):
		self.xpos = current_map[0][0]
		self.ypos = current_map[0][1]
		self.gamemap = current_map[1]

	def tick(self, action):

		gamemap = self.gamemap

		def collision(ypos, xpos, direct):
			if '#' != gamemap[ypos][xpos]:
				if UP_NUM == direct: self.ypos -= 1
				if DOWN_NUM == direct: self.ypos += 1
				if LEFT_NUM == direct: self.xpos -= 1
				if RIGHT_NUM == direct: self.xpos += 1
				if 'W' == gamemap[self.ypos][self.xpos]: return WIN
				return OK
			else:
				return "You cant move to wall :("


		if action in ACT_UP:
			return collision(self.ypos-1, self.xpos, UP_NUM)
		if action in ACT_DOWN:
			return collision(self.ypos+1, self.xpos, DOWN_NUM)
		if action in ACT_LEFT:
			return collision(self.ypos, self.xpos-1, LEFT_NUM)
		if action in ACT_RIGHT:
			return collision(self.ypos, self.xpos+1, RIGHT_NUM)
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