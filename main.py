import sys
from settings import *
import player
from mapinclude import load_sqlite3_maps


def print_view(to_print: list) -> None:
    print("What you see:")
    print("┍━━━━━━┑")
    print("││".format(to_print[0]))
    print(f"│{to_print[1]}│")
    print(f"│{to_print[2]}│")
    print("┕━━━━━━┙")


def main() -> None:
    pl = player.Player()

    steps_cnt_global = 0

    if len(sys.argv) > 1:
        try:
            maplist = load_sqlite3_maps(sys.argv[1])
        except:
            try:
                maplist = load_sqlite3_maps("maps.db")
            except:
                print("\"maps.db\" not exist :(. You need some maps!")
                return
    else:
        try:
            maplist = load_sqlite3_maps("maps.db")
        except:
            print("\"maps.db\" not exist :(. You need some maps!")
            return

    for current_map in maplist:
        running = True
        pl.load_map(current_map)
        steps_cnt = 0
        to_print = pl.view_around()
        print("What you see:",
              "┍━━━━━━┑",
              f"│{to_print[0]}│",
              f"│{to_print[1]}│",
              f"│{to_print[2]}│",
              "┕━━━━━━┙", sep="\n")

        while running:
            action = input().strip().lower()
            action_result = pl.tick(action)

            if action_result == WIN:
                break
            elif action_result == ACT_EXIT:
                break
            print(action_result)
            to_print = pl.view_around()
            print("What you see:",
                  "┍━━━━━━┑",
                  f"│{to_print[0]}│",
                  f"│{to_print[1]}│",
                  f"│{to_print[2]}│",
                  "┕━━━━━━┙", sep="\n")
            steps_cnt += 1
            steps_cnt_global += 1
        if action_result == ACT_EXIT:
            break
        print(f"Nice! You passed this map in {steps_cnt} steps.")
    if action_result == WIN:
        print("Congratulations! You finished this maplist!")
        print("you used", steps_cnt_global, "steps to pass these maps")
        input("Press enter to close.")

if __name__ == '__main__':
    main()