import scripts.pygpen as pp
import math

class Bullet(pp.Entity):
    def __init__(self, type, pos, angle=0, health=1):
        super().__init__(type, pos)
        
        self.speed = 3 
        self.angle = math.radians(angle) 
        
        self.health = health
        
        self.outline = (40, 35, 40)

    @property
    def img(self):
        return self.e['Assets'].images['bullets']['bullet']

    def update(self):

        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        self.pos[0] += dx
        self.pos[1] += dy

        screen_w, screen_h = self.e['Window'].size
        if not (0 <= self.pos[0] <= screen_w and 0 <= self.pos[1] <= screen_h):
            self.destroy()