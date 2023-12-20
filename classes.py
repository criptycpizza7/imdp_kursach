from simpy.core import Environment
from simpy import Resource

from typing import Final

from consts import *


fixed_tabs = [[(NUM_OF_FIRST, 0)], [(NUM_OF_SECOND, 0)], [(NUM_OF_THIRD, 0)]]

env = Environment()
workshop = Resource(env, capacity=20) # предположим, что в мастерской 20 мест
q = 0

workshop_stats = [(0, 0)]
q_stats = [(0, 0)]

num_of_tablets = [(NUM_OF_FIRST + NUM_OF_SECOND + NUM_OF_THIRD, 0)]


class Tablet():

    def __init__(self, env: Environment, type: int = 1, name: str = 'undefined'):
        
        self.env = env

        self.TYPE: Final[int] = type

        self.name = name

        match self.TYPE:
            case 1:
                self.m = 480
                self.sig = 95

                self.KR = 480
                self.CR = 220
                self.TR = 24
                
                
                self.rasprs = [0, 0, 480, 220, 24]
                self.FIXED = 0.2

            case 2:
                self.m = 410
                self.sig = 80

                self.KR = 370
                self.CR = 200
                self.TR = 18

                self.rasprs = [0, 0, 370, 200, 18]
                self.FIXED = 0.9

            case 3:
                self.m = 360
                self.sig = 70

                self.KR = 320
                self.CR = 180
                self.TR = 16

                self.rasprs = [0, 0, 320, 180, 16]
                self.FIXED = 1
            
        self.current_state = STATES['working']

        self.action = env.process(self.run())

    
    def run(self):
        global q_stats, q

        from random import gauss, uniform
        from numpy.random import exponential

        while self.current_state != STATES['broken']:
            yield self.env.timeout(int(gauss(self.m, self.sig)))

            if fixed_tabs[self.TYPE - 1][-1][0] - 1 >= 0:
                fixed_tabs[self.TYPE - 1].append((fixed_tabs[self.TYPE - 1][-1][0] - 1, self.env.now))


            br = uniform(0, 1)

            if br < BROKEN:
                self.current_state = STATES['broken']
            if BROKEN <= br < BROKEN + KP:
                self.current_state = STATES['KP']
            if BROKEN + KP <= br < BROKEN + KP + CP:
                self.current_state = STATES['CP']
            if BROKEN + KP + CP <= br:
                self.current_state = STATES['TP']

            if self.current_state == STATES['broken']:
                break
            
            while self.current_state != STATES['working']:

                if self.current_state == STATES['KP'] or self.current_state == STATES['CP']:
                    req = workshop.request()
                    q += 1
                    yield req
                    q -= 1
                    workshop_stats.append((workshop.count, self.env.now))
                    q_stats.append((q, self.env.now))

                yield self.env.timeout(int(exponential(self.rasprs[self.current_state])) * 3)
                
                if self.current_state == STATES['KP'] or self.current_state == STATES['CP']:
                    yield workshop.release(req)
                    workshop_stats.append((workshop.count, self.env.now))

                fix = uniform(0, 1)

                if fix < self.FIXED:
                    fixed_tabs[self.TYPE - 1].append((fixed_tabs[self.TYPE - 1][-1][0] + 1, self.env.now))
                    self.current_state = STATES['working']
