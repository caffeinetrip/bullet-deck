import scripts.pygpen as pp

class Spells(pp.Element):
    def __init__(self, pos, objects, angle=0, custom_id=None, singleton=False, register=False):
        super().__init__(custom_id, singleton, register)
        
        self.per_use_time = 0.1
        
        self.pos = pos
        self.angle = angle
        
        self.object_function = self.use()
        self.objects = objects
        
    def use(self):
        print('Spell is used!')