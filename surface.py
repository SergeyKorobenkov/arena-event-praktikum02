import pygame

colors = {
    'black': (0, 0, 0, 255),
    'white': (255, 255, 255, 255),
    'red': (255, 0, 0, 255),
    'green': (0, 125, 0, 255),
    'blue': (0, 0, 255, 255),
    'wooden': (153, 92, 0, 255),
}

background = pygame.image.load('images/background.png')
background_rect = background.get_rect()


class ScreenHandle(pygame.Surface):

    def __init__(self, *args, **kwargs):
        if len(args) > 1:
            self.successor = args[-1]
            self.next_coord = args[-2]
            args = args[:-2]
        else:
            self.successor = None
            self.next_coord = (0, 0)
        super().__init__(*args, **kwargs)
        # self.fill(colors['wooden'])
        self.set_alpha(0)
        self.game_engine = None

    def draw(self, canvas):
        if self.successor is not None:
            canvas.blit(self.successor, self.next_coord)
            self.successor.draw(canvas)

    def connect_engine(self, engine):
        self.game_engine = engine

        if self.successor is not None:
            self.successor.connect_engine(engine)


class ArenaSurface(ScreenHandle):
    def draw_info_message(self, message, top):
        font = pygame.font.SysFont('comicsansms', 30)
        text = font.render(message, True, colors['white'])
        place = text.get_rect(center=(background_rect.width / 2, top))
        self.blit(text, place)

    def draw(self, canvas):

        self.blit(background, background_rect)
        fighters = self.game_engine.fighters
        alive_persons = self.game_engine.alive_persons
        if len(fighters) == 2:
            if self.game_engine.fighting:
                self.game_engine.attack()
                font = pygame.font.SysFont('comicsansms', 30)
                self.blit(font.render(f'Раунд {self.game_engine.round_number}', True, colors['white']), (555, 350))

                self.draw_info_message(
                    f'{self.game_engine.attacker.name} наносит удар по {self.game_engine.defender.name}'
                    f' на {self.game_engine.attacker.damage} урона',
                    600
                )

            else:
                has_winner = self.game_engine.attacker.is_defeated
                if has_winner:
                    self.draw_info_message(
                        f'Бой завершен, победил {self.game_engine.defender.name}. '
                        f'Для продолжения нажмите Enter',
                        600
                    )
                else:
                    self.draw_info_message('Бой завершен. Победитель не выявлен. Для продолжения нажмите Enter', 600)

            pygame.draw.rect(self, colors['white'], (230, 50, 200, 30), 1)
            pygame.draw.rect(self, colors['green'], (231, 51, 1.98 * fighters[0].current_hp_percent, 28))
            pygame.draw.rect(self, colors['white'], (750, 50, 200, 30), 1)
            pygame.draw.rect(self, colors['green'], (751, 51, 1.98 * fighters[1].current_hp_percent, 28))

            font = pygame.font.SysFont('comicsansms', 25)
            self.blit(font.render(f'{fighters[0].info}', True, colors['white']), (230, 30))
            self.blit(font.render(f'{fighters[1].info}', True, colors['white']), (750, 30))

            person_1 = pygame.image.load('images/person_1.png')
            self.blit(person_1, (150, 230))

            person_2 = pygame.image.load('images/person_2.png')
            self.blit(person_2, (650, 200))

            font = pygame.font.SysFont('comicsansms', 20)

            fighter_things = fighters[0].things
            for i in range(len(fighter_things)):
                self.blit(font.render(fighter_things[i].info, True, colors['white']), (230, 16*i + 90))

            fighter_things = fighters[1].things
            for i in range(len(fighter_things)):
                self.blit(font.render(fighter_things[i].info, True, colors['white']), (750, 16*i + 90))

        elif not self.game_engine.is_game_over:
            self.draw_info_message('Чтобы начать бой нажмите пробел', 350)
        else:
            self.draw_info_message(f'Игра завершена, победил {alive_persons[0].name}', 350)

        font = pygame.font.SysFont('comicsansms', 25)
        self.blit(
            font.render(f'Участники', True, colors['white']),
            (30, 100))

        for i in range(len(alive_persons)):
            self.blit(font.render(f'{alive_persons[i].name}', True, colors['white']),
                      (30, 20*i + 130))

        super().draw(canvas)
