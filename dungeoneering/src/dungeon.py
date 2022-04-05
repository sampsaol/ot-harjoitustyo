import pygame

class Game:
    def __init__(self):
        pygame.init()


        self.level = 0
        self.health = 3
        self.points = 0

        self.screen = pygame.display.set_mode((1300,1000))
        self.font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Dungeoneering")        
        self.load_pictures()

        self.new_game()

        self.loop()

    def load_pictures(self):
        self.pictures = []
        for picture in ["coin","door","hero","monster", "heart"]:
            self.pictures.append(pygame.image.load(picture + ".png"))


    def new_game(self):
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def loop(self):
        while True:
            self.check_events()
            self.draw_screen()

    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass
