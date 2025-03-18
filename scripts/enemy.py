import pygpen as pp

class Enemy(pp.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.speed = 1
        self.target_pos = None 
        
        self.outline = (40, 35, 40)
        
    @property
    def img(self):
        return self.e['Assets'].images['enemy'][self.type]
    
    def set_target(self, target_pos):
        self.target_pos = list(target_pos)
    
    def update(self, dt):
        if self.target_pos is None:
            return False

        dx = self.target_pos[0] - self.pos[0]
        dy = self.target_pos[1] - self.pos[1]
        dist = pp.distance(self.pos, self.target_pos)

        if dist == 0:
            return False

        direction_x = dx / dist
        direction_y = dy / dist

        step = self.speed * dt

        self.pos[0] += direction_x * step
        self.pos[1] += direction_y * step

        if pp.distance(self.pos, self.target_pos) <= step:
            self.pos = self.target_pos
            self.target_pos = None
        
        self.renderz()