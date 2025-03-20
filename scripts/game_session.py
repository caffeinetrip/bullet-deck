from scripts.enemy import Enemy
from scripts.deck import Deck
import scripts.pygpen as pp
import pygame, random

RECT_SIZE = (50, 50, 50, 50)

class G(pp.ElementSingleton):
    def __init__(self, player_pos, custom_id=None):
        super().__init__(custom_id)
        
        self.health = 3
        self.enemy_move = player_pos
        self.player_center = [player_pos[0]-25, player_pos[1]-50]
        
        self.player_rect = pygame.Rect(
            *RECT_SIZE
        )
        
        self.bullets = []
        self.enemys = []
        self.spawn_time = 0
        self.bounce = False
        
        self.deck = Deck()
        self.kd = 1
        self.card_cooldowns = [0, 0, 0]
        self.deck_binds = [	"first_card", "second_card", "third_card"]
        
        self.enemy_range_count = [3, 5]

    def deck_update(self, dt):
        x = self.player_center[0] - 20
        for idx, item in enumerate(self.deck.cards):
            self.e['Renderer'].blit(item.img, [x, self.player_center[1]], group='game')
            
            if self.card_cooldowns[idx] > 0:
                progress = round(dt-self.card_cooldowns[idx], 1)
                
                if progress >= self.kd:
                    self.card_cooldowns[idx] = 0
                else:
                    surf = pygame.Surface([item.img.get_width(), item.img.get_height()*(1.0-progress)])
                    surf.fill((1,0,0))
                    self.e['Renderer'].blit(surf, [x, self.player_center[1]], group='ui', alpha=20)
                
            if self.e['Input'].pressed(self.deck_binds[idx]) and self.card_cooldowns[idx] == 0:
                self.deck.cards[idx].use_card()
                for i in range(3):
                    self.card_cooldowns[i] = dt
                self.deck.shuffle(idx)
                
            x += 25
        
    def update(self, dt):
        if dt % 5 == 0 and not self.bounce:
            for _ in range(random.randint(self.enemy_range_count[0], self.enemy_range_count[1])):
                self.enemys.append(Enemy((random.randint(10, 15)) / 100, 'enemy', [random.randint(40, 300), random.randint(50, 100)], self.enemy_move))
            self.bounce = True
            
        if dt % 5 != 0 and self.bounce:
            self.bounce = False
        
        for bullet in self.bullets:
            bullet.update()
        
        for enemy in self.enemys:
            enemy.update()
        
        self.deck_update(dt)
