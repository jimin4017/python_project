import pygame

pygame.init() ## 초기화

screen_width = 480 #가로크기
screen_high = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_high))

# 화면 타이틀 설정

pygame.display.set_caption("jimin_game") # 게임 이름

background =pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/background.png")  #이미지 로드

#캐릭터 불러오기

character = pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_high = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_high - character_high

#  이벤트 루프
running =True  ## 게임진행 변수
### 케릭터 변수
to_x = 0  ## 케릭터 위치 변수
to_y = 0
while running :
    for event in pygame.event.get():    ## 이벤트 발생
        if event.type == pygame.QUIT:
            running=False 
        if event.type == pygame.KEYDOWN : # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT :
                to_x -= 2
            elif event.key == pygame.K_RIGHT :
                to_x += 2
            elif event.key == pygame.K_UP :
                to_y -= 1
            elif event.key == pygame.K_DOWN :
                to_y += 1
        if event.type == pygame.KEYUP  : # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_pos  += to_x
    character_y_pos  += to_y
     

    # 가로 경계 
    if character_x_pos <= 0 :
        character_x_pos =0 
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width -character_width

    if character_y_pos <= 0 :
        character_y_pos =0
    elif character_y_pos > screen_high -character_high :
        character_y_pos = screen_high -character_high

    
          
    




    #screen.fill((0,0,255))  rgb 값으로 배경 넣기

    screen.blit(background,(0,0))    ## 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 케릭터 그리기
    pygame.display.update() # 게임화면 다시그리기 계속 호출 되어야 하는거


pygame.quit()