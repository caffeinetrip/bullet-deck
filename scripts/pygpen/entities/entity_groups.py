import pygame

from ..utils.elements import ElementSingleton
from ..data_structures.entity_quads import EQuads

class EntityGroups(ElementSingleton):
    def __init__(self, quad_size=64, quad_groups=[]):
        super().__init__()
        self.groups = {}
        self.locked = False
        self.add_queue = []
        
        self.z = 0
        
        self.quad_groups = set(quad_groups)
        self.equads = EQuads(quad_size=quad_size)
        
    def set_quad_groups(self, quad_groups=[]):
        self.quad_groups = set(quad_groups)
        
    # def get_rects(self, group_name):
    #     if group_name in self.groups:
    #         for item in self.groups[group_name]:
    #             yield item.rect
    #     else: return []
        
    def get_rects(self, group_name):
        enemys_rect = []
        
        if group_name in self.groups:
            for item in self.groups[group_name]:
                enemys_rect.append(item.rect)
        
        return enemys_rect
        
    def add(self, entity, group):
        if self.locked:
            self.add_queue.append((entity, group))
        else:
            # two insert cases depending on whether the group is spatially partitioned
            if group in self.quad_groups:
                self.equads.insert(entity, egroup=group)
            else:
                if group not in self.groups:
                    self.groups[group] = []
                self.groups[group].append(entity)
    
    def update(self, group=None, unlock=True, quad_rect=pygame.Rect(0, 0, 100, 100), enemys_rects=None):

        # update active entities based on quads (only applies when doing a general update)
        if len(self.quad_groups) and not group:
            self.equads.update_active(quad_rect)
            # update local group listing based on spatial partitioning
            self.groups.update(self.equads.active_entities)
            
        self.locked = True
        if group:
            if group in self.groups:
                for entity in self.groups[group].copy():
                    
                    if group == 'bullets':
                        kill = entity.update(enemys_rects=enemys_rects)
                    else:
                        kill = entity.update(self.bullets_colide)
                        
                    if kill:
                        if group == 'bullets':
                            self.bullets_colide.append(kill)
                        else:
                            self.bullets_colide.remove(kill)
                        
                        self.groups[group].remove(entity)
                        # delete from quads if applicable
                        if group in self.quad_groups:
                            self.equads.delete(entity)
        else:
            for group in self.groups:
                self.update(group, unlock=False, enemys_rects=enemys_rects)
        if unlock:
            self.locked = False
            if len(self.add_queue):
                for addition in self.add_queue:
                    self.add(*addition)
                self.add_queue = []
    
    def render(self, group=None, offset=(0, 0)):
        if group:
            if group in self.groups:
                for entity in self.groups[group]:
                    entity.renderz(offset=offset)
        else:
            for group in self.groups:
                self.render(group=group, offset=offset)
    
    def renderz(self, group=None, render_group='default', offset=(0, 0)):
        if group:
            if group in self.groups:
                for entity in self.groups[group]:
                    entity.renderz(group=render_group, offset=offset)
        else:
            for group in self.groups:
                self.renderz(group=group, render_group=render_group, offset=offset)