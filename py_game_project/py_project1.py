import pygame
import os
###################################################################################
#기본 초기화


pygame.init() ## 초기화

# 화면 크기 설정
screen_width = 480 #가로크기
screen_high = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_high))

# 화면 타이틀 설정

pygame.display.set_caption("jimin_game") # 게임 이름

background =pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/background.png")  #이미지 로드

# FPS

clock = pygame.time.Clock() ## 게임프레임

################################################################################################################################
# 1. 사용자 게임 초기화 (배경 화면 ,게임 이미지 , 좌표)






#캐릭터 불러오기

character = pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_high = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_high - character_high

# 적
enemy = pygame.image.load("C:/Users/정지민/Desktop/python_project/python_project/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_high = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = (screen_high/2) - enemy_high


# 폰트 정의

game_font = pygame.font.Font(None,40)

# 총 시간

total_time = 100
# 시간 계산

start_ticks = pygame.time.get_ticks()  ## 시작을 받아오는 변수

#  이벤트 루프
running =True  ## 게임진행 변수
### 케릭터 변수
to_x = 0  ## 케릭터 위치 변수
to_y = 0
character_speed = 10 # 캐릭터 속도  ex) character_speed * frame(clock)
while running :
    dt = clock.tick(100) #### 게임에 프레임 넣기


    print("fps:"+str(clock.get_fps()))
    # 2. 이벤트 처리 (키보드 ,마우스 등)
    for event in pygame.event.get():    ## 이벤트 발생
        
        if event.type == pygame.QUIT:
            running=False 

        
        
    #3. 게임  캐릭터 위치 정의


    #4. 충돌 처리



    #5. 화면에 그리기
    screen.blit(background,(0,0))    ## 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 케릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))



    character_x_pos  += to_x
    character_y_pos  += to_y
     

    # 가로 경계 
    if character_x_pos <= 0 :
        character_x_pos =0 
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width -character_width
    #가로 경계
    if character_y_pos <= 0 :
        character_y_pos =0
    elif character_y_pos > screen_high -character_high :
        character_y_pos = screen_high -character_high
    

    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    #충돌 체크

    if character_rect.colliderect(enemy_rect) :
        print("오류가 났어요")

        running ==False


    




    #screen.fill((0,0,255))  rgb 값으로 배경 넣기

   

    # 경과 시간 넣기  반드 스크린 뒤에 넣어야한다

    elapsed_time =(pygame.time.get_ticks()-start_ticks) /1000

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    #  render(시간 , True , 글자 색상 순서 로)

    if total_time - elapsed_time <=0 :
        running =False
          
    screen.blit(timer,(10,10))
    pygame.display.update() # 게임화면 다시그리기 계속 호출 되어야 하는거


pygame.quit()