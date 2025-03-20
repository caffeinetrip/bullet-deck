import importlib
import scripts.pygpen as pp

class Card(pp.Element):
    def __init__(self, key_index, type, custom_id=None, singleton=False, register=False):
        super().__init__(custom_id, singleton, register)
        
        self.type = type
        
        self.key = key_index
        self.class_ref = self._load_class()
        
    @property
    def img(self):
        return self.e['Assets'].images['cards'][self.type]
        
    def _load_class(self):
        module = importlib.import_module(f'scripts.spells.{self.type}')
        class_obj = getattr(module, self.type)
        return class_obj
    
    def use_card(self):
        instance = self.class_ref([0,0], None)
        instance.use() 