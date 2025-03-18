from random import choice
import pygpen as pp

CARDS_TYPES = ['one_bullet', 'two_bullets', 'three_bullets']

class Deck(pp.ElementSingleton):
    def __init__(self, custom_id=None):
        super().__init__(custom_id)
        
        self.cards = [None, None, None]
        self.shuffle('all')
        
    def shuffle(self, card_i='all'):
        if card_i == 'all':
            for i in self.cards:
                self.cards[i] = choice(CARDS_TYPES)
        else:
            self.cards[card_i] = choice(CARDS_TYPES)
