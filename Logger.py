class Logger:
    def __init__(self):
        pass

    def Notify(self, eventType: str, args={}):
        if eventType == 'start':
            print(f"Да начнется великая битва\n")
        elif eventType == 'packed':
            print(f"Арена наполнена смертниками\n")
        elif eventType == 'armed':
            print(f"Подвезли вещичек\n")
        elif eventType == 'distributed':
            print(f"Вещи распределены, приготовьтесь\n")
        elif eventType == 'attack':
            print(
                f"{args['attacker']} наносит удар по "
                f"{args['defender']} на {args['dmg']} урона\n"
            )
        elif eventType == 'death':
            print(
                f"===\n{args['defender']}, не в силах терпеть муки "
                f"жизни, решил больше не жить\n===\n"
            )
        elif eventType == 'victory':
            print(
                f"{args['victor']} справился. Но ненадолго. Начинаем заново\n")
        elif eventType == 'custom':
            print(f"{args['message']}")
