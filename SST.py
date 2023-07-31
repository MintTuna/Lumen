import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Animation Test")

clock = pygame.time.Clock()
character = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Lumen/images/PlayerSheet(6).png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (width / 2) - (character_width / 2)
character_y_pos = (height / 2) - (character_height / 2)
character_speed = 0.6
to_x = 0
to_y = 0
dx, dy = 96, 96

ph = 0


running = True
while running:
    dt = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
                ph = 0
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                ph = 1
            elif event.key == pygame.K_UP:
                to_y -= character_speed
                if ph ==0:
                    ph = 2
                elif ph == 5:
                    ph = 3
                elif ph == 1:
                    ph = 3
                else:
                    ph = 2
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
                if ph == 0:
                    ph = 4
                elif ph == 2:
                    ph = 4
                else:
                    ph = 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    screen.fill((0, 0, 0))
    screen.blit(character, (character_x_pos, character_y_pos), (dx * ph, 0, dx, dy))
    pygame.display.update()
pygame.quit()