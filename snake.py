from random import randint
from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 900))

class SnakeModule:

    def __init__(self, direction, x, y, img):
        self.direction = direction
        self.x, self.y = x, y
        self.position = [self.x, self.y]
        self.img = pygame.image.load(img)

    def move(self):
        self.x += self.direction[0] * 30
        self.y += self.direction[1] * 30
        self.position = [self.x, self.y]

modules = [SnakeModule([0, 1], 0, 90, "snake module.png"), SnakeModule([0, 1], 0, 120, "snake module.png"), SnakeModule([0, 1], 0, 150, "snake head module.png")]
positions = [module.position for module in modules]
running = True
apple = {"img": pygame.image.load("apple.png"), "position": [300, 300]}

def update_modules():
    for i, module in enumerate(modules):
        if i != 0:
            modules[i - 1].direction = module.direction

free_positions = []

def move_apple():
    global modules
    i = 900 - len(positions)
    j = randint(0, i - 1)
    if positions[-1] == apple["position"]:
        apple["position"] = free_positions[j]
        new_module = SnakeModule(modules[0].direction, modules[0].x + modules[0].direction[0] * -30, modules[0].y + modules[0].direction[1] * -30, "snake module.png")
        modules = [new_module] + modules


while running:
    pygame.time.delay(100)
    positions = [module.position for module in modules]

    free_positions = []
    for i in range(0, 871, 30):
        for j in range(0, 871, 30):
            free_positions.append([j, i])
    for position in positions:
        if position in free_positions:
            free_positions.remove(position)
    
    if len(modules) + len(free_positions) != 900:
        exit()
    
    if free_positions == []:
        print("Yay you won!!!")
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if positions[-2] != [positions[-1][0] - 30, positions[-1][1]]:
                    modules[-1].direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                if positions[-2] != [positions[-1][0] + 30, positions[-1][1]]:
                    modules[-1].direction = [1, 0]
            elif event.key == pygame.K_UP:
                if positions[-2] != [positions[-1][0], positions[-1][1] - 30]:
                    modules[-1].direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                if positions[-2] != [positions[-1][0], positions[-1][1] + 30]:
                    modules[-1].direction = [0, 1]
    
    move_apple()
    
    screen.fill((0, 0, 0))
    for module in modules:
        module.move()
    update_modules()
    for module in modules:
        screen.blit(module.img, module.position)
    screen.blit(apple["img"], apple["position"])

    pygame.display.update()