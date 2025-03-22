from random import choice
from scripts.cards import Card

import scripts.pygpen as pp

CHANSE = {
    'one_bullet': [10, 1],
    'two_bullets': [3, 2],
    'three_bullets': [1, 3]
}

CARDS_SHUFFLE = []

for name, item in CHANSE.items():
    for i in range(item[0]):
        CARDS_SHUFFLE.append(name)
class Deck(pp.ElementSingleton):
    def __init__(self, custom_id=None):
        super().__init__(custom_id)
        
        self.cards = [None, None, None]
        self.kd = [[0],[0],[0]]
        self.max_kd = [0,0,0]
        self.card_cooldowns = [0, 0, 0]
        self.deck_binds = ["first_card", "second_card", "third_card"]
        
        self.shuffle('all')
        
    def card_use(self, idx, time, angle):
        data = self.cards[idx].use_card(angle)
        for i in range(3):
            self.card_cooldowns[i] = time
            self.kd[i].append(self.cards[idx].kooldown[0])
            self.max_kd[i] += self.cards[idx].kooldown[0]
        self.kd[idx][len(self.kd[idx])-1] += self.cards[idx].kooldown[1]
        self.max_kd[idx] += self.cards[idx].kooldown[1]
        self.shuffle(idx)
        return data
        
    def shuffle(self, card_i='all'):
        card_type = choice(CARDS_SHUFFLE)
        
        if card_i == 'all':
            for i in range(len(self.cards)):
                card_type = choice(CARDS_SHUFFLE)
                self.cards[i] = Card(i, card_type, rang=CHANSE[card_type][1])
                
            return

        self.cards[card_i] = Card(card_i, card_type, rang=CHANSE[card_type][1])