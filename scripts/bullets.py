import scripts.pygpen as pp
import math, pygame

class Bullet(pp.Entity):
    def __init__(self, type, pos, angle=0):
        super().__init__(type, pos)
        
        self.speed = 1.5
        self.drad = angle
        self.angle = math.radians(angle) 

    @property
    def img(self):
        return pygame.transform.rotate((self.e['Assets'].images['bullet']['bullet']), self.drad)

    def update(self, enemys_rects=[]):
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed
        self.pos[0] += dx
        self.pos[1] += dy

        for enemy_rect in enemys_rects:
            if self.rect.colliderect(enemy_rect):
                return self.rect