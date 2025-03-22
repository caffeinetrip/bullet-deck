import scripts.pygpen as pp
from scripts.pygpen.utils.game_math import distance


class Enemy(pp.Entity):
    def __init__(self, speed, type, pos, target):
        super().__init__(type, pos)
        
        self.speed = 0
        self.speed_ = speed
        self.target_pos = target
        
    @property
    def img(self):
        return self.e['Assets'].images['enemy']['default']

    def update(self):
        if self.target_pos is None:
            return False
        
        if self.speed < self.speed_:
            self.speed += 0.005

        dx = self.target_pos[0] - self.pos[0]
        dy = self.target_pos[1] - self.pos[1]
        dist = distance(self.pos, self.target_pos)

        if dist == 0:
            return False

        direction_x = dx / dist
        direction_y = dy / dist

        step = self.speed

        self.pos[0] += direction_x * step
        self.pos[1] += direction_y * step

        if distance(self.pos, self.target_pos) <= step:
            self.pos = self.target_pos
            self.target_pos = None