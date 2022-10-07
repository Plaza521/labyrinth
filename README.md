# labyrinth

For players:  

To run game you need run main.py (or main.exe in release), enter mapname at argument, without arguments game load "maps.db".  

You need to get to the WN cell
---

Movement is done with these commands:  
  right(or d) - move right  
  left(or a)  - move left  
  down(or s)  - move down  
  up(or w)    - move up  

Alse game have an "exit" command for exit from game.

For map creators:
---

The first line is the player's starting position, starting at 1  
Example: "1 1" - player starts at top right corner  

The following lines is a maze  
  \# - wall  
  W - win  

exaxmple of map:
```
2 2
  #####
      #
# ### #
#   # #
# #####
#     #
#####W#
```

To load map you need to write path to it in file "maplist.cfg".  
To write several maps in a row, enter them in a line, separating them with a space  

After creating maplist you need to convert it to sqlite3 database through convertor from "map convertor" folder:  
just copy your "maplist.cfg" with maps to this folder, and run main.py (or main.exe in release)  
