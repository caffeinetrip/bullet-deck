from scripts.spells.spell_global_class import Spells

class three_bullets(Spells):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def use(self):
        print('Three bullets!')
        self.destroy()