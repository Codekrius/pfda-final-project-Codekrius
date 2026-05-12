import pygame
import random

class Flapping_avian():

    def __init__(self, pos = (0,0), size = 15):
        #GAME STATES
        self.spawned = False
        self.start = False
        #GAME PHYSICS
        self.flap_strength = -10
        self.gravity_strength = 0.5
        #~~~~~~~~~~~~~~~~~~~
        #PLAYER SURFACE
        self.player = pygame.Rect(250, 300, 15, 15)
        self.size = size
        self.color = pygame.Color(0, 0, 255)
        self.surface = self.update_surface()
        self.velocity = 0
        self.dead = False
        #PLAYER STATES
        self.flapping = False
        #~~~~~~~~~~~~~~~~~~~
        #OBSTACLE STATS
        self.top = pygame.Rect(250, 300, 15, 15)
        self.gap = 200
        self.bottom = pygame.Rect(250, 300, 15, 15)
        self.bottom_size = (450 - self.gap)
        self.obstacle_speed = 5
        self.obstacle_timer_counter = 0
        self.obstacle_timer = 300 # 1 every x/dt
        self.obstacles = []
    
    #Game Loop
    def update (self, dt, screen):
        if self.spawned == False:
            self.spawn_player(self)
        elif self.start == False:
            self.check_for_start()
        else:
           self.update_player(dt)
           self.update_obstacles(screen, dt)

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
    
    #Player visuals
    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, screen):
        if self.dead:
            return
        pygame.draw.rect(screen, self.color, self.player)

    #Input/player movement
    def detect_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.flapping = True
            return self.flapping
    
    def gravity(self, dt):
        self.velocity = self.velocity + self.gravity_strength

    def update_pos(self, dt):
        if self.player.y <= 75 or self.player.y >= 510:
            self.dead = True
        else:
            self.gravity(self)
            self.player.y += self.velocity
        
    def flap(self, dt):
        self.velocity = self.flap_strength

        
    #Obstacles
    def update_obstacles(self, screen, dt):
        #self.obstacles_move(dt)
        self.obstacles_spawn_new(screen)

    def obstacles_move(self, dt):
        #update every obstacle in an index
        #each obstacle should move left some amount
        #check if obstacle is in player x
        self.obstacle_collide_x()
        #if so check if player lands within gap
        self.obstacle_collide_y()
        #if not, kill player
        #check if an obstacle is off screen
        self.obstacles_is_offscreen()
        #delete if offscreen
        pass

    def obstacle_collide_x():
        #check if obstacle lands within player's x
        pass

    def obstacle_collide_y():
        #check if player lands within gap space of obstacle's y
        #return boolean
        pass

    def obstacles_is_offscreen():
        #check if obstacle is past a certain x value
        #return a boolean
        pass

    def obstacles_spawn_new(self, screen):
        if self.obstacle_timer_counter >= self.obstacle_timer:
            self.random_height = random.randint(0, self.bottom_size)
            obstacle_top = pygame.draw.rect(screen, (255,0,0), pygame.Rect(785, (-375 + self.random_height), 15, 450))
            obstacle_bottom = pygame.draw.rect(screen, (255,0,0), pygame.Rect(785, (75 + self.gap + self.random_height), 15, (450 - self.gap)))
            self.obstacles.insert(0, obstacle_top)
            self.obstacles.insert(0, obstacle_bottom)
            self.obstacle_timer_counter = 0
        else:
            self.obstacle_timer_counter += 1
        #spawn new obstacle and add it to the list


#MAIN (INITIALIZE + LOOP)
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
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 800, 75))
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 525, 800, 75))
        flapping_avian.update(dt, screen)
        flapping_avian.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()