from scripts.enemy import Enemy
import scripts.pygpen as pp
import pygame

RECT_SIZE = (50, 50, 50, 50)

class G(pp.ElementSingleton):
    def __init__(self, player_pos, custom_id=None):
        super().__init__(custom_id)
        
        self.health = 3
        self.player_center = [player_pos[0]-25, player_pos[1]-50]
        
        self.player_rect = pygame.Rect(
            *RECT_SIZE
        )
        
        self.bullets = []
        self.enemys = []
        self.spawn_time = 0
        self.bounce = False
        
    def render(self, dt):
        
        surf = pygame.Surface((50,50))
        pygame.draw.rect(surf, (200,200,200), self.player_rect)
        
        if dt % 5 == 0 and not self.bounce:
            self.enemys.append(Enemy('bullets', [self.player_center[0]-100, self.player_center[1]-100], self.player_center))
            self.bounce = True
        if dt % 5 != 0 and self.bounce:
            self.bounce = False
        
        for bullet in self.bullets:
            bullet.update(dt)
        
        for enemy in self.enemys:
            enemy.update(dt)
        
        self.e['Renderer'].blit(surf, 
                                [self.player_center[0], self.player_center[1]],
                                group='ui')
            
