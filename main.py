"""
Фармакопея. Цивилизация и битва.
"""
from backoffice import create_persons, war_of_war


def game_over_show(winner) -> None:
    print('***** БОИ ЗАВЕРШЕНЫ *****')
    print()
    print(f'Победитель сезона определён!\n'
          f'{winner.name}!\n'
          f'Вспомним, в чём он пришёл на игры:\n'
          f'{", ".join(winner.things_titles)}.\n')
    print()
    print('Спасибо, что были с нами!')


def dawn_of_the_arena() -> None:
    """
    Функция-импрессарио. Организует подготовку воинов
    и проводит соревнования.
    """

    # 1.
    print(f'Здесь планировался вводный текст. Может быть даже смешной.\n'
          f'Однако, сценарист уснул, а режиссёр потерялся.\n'
          f'Что касается автора кода, то проведя бессонную ночь\n'
          f'он растерял и графоманские способности.\n'
          f'Поэтому, давайте без прелюдий. Сразу к делу!\n')

    # 2.
    warriors = create_persons()

    # 3.
    message = 'Отбор участников завершён. Познакомьтесь:'
    print('*' * len(message))
    print(message)
    for war in warriors:
        print(f'>>> {war.name} <<<\n'
              f'Обновки: {", ".join(war.things_titles)}.')
    print()
    input('Всё готово. Нажмите Enter, чтобы начать...')

    # 4.
    winner = war_of_war(warriors)

    # 5.
    game_over_show(winner)


if __name__ == '__main__':
    dawn_of_the_arena()
