import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

radius = 5
color = (255, 0, 0)
mode = "draw"  # draw, rect, circle, erase (by def - draw)

drawing = False
start_pos = None

screen.fill((255, 255, 255)) 

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
                print("COLOR CHANGED TO RED")
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
                print("COLOR CHANGED TO GREEN")
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
                print("COLOR CHANGED BLUE")
            elif event.key == pygame.K_d:
                color = (0, 0, 0)
                print("COLOR CHANGED TO BLACK")

            elif event.key == pygame.K_1:
                mode = "draw"
                print("MODE CHANGED TO DRAW")
            elif event.key == pygame.K_2:
                mode = "rect"
                print("MODE CHANGED TO RECT")
            elif event.key == pygame.K_3:
                mode = "circle"
                print("MODE CHANGED TO CIRCLE")
            elif event.key == pygame.K_e:
                mode = "erase"
                print("MODE CHANGED TO ERASE")

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, rect, 4)

            elif mode == "circle":
                end_pos = event.pos
                radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius_circle, 4)

        if event.type == pygame.MOUSEMOTION and drawing:

            if mode == "draw":
                pygame.draw.circle(screen, color, event.pos, radius)

            elif mode == "erase":
                pygame.draw.circle(screen, (255, 255, 255), event.pos, radius * 5)

    pygame.display.flip()
    clock.tick(60)