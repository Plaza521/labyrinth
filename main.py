from settings import *
import player
from mapinclude import load_maplist

def main():
	pl = player.Player()

	steps_cnt_global = 0

	for mapname in load_maplist():
		running = True
		pl.load_map(mapname)
		steps_cnt = 0
		to_print = pl.view_around()
		print("What you see:","┍━━━━━━┑",f"│{to_print[0]}│",f"│{to_print[1]}│",f"│{to_print[2]}│","┕━━━━━━┙",sep="\n")

		while running:
			action = input().strip().lower()
			action_result = pl.tick(action)
			if action_result == WIN: break
			print(action_result)
			to_print = pl.view_around()
			print("What you see:","┍━━━━━━┑",f"│{to_print[0]}│",f"│{to_print[1]}│",f"│{to_print[2]}│","┕━━━━━━┙",sep="\n")
			steps_cnt += 1
			steps_cnt_global += 1
		print("Nice! You passed this map in",steps_cnt,"steps.")
	print("Congratulations! You finished this maplist!")
	print("you used", steps_cnt_global, "steps to pass these maps")

if __name__ == '__main__':
	main()
