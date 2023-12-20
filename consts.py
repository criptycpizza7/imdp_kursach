from typing import Final
from random import randint

SEED: Final[int] = randint(1, 1000)

DAYS: Final[int] = 365

NUM_OF_FIRST: Final[int] = 36
NUM_OF_SECOND: Final[int] = 54
NUM_OF_THIRD: Final[int] = 72

BROKEN: Final[float] = 0.12
KP: Final[float] = 0.13
CP: Final[float] = 0.25
TP: Final[float] = 0.5

STATES: Final[dict] = {'working': 1,            # возмжные состояния планшетов
                        'KP': 2,
                        'CP': 3,
                        'TP': 4,
                        'broken': 5}
