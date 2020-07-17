import random
import pygame

font = pygame.font.SysFont("comicsansms",40)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
fps = 300
tp = pygame.image.load("tp.jpg")
paddles = [[5,275],[785,275]]
paddle_drn = [0,0]
taps = [0,0]
score = [0,0]
colors = [(255,0,0),(0,0,255)]
ball_crd = [400,350]
ball_drn = [1,0]
runs = 0
c_run = random.randint(125,200)
running = True

while running:
    prev_taps = tuple(taps)
    act_score = tuple(score)
    screen.fill((0,0,0))
    screen.blit(tp,(0,0))
    pygame.draw.rect(screen, (0,0,0,0),(0,100,800,500))
    pygame.draw.rect(screen, (255,255,255),(0,100,800,5))
    pygame.draw.rect(screen, (255,255,255),(0,595,800,5))
    for i in range(106,610,25):
        pygame.draw.rect(screen, (255,255,255), (398,i,4,12))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle_drn[1] = -1
            if event.key == pygame.K_DOWN:
                paddle_drn[1] = 1
            if two_player:
                if event.key == pygame.K_w:
                    paddle_drn[0] = -1
                if event.key == pygame.K_s:
                    paddle_drn[0] = +1
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] in range(740,790) and pos[1] in range(10,60):
                        running = False

    if not(two_player):               
        if runs%c_run == 0 and paddles[0][0] <= 400:
            c_run = random.randint(125,200)
            if ball_crd[1] <= paddles[0][1] + 75:
                paddle_drn[0] = -1
            else:
                paddle_drn[0] = +1
        
    for i in range(2):
        ball_crd[i] += ball_drn[i]
        paddles[i][1] += paddle_drn[i]
        if paddles[i][1] >= 445:
            paddles[i][1] = 445
            paddle_drn[i] = 0
        if paddles[i][1] <= 105:
            paddles[i][1] = 105
            paddle_drn[i] = 0

    if ball_crd[0] == 24:
        taps[0] += 1
        dy = ball_crd[1] - paddles[0][1]
        if dy >= 0 and dy <= 55:
            ball_drn = [1,-1]
        elif dy > 55 and dy < 95:
            ball_drn[0] = 1
        elif dy >= 95 and dy <= 150:
            ball_drn = [1,1]
        else:
            score[1] += 1
            ball_crd = [400,350]
            ball_drn = [1,0]
            fps = 300
            taps = [0,0]

    if ball_crd[0] == 776:
        taps[1] += 1
        dy = ball_crd[1] - paddles[1][1]
        if dy >= 0 and dy <= 55:
            ball_drn = [-1,-1]
        elif dy > 55 and dy < 95:
            ball_drn[0] = -1
        elif dy >= 95 and dy <= 150:
            ball_drn = [-1,1]
        else:
            score[0] += 1
            ball_crd = [400,350]
            ball_drn = [-1,0]
            fps = 300
            taps = [0,0]

    if ball_crd[1] == 106:
        ball_drn[1] *= -1

    if ball_crd[1] == 594:
        ball_drn[1] *= -1

    if running == False:
        break

    for i in range(2):
        text = font.render(str(score[i]), False, (255,255,255))
        pygame.draw.rect(screen, colors[i], paddles[i] + [10,150])
        pygame.draw.rect(screen, colors[i], [310 + 100*i ,10 , 80, 80])
        screen.blit(text, [340 + 100*i ,20])
    pygame.draw.circle(screen, (255,255,255), ball_crd, 10)
    screen.blit(hm_img, (750,10))
    
    pygame.display.flip()
    clock.tick(fps)
    if 5 in score:
        running = False
    runs += 1
    if sum(taps) != sum(prev_taps):
        taps = [0,0]
        fps += 30
        if fps >= 600:
            fps -= 10
