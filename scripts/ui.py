import scripts.pygpen as pp
from scripts.deck import Deck

class CardUI(pp.ElementSingleton):
    def __init__(self, deck, custom_id=None):
        super().__init__(custom_id)
        
        self.tutorial = 0
        self.deck = deck
        
    def render(self):
        for idx, item in enumerate(self.deck.cards):
            if not self.deck.progress[idx] >= self.deck.kd[idx][0] - 0.1:
                pass    