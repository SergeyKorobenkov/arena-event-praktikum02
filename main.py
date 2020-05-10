from game import Arena


def main():
    game = Arena.factory_standard()
    game.run()


if __name__ == '__main__':
    main()