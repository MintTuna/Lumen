import pygame
pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Lumen")

clock = pygame.time.Clock()

####################오브젝트####################

background = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/background.png")

character = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/player.png")
character_size = character.get_rect().size # 이미지 크기
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = (screen_height / 2) - (character_height / 2) #화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로) 연구소
character_speed = 0.6
to_x = 0
to_y = 0

light = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/light.png")
light_size = light.get_rect().size
light_width = light_size[0]
light_height = light_size[1]
light_x_pos = (screen_width / 2) - (light_width / 2)
light_y_pos = (screen_height / 2) - (light_height / 2)

shadow = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/shadow.png")
shadow = pygame.transform.scale(shadow, (2560, 1440)) 
shadow_size = shadow.get_rect().size
shadow_width = shadow_size[0]
shadow_height = shadow_size[1]
shadow_x_pos = (screen_width / 2) - (shadow_width / 2)
shadow_y_pos = (screen_height / 2) - (shadow_height / 2)

textbar = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/textbar.png")
textbar = pygame.transform.scale(textbar, (630, 150)) 
textbar_size = textbar.get_rect().size
textbar_width = textbar_size[0]
textbar_height = textbar_size[1]
textbar_x_pos = -630 # (screen_width / 2) - (textbar_width / 2)
textbar_y_pos = -150 # (screen_height / 2) - (textbar_height / 2)

enemy = pygame.image.load("C:/Users/woota/OneDrive/바탕 화면/Pygame/Light/images/enemy.png")
enemy_size = enemy.get_rect().size # get image size
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로) 연구소

game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

text = game_font.render("Yellow Square", True, (0, 0, 0))
text_x_pos = -630
text_y_pos = -150

# timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상

# Event loop
running = True
while running:
    dt = clock.tick(60) # FPS 설정
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌려있는지 확인 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로 
                to_y += character_speed
            elif event.key == pygame.K_SPACE:
                if character_rect.colliderect(enemy_rect):
                    textbar_x_pos = (screen_width / 2) - (textbar_width / 2)
                    textbar_y_pos = (screen_height / 2) - (textbar_height / 2) + 160
                    text_x_pos = (screen_width / 2) - (textbar_width / 2) + 50
                    text_y_pos = (screen_height / 2) - (textbar_height / 2) + 200

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_SPACE:
                textbar_x_pos = -630
                textbar_y_pos = -150
                text_x_pos = -630
                text_y_pos = -150

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    shadow_x_pos = character_x_pos - (shadow_width / 2) + (character_width / 2)
    shadow_y_pos = character_y_pos - (shadow_height / 2) + (character_height / 2)

    light_x_pos = character_x_pos - 20
    light_y_pos = character_y_pos + 20
    
    # 가로 경계값 처리
    if character_x_pos < -20:
        character_x_pos = -20
    elif character_x_pos > screen_width - character_width + 20:
        character_x_pos = screen_width - character_width + 20

    # 세로 경계값 처리
    if character_y_pos < -20:
        character_y_pos = -20
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    ###################충돌처리#####################

    # 충돌 처리를 위한 rect 정보 업데이트 
    character_rect = character.get_rect() 
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크 
    '''
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        touching = 1
    '''

    ###############################################
     
    screen.blit(background, (0, 0))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(light, (light_x_pos, light_y_pos))
    screen.blit(shadow, (shadow_x_pos, shadow_y_pos))
    screen.blit(textbar, (textbar_x_pos, textbar_y_pos))
    screen.blit(text, (text_x_pos, text_y_pos))
    print(textbar_x_pos)
    print(textbar_y_pos)

    # timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    # screen.blit(timer, (10, 10))

    pygame.display.update() # 게임 화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(500)

# pygame quit
pygame.quit()