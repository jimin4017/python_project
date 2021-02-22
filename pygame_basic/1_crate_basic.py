import pygame

pygame.init() ## 초기화

screen_width = 480 #가로크기
screen_heigh = 640 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_heigh))

# 화면 타이틀 설정

pygame.display.set_caption("jimin_game") # 게임 이름

background =pygame.image.load()



####


running =True  ## 게임진행 변수
while running :
    for event in pygame.event.get():    ## 이벤트 발생
        if event.type == pygame.QUIT:
            running=False 


pygame.quit()