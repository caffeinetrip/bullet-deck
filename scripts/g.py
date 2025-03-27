from scripts.enemy import Enemy
from scripts.deck import Deck
import scripts.pygpen as pp
import pygame, random, math

RECT_SIZE = (50, 50, 50, 50)

class G(pp.ElementSingleton):
    def __init__(self, custom_id=None):
        super().__init__(custom_id)
        
        player_pos = pp.io.read_json('data/hooks/data.json')['player_position']
        
        self.health = 3
        self.angle = None
        
        self.enemy_x_range = 300
        self.enemy_move = player_pos
        self.player_center = [player_pos[0]-25, player_pos[1]-50]
        
        self.player_rect = pygame.Rect(*RECT_SIZE)
        
        self.game_objects = pp.EntityGroups(quad_size=self.enemy_x_range*2, quad_groups=['bullets', 'enemies'])

        self.spawn_timer = 4.5
        self.spawn_interval = 5
        
        self.wave_timer = 0
        self.wave_interval = 21 
        self.wave = 0
        
        self.base_enemy_count = [3, 5]
        self.enemy_count = self.base_enemy_count.copy()
        self.base_enemy_speed = [10, 15]
        self.enemy_speed = self.base_enemy_speed.copy()
        
        self.deck = Deck()


    def deck_update(self, time):
        x = self.player_center[0] - 35

        for idx, item in enumerate(self.deck.cards):
            self.e['Renderer'].blit(item.img, [x, self.player_center[1]-10], group='game')

            if self.deck.card_cooldowns[idx] > 0:
                progress = round(time - self.deck.card_cooldowns[idx], 2)

                if progress >= self.deck.kd[idx][0] - 0.1:
                    if len(self.deck.kd[idx]) == 1:
                        self.deck.card_cooldowns[idx] = 0
                        self.deck.kd[idx][0] = 0
                    else:
                        self.deck.kd[idx].pop(0)
                else:
                    surf_height = (item.img.get_height()-2) * (1.0 - (progress / self.deck.kd[idx][0]))
                    surf_height = max(0, min(surf_height, item.img.get_height()-2))
                    surf = pygame.Surface([item.img.get_width()-2, surf_height])
                    surf.fill((10, 10, 10))
                    surf.set_alpha(80)
                    self.e['Renderer'].blit(surf, [x+2, self.player_center[1]-8], group='game')

            if (self.e['Input'].holding(self.deck.deck_binds[idx]) and 
                self.deck.card_cooldowns[idx] == 0 and 
                self.deck.kd[idx][0] == 0):
                self.angle = pp.game_math.calculate_angle(
                    pp.game_math.scale_mouse_pos(self.e['Mouse'].pos, self.e['Window'].dimensions, [340, 220]),
                    self.enemy_move
                )
            elif (self.e['Input'].released(self.deck.deck_binds[idx]) and 
                  self.deck.card_cooldowns[idx] == 0 and 
                  self.deck.kd[idx][0] == 0):
                for bullet in self.deck.card_use(idx, time, self.angle):
                    self.game_objects.add(bullet, 'bullets')

            x += 40
            
    def increase_wave_difficulty(self):
        self.enemy_count[0] += 1
        self.enemy_count[1] += 1
        self.spawn_interval += 1
        self.wave += 1
            
    def update(self, time):
        dt = self.e['Window'].dt
        
        self.spawn_timer += dt
        self.wave_timer += dt
        
        if self.spawn_timer >= self.spawn_interval or len(self.game_objects.get_rects('enemies')) == 0:
            used_x = []
            
            for _ in range(random.randint(*self.enemy_count)):
                enemy_x = pp.game_math.randint_excluding_ranges(40, self.enemy_x_range, used_x)
                speed = random.uniform(*self.enemy_speed) / 100
                enemy = Enemy(
                    speed, 
                    'enemy', 
                    [enemy_x, random.randint(10, 40)], 
                    self.enemy_move
                )
                self.game_objects.add(enemy, 'enemies')
                used_x.append([enemy_x-10, enemy_x+10])
                
            self.spawn_timer = 0
        
        if self.wave_timer >= self.wave_interval:
            self.increase_wave_difficulty()
            self.wave_timer = 0
            
        for particle in list(self.game_objects.kill_particles): 
            if particle.update(dt):
                self.game_objects.kill_particles.remove(particle)
            else:
                particle.renderz('game')

        self.game_objects.update(enemys_rects=self.game_objects.get_rects('enemies'))
        self.game_objects.render()
        self.deck_update(time)