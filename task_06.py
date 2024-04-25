class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(list_players):
    # метод "Камень-Ножницы-Бумага"
    if len(list_players) > 2:
        raise WrongNumberOfPlayersError("Wrong number of players.")
    for item in list_players:
        if item[1] not in 'RSP':
            raise NoSuchStrategyError("No such strategy.")
    if list_players[0][1] == 'P':
        if list_players[1][1] == 'P':
            return f"{list_players[0][0]} {list_players[0][1]}"
        if list_players[1][1] == 'R':
            return f"{list_players[0][0]} {list_players[0][1]}"
        if list_players[1][1] == 'S':
            return f"{list_players[1][0]} {list_players[1][1]}"

    if list_players[0][1] == 'S':
        if list_players[1][1] == 'P':
            return f"{list_players[0][0]} {list_players[0][1]}"
        if list_players[1][1] == 'R':
            return f"{list_players[1][0]} {list_players[1][1]}"
        if list_players[1][1] == 'S':
            return f"{list_players[0][0]} {list_players[0][1]}"

    if list_players[0][1] == 'R':
        if list_players[1][1] == 'P':
            return f"{list_players[1][0]} {list_players[1][1]}"
        if list_players[1][1] == 'S':
            return f"{list_players[0][0]} {list_players[0][1]}"
        if list_players[1][1] == 'R':
            return f"{list_players[0][0]} {list_players[0][1]}"



print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) # => WrongNumberOfPlayersError
print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) # => NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) # => 'player1 P'