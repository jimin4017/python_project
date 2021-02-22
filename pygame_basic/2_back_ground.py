import pygame

pygame.init() ## 초기화

screen_width = 480 #가로크기
screen_heigh = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_heigh))

# 화면 타이틀 설정

pygame.display.set_caption("jimin_game") # 게임 이름

background =pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/background.png")  #이미지 로드

#캐릭터 불러오기

character = pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height/2

#  이벤트 루프
running =True  ## 게임진행 변수
while running :
    for event in pygame.event.get():    ## 이벤트 발생
        if event.type == pygame.QUIT:
            running=False 
    #screen.fill((0,0,255))  rgb 값으로 배경 넣기

    screen.blit(background,(0,0))    ## 배경 그리기

    pygame.display.update() # 게임화면 다시그리기 계속 호출 되어야 하는거


pygame.quit()