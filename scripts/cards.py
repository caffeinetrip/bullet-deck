import importlib
import pygpen as pp

class Card(pp.Element):
    def __init__(self, key, custom_id=None, singleton=False, register=False):
        super().__init__(custom_id, singleton, register)
        
        self.key = key    
        self.function = self._load_function()
        
    def _load_function(self):
        module = importlib.import_module(self._name)
        function_class = getattr(module, self._name)
        return function_class

    def use_card(self):
        if self.function:
            instance = self.function()
            pass
        