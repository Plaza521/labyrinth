# labyrinth

For players:

You need to get to the WN cell
---

Movement is done with these commands:  
  right - move right  
  left  - move left  
  down  - move down  
  up    - move up  

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