import pygpen as pp

class Spells(pp.Element):
    def __init__(self, custom_id=None, singleton=False, register=False):
        super().__init__(custom_id, singleton, register)