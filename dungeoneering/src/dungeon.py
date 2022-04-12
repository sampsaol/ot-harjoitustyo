import pygame
from random import randint

class Game:
    def __init__(self):
        pygame.init()

        ### Setting up all the basic variables we need
        self.load_pictures()
        self.level = 0
        self.health = 3
        self.points = 0
        self.difficulty = 1
        self.monster_list = []
        self.coin_list = []
        self.heart_list = []
        self.attacks = 5
        
        ### Screen size and title
        self.screen = pygame.display.set_mode((900,1000))
        self.font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Dungeoneering")        
        self.width, self.height = pygame.display.get_surface().get_size()
        self.scale = self.width//12

        



        self.new_game()

        self.loop()
        ### Function for loading pictures
    def load_pictures(self):
        self.pictures = []
        for picture in ["coin","door","hero","monster", "heart"]:
            self.pictures.append(pygame.image.load(f"src/{picture}.png"))
            self.pictures[-1] = pygame.transform.scale(self.pictures[-1], (75, 75))
        

        ### the basic set up for levels is a 12x12 matrix
    def new_game(self):
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
      
        ### getting different levels and difficulties by a randomly generated 12x12 map where door, at least for now, is always in the 
        ### upper right corner and the hero starts in the lower left corner
    def level_generator(self):
        self.level += 1
        self.attacks = 5
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.map[0][-1] = 2
        self.map[-1][0] = 3
        ### for now monsters spawned are defined to be 3 times the difficulty and coins are defined to be 5 times the difficulty
        monsters = self.difficulty*3
        coins = self.difficulty * 5
        hearts = 3
        ### 2 loops to make sure we don't get overlapping objects in the game while randomly generating the map
        for i in range(coins):
            if i < monsters:
                while True:
                    x = randint(0,11)
                    y = randint(0,11)
                    if self.map[y][x] == 0:
                        self.map[y][x] = 4
                        self.monster_list.append([y, x])
                        break
            if i < hearts:
                while True:
                    x = randint(0,11)
                    y = randint(0,11)
                    if self.map[y][x] == 0:
                        self.map[y][x] = 5
                        break
            while True:
                x = randint(0,11)
                y = randint(0,11)
                if self.map[y][x] == 0:
                    self.map[y][x] = 1
                    break
        
    
    ### a looping function to check what events have occured and to draw the screen
    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()
    ### function for all the events such as leave game or buttons pressed
    def check_events(self):
        for event in pygame.event.get():
            ### functionality for pressing down keys
            if event.type == pygame.KEYDOWN:
                if self.level != 0:
                    if event.key == pygame.K_LEFT:
                        self.move(0, -1, False)
                    if event.key == pygame.K_RIGHT:
                        self.move(0, 1, False)
                    if event.key == pygame.K_UP:
                        self.move(-1, 0, False)
                    if event.key == pygame.K_DOWN:
                        self.move(1, 0, False)

                    if event.key == pygame.K_SPACE:
                        self.move(0, 0, True)

                if event.key == pygame.K_ESCAPE:
                    exit()
                    ### Button press to initiate the first level
                if self.level == 0 and event.key == pygame.K_1:
                    self.level = 1
                    self.level_generator()
            if event.type == pygame.QUIT:
                exit()
    ### function to draw the screen, including the background as well as boxes for objects
    def draw_screen(self):
        self.screen.fill((0, 0, 128))

        for y in range((self.height-100)//self.scale+1):
            pygame.draw.line(self.screen, (255, 255, 0), (0, y*self.scale), (self.width, y*self.scale))
        for x in range((self.width//self.scale+1)):
            pygame.draw.line(self.screen, (255, 255, 0), (x*self.scale, 0), (x*self.scale, self.height-100))
        ### drawing the objects
        for y in range((self.height-100)//self.scale):
            for x in range(self.width//self.scale):
                box = self.map[y][x]-1
                if box >= 0:
                    self.screen.blit(self.pictures[box], (x*self.scale, y*self.scale))
        if self.level == 1:
            pygame.draw.line(self.screen, (0,255,255), (0, 300), (self.width, 300))
        ### drawing info on the bottom of the screen
        text = self.font.render(f"Health: {self.health}", True, (255, 255, 255))
        self.screen.blit(text, (30, self.height-50))
        text = self.font.render(f"Points: {self.points}", True, (255, 255, 255))
        self.screen.blit(text, (150, self.height-50))
        text = self.font.render(f"Level: {self.difficulty}", True, (255, 255, 255))
        self.screen.blit(text, (270, self.height-50))
        text = self.font.render(f"Attacks: {self.attacks}", True, (255, 255, 255))
        self.screen.blit(text, (390, self.height-50))
        text = self.font.render(f"Esc = exit {self.difficulty}", True, (255, 255, 255))
        self.screen.blit(text, (550, self.height-50))

        pygame.display.flip()
    ### function to get location of the hero
    def hero_location(self):
        for y in range((self.height-100)//self.scale):
            for x in range(self.width//self.scale):
                if self.map[y][x] == 3:
                    return (y,x)
    ### function that moves the hero and the monsters respectively
    def move(self, move_y, move_x, attack):
        hero_old_y, hero_old_x = self.hero_location()
        hero_new_y = hero_old_y + move_y
        hero_new_x = hero_old_x + move_x
        if hero_new_x < 0 or hero_new_y < 0 or hero_new_y >= (self.height-100)//self.scale or hero_new_x >= self.width//self.scale:
            return
               
        ### let's define attack and make sure it doesn't go out of bounds
        if attack and self.attacks > 0:
            self.attacks -= 1
            if hero_new_y+1 < self.width//self.scale:
                if self.map[hero_new_y+1][hero_new_x] == 4:
                    self.map[hero_new_y+1][hero_new_x] = 0
            if hero_new_y-1 >= 0:
                if self.map[hero_new_y-1][hero_new_x] == 4:
                    self.map[hero_new_y-1][hero_new_x] = 0
            if hero_new_x +1 < self.width//self.scale:
                if self.map[hero_new_y][hero_new_x+1] == 4:
                    self.map[hero_new_y][hero_new_x+1] = 0
            if hero_new_x-1 >= 0:
                if self.map[hero_new_y][hero_new_x-1] == 4:
                    self.map[hero_new_y][hero_new_x-1] = 0

        ### moving the monsters, choosing one at a time, to be made more efficient
        monster_new_y = -1
        monster_new_x = -1
        for y in range(len(self.map)):
            for x in range(len(self.map)):
                if self.map[y][x] == 4:
                    monster_old_y = y
                    monster_old_x = x

                    ### checking if the monster should move vertically or horizontally
                    if abs(monster_old_y-hero_new_y) >= abs(monster_old_x-hero_new_x):
                        if monster_old_y-hero_new_y > 0:
                            monster_new_y = monster_old_y-1
                            monster_new_x = monster_old_x
                        else:
                            monster_new_y = monster_old_y+1
                            monster_new_x = monster_old_x
                    else:
                        if monster_old_x-hero_new_x > 0:
                            monster_new_x = monster_old_x-1
                            monster_new_y = monster_old_y
                        else:
                            monster_new_x = monster_old_x+1
                            monster_new_y = monster_old_y
                    ### checking if monster collides with the hero
                    if monster_new_y == hero_new_y and monster_new_x == hero_new_x or monster_old_y == hero_new_y and monster_old_x == hero_new_x:
                        self.health -= 1
                        monster_new_y = -1
                        monster_new_x = -1
                        self.map[monster_old_y][monster_old_x] = 0
                        if self.health <= 0:
                            self.__init__()



        ### hero collides with a coin
        if self.map[hero_new_y][hero_new_x] == 1:
            self.map[hero_new_y][hero_new_x] = 0
            self.points += self.difficulty*10
        ### hero collides with a heart
        elif self.map[hero_new_y][hero_new_x] == 5:
            self.health += 1
            self.map[hero_new_y][hero_new_x] = 0
        ### hero finds the door, empty all the level sensitive lists
        elif self.map[hero_new_y][hero_new_x] == 2:
            self.difficulty += 1
            self.coin_list = []
            self.heart_list = []
            self.monster_list = []
            self.level_generator()
            return
        ### checking monster collisions and moving the monster
        if monster_new_y != -1:
            if self.map[monster_new_y][monster_new_x] == 1:
                self.coin_list.append((monster_new_y, monster_new_x))
                self.map[monster_new_y][monster_new_x] = 0
            elif self.map[monster_new_y][monster_new_x] == 5:
                self.heart_list.append((monster_new_y,monster_new_x))
                self.map[monster_new_y][monster_new_x] = 0
            elif self.map[monster_new_y][monster_new_x] == 2:
                monster_new_y += 1
            elif self.map[monster_new_y][monster_new_x] == 4:
                self.monster_list.append((monster_new_y,monster_new_x))
                self.map[monster_new_y][monster_new_x] = 0
            self.map[monster_new_y][monster_new_x] = 4
            self.map[monster_old_y][monster_old_x] = 0


        ### hero is finally moved
        if self.map[hero_new_y][hero_new_x] == 0:
            self.map[hero_old_y][hero_old_x] = 0
            self.map[hero_new_y][hero_new_x] = 3
    
        ### returning the coins that monsters have stood on    
        for object in self.coin_list:
            if self.map[object[0]][object[1]] == 0:
                self.map[object[0]][object[1]] = 1
                self.coin_list.remove(object)

        ### returning the hearts that monsters have stood on
        for object in self.heart_list:
            if self.map[object[0]][object[1]] == 0:
                self.map[object[0]][object[1]] = 5
                self.heart_list.remove(object)

        ### returning monsters that collided - bad idea, maybe discarded
        #for object in self.monster_list:
         #   if self.map[object[0]][object[1]] == 0:
          #      self.map[object[0]][object[1]] = 4
           #     self.monster_list.remove(object)

if __name__ == "__main__":
    game = Game()


            


        
