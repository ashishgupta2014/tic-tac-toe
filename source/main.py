from source.game import Game


def main():
    print('-------Tic Tac Toe Game-------')
    size = 3
    game = Game(size)
    players = [('Muskan', 'O'), ('Atul', 'X')]
    game.add_players(players)
    game.start()


if __name__ == "__main__":
    main()
