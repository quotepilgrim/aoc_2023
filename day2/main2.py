import re

games = "input"
powers = []


def parse_game(game):
    expr = "Game .*: (.*)"
    match = re.search(expr, game)
    game = match.group(1).split(";")  # type: ignore

    min_cubes = {"red": 0, "green": 0, "blue": 0}

    for stage in game:
        turns = stage.split(", ")
        for turn in turns:
            count, color = turn.split()
            count = int(count)
            if count > min_cubes[color]:
                min_cubes[color] = count

    result = 1
    for i in min_cubes.values():
        result = result * i

    return result


with open(games, "r") as f:
    for line in f:
        result = parse_game(line)
        powers.append(result)

print(powers, sum(powers))
