from __future__ import annotations

import logging
import sys

from typing import List, Optional

from generate_persons import generate_persons, get_random_index
from generate_things import dress_things
from models.person import Person

LOG_CONSOLE_FORMAT = "%(asctime)s - %(message)s"
log_datetime_format = "%Y-%m-%d %H:%M:%S"
log_stdout_handler = logging.StreamHandler(sys.stdout)
log_stdout_handler.setFormatter(logging.Formatter(fmt=LOG_CONSOLE_FORMAT,
                                                  datefmt=log_datetime_format))
log_file_handler = logging.FileHandler(filename='log.txt')
log_file_handler.setFormatter(logging.Formatter(fmt=LOG_CONSOLE_FORMAT,
                                                datefmt=log_datetime_format))
logging.basicConfig(level=logging.INFO,
                    handlers=[log_stdout_handler, log_file_handler])

log = logging.getLogger(__name__)


def prepare_persons(count: int) -> List[Person]:
    persons = generate_persons(count)
    for person in persons:
        dress_things(person)
    return persons


def prepare_battle(participants_count: int = 10) -> Battle:
    participants = prepare_persons(participants_count)
    return Battle(participants)


class Battle:
    def __init__(self, life_participants):
        self.life_participants: List[Person] = life_participants
        self.death_participants: List[Person] = []
        self.winner: Optional[Person] = None

    @property
    def life_participants_count(self):
        return len(self.life_participants)

    def start(self) -> Person:
        log.info('Сегодня для вас выступят:')
        for participant in self.life_participants:
            log.info(participant.extended_info())
        round_index = 1
        log.info('Битва началась, выживет только один!')
        while not self.winner:
            log.info(f'Начало {round_index} раунда,'
                     f' в живых {self.life_participants_count}')

            for participant in self.life_participants:
                strike_name = 'удар'
                enemies = participant.get_enemies(self.life_participants)
                enemy_index = get_random_index(enemies)
                enemy = enemies[enemy_index]
                outgoing_damage, critical = participant.deal_damage()
                final_damage = enemy.take_damage(outgoing_damage)
                if critical:
                    strike_name = 'критический удар'
                log.info(f'{participant} наносит {strike_name} по {enemy}'
                         f' на {final_damage} урона')
                if enemy.is_dead:
                    log.info(f'{participant} убивает {enemy}')
                    self.death_participants.append(enemy)
                    self.life_participants.remove(enemy)
                if self.life_participants_count == 1:
                    log.info(f'Is the winner is {participant}')
                    self.winner = participant
            round_index += 1

        log.info(f'Битва окончена, победил {self.winner.extended_info()}')
        return self.winner


battle = prepare_battle(10)
battle.start()





