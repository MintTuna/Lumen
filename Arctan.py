import pygame
import math 
import random

pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("SpriteSheet")

clock = pygame.time.Clock()

#=============================클래스=============================#
class IMG:
  def __init__(self, img, x, y):
    self.img = pygame.image.load(f"C:/Users/woota/OneDrive/바탕 화면/Pygame/Lumen/images/{img}.png")
    self.size = self.img.get_rect().size
    self.width = self.size[0]
    self.height = self.size[1]
    self.x = x
    self.y = y
#===============================================================#

player = IMG('PlayerSheet(6)', 252, 252)
player.width = player.size[0] / 6
player_speed = 0.6
to_x = 0
to_y = 0
dx, dy = 96, 96
frame_index = 0

spear = IMG('spear', -64, -64)
speedtrue = True
rotatespear = pygame.transform.rotate(spear.img, 45)
gameOver = 0

temp = math.gcd((abs(spear.y - player.y)), (abs(spear.x - player.x)))
s_speed_y = abs(spear.y - player.y) / temp
s_speed_x = abs(spear.x - player.x) / temp

divide_x = s_speed_x / math.gcd(int(s_speed_x), int(s_speed_y))
divide_y = s_speed_y / math.gcd(int(s_speed_x), int(s_speed_y))
if divide_x > 10:
    i=0
    while True:
        i+=1
        divide_x = divide_x / 10
        if divide_x <= 10:
            break
    divide_y = (divide_y / 10**i) * 2 
    divide_x = divide_x * 2

if divide_x < 5:
    divide_x = divide_x * 2
    divide_y = divide_y * 2

running = True
while running:
    dt = clock.tick(120)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
                frame_index = 0
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed
                frame_index = 1
            elif event.key == pygame.K_UP:
                to_y -= player_speed
                if frame_index ==0:
                    frame_index = 2
                elif frame_index == 5:
                    frame_index = 3
                elif frame_index == 1:
                    frame_index = 3
                else:
                    frame_index = 2
            elif event.key == pygame.K_DOWN:
                to_y += player_speed
                if frame_index == 0:
                    frame_index = 4
                elif frame_index == 2:
                    frame_index = 4
                else:
                    frame_index = 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    player.x += to_x * dt
    player.y += to_y * dt

    # 가로 경계값 처리
    if player.x < -20:
        player.x = -20
    elif player.x > width - player.width + 20:
        player.x = width - player.width + 20

    # 세로 경계값 처리
    if player.y < -20:
        player.y = -20
    elif player.y > height - player.height:
        player.y = height - player.height

    horizontal = abs(spear.x - player.x)
    vertical = abs(spear.y - player.y)
    if horizontal == 0:
        horizontal = 1
    if vertical == 0:
        vertical = 1
    angle = math.degrees(math.atan((horizontal / vertical)))

    spear.x +=divide_x
    spear.y +=divide_y

    if abs(spear.x - player.x) < 10:
        if abs(spear.y - player.y) < 10:
            print("충돌")
            gameOver += 1
            if gameOver > 15:
                running = False
           
    if spear.y > random.randint(600, 800):
        spear.y = -64
        spear.x = -64
        angle = math.degrees(math.atan((abs(spear.x - player.x) / abs(spear.y - player.y))))
        rotatespear = pygame.transform.rotate(spear.img, angle)

        temp = math.gcd(int(abs(spear.x - player.x)), int(abs(spear.y - player.y)))
        s_speed_x = abs(spear.x - player.x) / temp
        s_speed_y = abs(spear.y - player.y) / temp

        divide_x = s_speed_x / math.gcd(int(s_speed_x), int(s_speed_y))
        divide_y = s_speed_y / math.gcd(int(s_speed_x), int(s_speed_y))
        if divide_x > 10:
            i=0
            while True:
                i+=1
                divide_x = divide_x / 10
                if divide_x <= 10:
                    break
            divide_y = (divide_y / 10**i)
            divide_x = divide_x

        if divide_x < 5:
            divide_x = divide_x * 2
            divide_y = divide_y * 2

        #print(divide_x)
        #print(divide_y)

    screen.fill((0, 0, 0))
    screen.blit(player.img, (player.x, player.y), (dx * frame_index, 0, dx, dy))
    screen.blit(rotatespear, (spear.x, spear.y))
    pygame.display.update()

pygame.quit()