class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):

    if len(players) != 2:
        raise WrongNumberOfPlayersError()

    for player in players:
        if player[1] not in ["R", 'P', 'S']:
            raise NoSuchStrategyError()

    player_1, move_1 = players[0][0], players[0][1]
    player_2, move_2 = players[1][0], players[1][1]

    if move_1 == move_2:
        return str(players[0][0]) + ' ' + str(players[0][1])
    elif (move_1 == 'R' and move_2 == 'S') or \
         (move_1 == 'S' and move_2 == 'P') or \
         (move_1 == 'P' and move_2 == 'R'):
        return str(players[0][0]) + ' ' + str(players[0][1])
    else:
        return str(players[1][0]) + ' ' + str(players[1][1])
