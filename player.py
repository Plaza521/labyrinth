from settings import *


class Player:
    def __init__(self):
        self.xpos = 1
        self.ypos = 1

    @property
    def pos(self):
        return (self.xpos, self.ypos)

    def load_map(self, current_map: list) -> None:
        self.xpos = current_map[0][0]
        self.ypos = current_map[0][1]
        self.gamemap = current_map[1]

    def _check_collision(self, ypos: int, xpos: int, direct: int) -> str:
        if '#' != self.gamemap[ypos][xpos]:
            if UP_NUM == direct:
                self.ypos -= 1
            if DOWN_NUM == direct:
                self.ypos += 1
            if LEFT_NUM == direct:
                self.xpos -= 1
            if RIGHT_NUM == direct:
                self.xpos += 1
            if 'W' == self.gamemap[self.ypos][self.xpos]:
                return WIN
            return OK
        else:
            return "You cant move to wall :("

    def tick(self, action: str) -> str:

        old_xpos = self.xpos
        old_ypos = self.ypos

        if action in ACT_UP:
            try:
                self.ypos -= 1
                self.view_around()
            except IndexError:
                self.ypos = old_ypos
                return ACT_LOOR
            self.ypos += 1

            return self._check_collision(self.ypos - 1,
                                         self.xpos,
                                         UP_NUM)

        if action in ACT_DOWN:
            try:
                self.ypos += 1
                self.view_around()
            except IndexError:
                self.ypos = old_ypos
                return ACT_LOOR
            self.ypos -= 1

            return self._check_collision(self.ypos + 1,
                                         self.xpos,
                                         DOWN_NUM)

        if action in ACT_LEFT:
            try:
                self.xpos -= 1
                self.view_around()
            except IndexError:
                self.xpos = old_xpos
                return ACT_LOOR
            self.xpos += 1

            return self._check_collision(self.ypos,
                                         self.xpos - 1,
                                         LEFT_NUM)

        if action in ACT_RIGHT:
            try:
                self.xpos += 1
                self.view_around
            except IndexError:
                self.xpos = old_xpos
                return ACT_LOOR
        self.xpos -= 1

        return self._check_collision(self.ypos,
                                     self.xpos + 1,
                                     RIGHT_NUM)

        if action == ACT_EXIT:
            return ACT_EXIT
        return "Error :(. Use command \"up\"('u'), \"down\"('d'), \
\"left\"('l') or \"right\"('r'). Also use \"exit\" command to leave from game"

    def view_around(self) -> list:
        gamemap = self.gamemap

        to_print_ln = 0
        to_print = ["", "", ""]
        for line in range(self.ypos - 1, self.ypos + 2):
            for column in range(self.xpos - 1, self.xpos + 2):
                if gamemap[line][column] == "#":
                    to_print[to_print_ln] += "██"
                elif gamemap[line][column] == "W":
                    to_print[to_print_ln] += "WN"
                else:
                    to_print[to_print_ln] += '  '
            to_print_ln += 1
        return to_print
