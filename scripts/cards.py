import importlib
import scripts.pygpen as pp

class Card(pp.Element):
    def __init__(self, key_index, type, rang=1, custom_id=None, singleton=False, register=False):
        super().__init__(custom_id, singleton, register)
        
        self.type = type
        self.rang = rang
        
        self.key = key_index
        self.class_ref = self._load_class()
        
    @property
    def img(self):
        return self.e['Assets'].images['cards'][self.type]
       
    @property
    def kooldown(self):
        if self.rang == 1:
            return [0.75, 0.075]
        elif self.rang == 2:
            return [1.5, 0.15]
        elif self.rang == 3:
            return [3.0, 0.3] 
        
    def _load_class(self):
        module = importlib.import_module(f'scripts.spells.{self.type}')
        class_obj = getattr(module, self.type)
        return class_obj
    
    def use_card(self, angle):
        instance = self.class_ref(angle)
        return instance.use() 