import pygame
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Lumen")

clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

##############################오브젝트 클래스##############################
class IMG:
  def __init__(self, img, x, y):
    self.img = pygame.image.load(f"C:/Users/woota/OneDrive/바탕 화면/Pygame/Lumen/images/{img}.png")
    self.size = self.img.get_rect().size
    self.width = self.size[0]
    self.height = self.size[1]
    self.x = x
    self.y = y
##########################################################################

background = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Lumen/images/background.png")

player = IMG('PlayerSheet(6)', 590, 310)
player.width = player.size[0] / 24
player.height = player.size[1] / 4
player.x = (screen_width / 2) - (player.width / 2)
player.y = (screen_height / 2) - (player.height / 2)
player_speed = 0.6
to_x = 0
to_y = 0
dx, dy = 96, 96
ph = 0
ld = 0

light = IMG('LightSheet', 570, 330)
light.x = (screen_width / 2) - (light.width / 2)
light.y = (screen_height / 2) - (light.height / 2)

shadow = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Lumen/images/shadow.png")
shadow = pygame.transform.scale(shadow, (2560, 1440)) 
shadow_size = shadow.get_rect().size
shadow_width = shadow_size[0]
shadow_height = shadow_size[1]
shadow_x = (screen_width / 2) - (shadow_width / 2)
shadow_y = (screen_height / 2) - (shadow_height / 2)

enemy = IMG('enemy', -640, -360)
enemy.x = (screen_width / 2) - (enemy.width / 2)
enemy.y = (screen_height / 2) - (enemy.height / 2)

text = game_font.render("Yellow Square", True, (0, 0, 0))
text_x_pos = -630
text_y_pos = -150

running = True
while running:
    dt = clock.tick(60) # FPS 설정
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌려있는지 확인 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= player_speed
                ph = 0
                ld = 0

            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += player_speed
                ph = 1
                ld = 1
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= player_speed
                if ph ==0:
                    ph = 2
                elif ph == 5:
                    ph = 3
                elif ph == 1:
                    ph = 3
                else:
                    ph = 2
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로 
                to_y += player_speed
                if ph == 0:
                    ph = 4
                elif ph == 2:
                    ph = 4
                else:
                    ph = 5
            elif event.key == pygame.K_SPACE:
                if player_rect.colliderect(enemy_rect):
                    text_x_pos = player.x - 50
                    text_y_pos = player.y + 120

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_SPACE:
                text_x_pos = -630
                text_y_pos = -150

        if event.type == pygame.MOUSEBUTTONDOWN:
            pd = 4

    player.x += to_x * dt
    player.y += to_y * dt

    shadow_x = player.x - (shadow_width / 2) + (player.width / 2) + 20
    shadow_y = player.y - (shadow_height / 2) + (player.height / 2) + 20
    
    light.x = player.x - 20
    light.y = player.y + 20
    if ld == 1:
        light.x = player.x + 20


    # 가로 경계값 처리
    if player.x < 0:
        player.x = 0
    elif player.x > screen_width - player.width - 70:
        player.x = screen_width - player.width - 70

    # 세로 경계값 처리
    if player.y < 0:
        player.y = 0
    elif player.y > screen_height - player.height - 70:
        player.y = screen_height - player.height - 70

    # 충돌 처리를 위한 rect 정보 업데이트 
    player_rect = player.img.get_rect() 
    player_rect.left = player.x
    player_rect.top = player.y

    enemy_rect = enemy.img.get_rect() 
    enemy_rect.left = enemy.x
    enemy_rect.top = enemy.y

    screen.blit(background, (0, 0))
    screen.blit(enemy.img, (enemy.x, enemy.y))
    screen.blit(player.img, (player.x, player.y), (dx * ph, 0, dx, dy))
    screen.blit(light.img, (light.x, light.y), (dx * ld, 0, dx, dy))
    screen.blit(shadow, (shadow_x, shadow_y))
    screen.blit(text, (text_x_pos, text_y_pos))

    pygame.display.update()

pygame.time.delay(500)

# pygame quit
pygame.quit()