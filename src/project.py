import pygame
import random

class Flapping_avian():

    def __init__(self, pos = (0,0), size = 15):
        #GAME STATES
        self.spawned = False
        self.start = False
        #~~~~~~~~~~~~~~~~~~~
        #PLAYER SURFACE
        self.player = pygame.Rect(250, 300, 15, 15)
        self.size = size
        self.color = pygame.Color(255, 0, 0)
        self.surface = self.update_surface()
        #self.player_pos = (self.pos_x, self.pos_y)
        self.velocity = 0
        self.acceleration = 0.05
        self.dead = False
        #PLAYER STATES
        self.flapping = False
    #Game Loop
    def update (self, dt):
        if self.spawned == False:
            self.spawn_player(self)
        elif self.start == False:
            self.check_for_start()
        else:
           self.update_player(dt)

    def update_player(self, dt):
        self.detect_input()
        if self.flapping == True:
            self.flap(self)
            self.update_pos(dt)
            self.flapping = False
        else:
            self.update_pos(dt)
    
    #Game spawn/start
    def spawn_player(self, dt):
        self.spawned = True
        
    def check_for_start(self):
        self.detect_input()
        if self.flapping == True:
            self.start = True
            self.velocity = 5
            print("Bark")
    
    #Player visuals
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, screen):
        if self.dead:
            return
        pygame.draw.rect(screen, self.color, self.player)
        #self.surface.set_alpha(self.alpha)
        #surface.blit(self.surface, self.pos)

    #Input/player movement
    def detect_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("meow")
            self.flapping = True
            return self.flapping
    
    def gravity(self, dt):
        self.velocity = self.velocity + self.acceleration

    def update_pos(self, dt):
        self.gravity(self)
        self.player.y += self.velocity
        
    def flap(self, dt):
        self.velocity = -5


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
        dt=clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()