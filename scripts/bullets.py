import scripts.pygpen as pp
import math

class Bullet(pp.Entity):
    def __init__(self, type, pos, angle=0, health=1):
        super().__init__(type, pos)
        
        self.speed = 0.5
        self.angle = math.radians(angle) 
        
        self.health = health
        
        self.outline = (40, 35, 40)

    @property
    def img(self):
        return self.e['Assets'].images['bullet']['bullet']

    def update(self):
        print(self.angle)
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        self.pos[0] += dx
        self.pos[1] += dy