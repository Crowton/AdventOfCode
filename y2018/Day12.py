# #..#. => .
# ##... => #
# #.... => .
# #...# => #
# ...#. => .
# .#..# => #
# #.#.# => .
# ..... => .
# ##.## => #
# ##.#. => #
# ###.. => #
# #.##. => .
# #.#.. => #
# ##..# => #
# ..#.# => #
# ..#.. => .
# .##.. => .
# ...## => #
# ....# => .
# #.### => #
# #..## => #
# ..### => #
# ####. => #
# .#.#. => #
# .#### => .
# ###.# => #
# ##### => #
# .#.## => .
# .##.# => .
# .###. => .
# ..##. => .
# .#... => #

state = ".#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#"
# state = "#..#.#..##......###...###"

turnsTo = {}

for i in range(32):
    f, t = input().split(" => ")
    turnsTo[f] = t

offset = 0

becomes = {}

# for i in range(20):
for i in range(50000000000):
    if state in becomes:

        state, dO = becomes[state]
        offset += dO * (50000000000 - i)
        break

        # this comes to a steady state, where the state doesn't change

    else:
        bS = state
        bO = offset

        state = "...." + state + "...."
        state2 = ""
        for s in range(2, len(state) - 2):
            state2 += turnsTo[state[s-2:s+3]]
        state = state2.strip(".")

        for c in state2:
            if c == ".":
                offset -= 1
            else:
                break
        offset += 2

        becomes[bS] = (state, offset - bO)

s = 0

for i in range(0, len(state)):
    if state[i] == "#":
        s += i - offset

print(s)
