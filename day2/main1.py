import re

games = "input"
max_cubes = {"red": 12, "green": 13, "blue": 14}
valid_games = []


def parse_game(game):
    result = True
    expr = "Game (.*): (.*)"
    match = re.search(expr, game)

    game_id = int(match.group(1))  # type: ignore
    game = match.group(2).split(";")  # type: ignore

    for stage in game:
        turns = stage.split(", ")
        for turn in turns:
            count, color = turn.split()
            if int(count) > max_cubes[color]:
                result = False

    return game_id, result


with open(games, "r") as f:
    for line in f:
        game_id, result = parse_game(line)
        if result:
            valid_games.append(game_id)


print(valid_games, sum(valid_games))
