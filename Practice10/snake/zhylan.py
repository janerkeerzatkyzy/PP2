import pygame
from color_palette import *
import random
pygame.init()

w = 600
h = 600
cell = 30 #each square will be 30x30

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

score = 0
level = 1
FPS = 4

font = pygame.font.SysFont("Arial", 20)


def draw_grid():
    for i in range(h // cell):
        for j in range(w // cell):
            pygame.draw.rect(screen, colorGREEN, (i * cell, j * cell, cell, cell), 1) #draw small squares


class Point:
    def __init__(self, x, y): #column and row
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 11) , Point(10, 12), Point(10, 13)] #head, body, tail
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1): #body follows head, tail follows body
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def check_wall_collision(self):
        head = self.body[0]
        if head.x < 0 or head.x >= w // cell or head.y < 0 or head.y >= h // cell:
            return True
        return False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorWHITE, (head.x * cell, head.y * cell, cell, cell))

        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorBLUE, (segment.x * cell, segment.y * cell, cell, cell))

    def check_collision(self, food):
        global score
        head = self.body[0]

        if head.x == food.pos.x and head.y == food.pos.y:
            score += 1
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)


class Food:
    def __init__(self):
        self.pos = Point(5, 5)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * cell, self.pos.y * cell, cell, cell)) #drawing an apple

    def generate_random_pos(self, snake_body):
        while True:
            new_x = random.randint(0, w // cell - 1) #from 0 to 19, we have 20 grids
            new_y = random.randint(0, h // cell - 1)

            conflict = False
            for segment in snake_body:
                if segment.x == new_x and segment.y == new_y:
                    conflict = True
                    break

            if not conflict:
                self.pos.x = new_x
                self.pos.y = new_y
                break


snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBLGREEN)

    draw_grid()

    snake.move()

    if snake.check_wall_collision():
        print("GAME OVER")
        running = False

    snake.check_collision(food)

    if score != 0:
        level = score // 3 + 1

    snake.draw()
    food.draw()

    score_text = font.render(f"SCORE: {score}", True, colorWHITE)
    level_text = font.render(f"LEVEL: {level}", True, colorWHITE)

    screen.blit(score_text, (20, 10))
    screen.blit(level_text, (20, 25))

    pygame.display.flip()
    clock.tick(FPS + level * 2) #increase speed with level
pygame.quit()