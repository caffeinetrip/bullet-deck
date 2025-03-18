import pygpen as pp
import math

class Bullet(pp.Entity):
    def __init__(self, *args, angle=0, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.speed = 3 
        self.angle = math.radians(angle) 
        
        self.outline = (40, 35, 40)

    @property
    def img(self):
        return self.e['Assets'].images['bullets'][self.type]

    def update(self, dt):

        dx = math.cos(self.angle) * self.speed * dt
        dy = math.sin(self.angle) * self.speed * dt

        self.pos[0] += dx
        self.pos[1] += dy

        screen_w, screen_h = self.e['Window'].size
        if not (0 <= self.pos[0] <= screen_w and 0 <= self.pos[1] <= screen_h):
            self.destroy()
