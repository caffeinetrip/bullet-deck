from random import choice
from scripts.cards import Card

import scripts.pygpen as pp

CHANSE = {
    'one_bullet': 10,
    'two_bullets': 3,
    'three_bullets': 1
}

CARDS_SHUFFLE = []

for name, item in CHANSE.items():
    for i in range(item):
        CARDS_SHUFFLE.append(name)
class Deck(pp.ElementSingleton):
    def __init__(self, custom_id=None):
        super().__init__(custom_id)
        
        self.cards = [None, None, None]
        self.shuffle('all')
        
    def shuffle(self, card_i='all'):
        if card_i == 'all':
            for i in range(len(self.cards)):
                card_type = choice(CARDS_SHUFFLE)
                
                self.cards[i] = Card(i, card_type)
                
            return

        self.cards[card_i] = Card(card_i, card_type)