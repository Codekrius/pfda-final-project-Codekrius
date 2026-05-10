import pygame
import random


class Player():

    def __init__(self, pos=(100, 100), size=15):
        self.size = size
        self.color = pygame.Color(255, 0, 0)
        self.alpha = 255
        self.pos = pos
        self.velocity = 0
        self.acceleration = 0
        self.dead = False
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)

class Flapping_avian():
    
    def __init__(self, pos):
        self.pos = pos
        self.player_size = 15
        self.does_not_exist = True
        self.player = Player(self.pos)

    def update (self, dt):
        self.spawn_player()
        self.update_player(dt)
        
    def update_player(self, dt):
        #UPDATE PLAYER POSITION
        return

    def spawn_player(self):
        if self.does_not_exist:
            self.does_not_exist = False
            return self.player
        return
    
    def draw(self, surface):
        self.player.draw(surface)



def main():
    pygame.init()
    pygame.display.set_caption("Flapping Avian")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    flapping_avian = Flapping_avian(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        flapping_avian.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        flapping_avian.draw(screen)
        pygame.display.flip()
        dt=clock.tick(12)
    pygame.quit()
            
#Start
#Game doesn't start until input detected

#Player
#Add a function to detect input from player
#Add velocity variable that moves the player
#Add acceleration variable that alters velocity (gravity)
#When game detects input from player set velocity to positive value and acceleration back to 0

#Obstacles
#Add kill floor/ceiling (grab player location, if is outside range player dies.)
#


#Collision
#

if __name__ == "__main__":
    main()