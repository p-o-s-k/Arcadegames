from random import randint

pygame.display.set_caption("Snake")
font = pygame.font.SysFont("comicsansms",35)
drn = [0,0]
fps = 120
snake = [[[300,300],list(drn)]]
drn_switch = []
crd_switch = []
bit_crd = []
running = True
bit_update = True
update = False
lost = False
end = False
while running:
    if bit_update:
        bit_crd = [randint(15,585)-5,randint(15,585)-5]
        bit_update = False
    prev_drn = list(drn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            end = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                drn = [0,-1]
            if event.key == pygame.K_DOWN:
                drn = [0,1]
            if event.key == pygame.K_LEFT:
                drn = [-1,0]
            if event.key == pygame.K_RIGHT:
                drn = [1,0]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(740,790) and pos[1] in range(10,60):
                    running = False
                    end = True

    if end:
        break

    if update:
        crd = [snake[-1][0][0]-(snake[-1][1][0]*18),snake[-1][0][1]-(snake[-1][1][1]*18)]
        snake.append([crd,snake[-1][1]])
        update = False

    if drn != prev_drn:
        snake[0][1] = list(drn)
        drn_switch.append(list(drn))
        crd_switch.append(list(snake[0][0]))

    for i in range(len(snake)):                  
        for j in range(2):
            snake[i][0][j] += snake[i][1][j]
        if snake[i][0] in crd_switch:
            ind = crd_switch.index(snake[i][0])
            snake[i][1] = list(drn_switch[ind])
            if i == len(snake)-1:
                del crd_switch[ind]
                del drn_switch[ind]
        if i == 0:
            if snake[i][0][0] <= 10 or snake [i][0][0] >= 590 or snake[i][0][1] <= 10 or snake [i][0][1] >= 590:
                lost = True
        else:
            ref_val = snake[0][0]
            test_val = snake[i][0]
            dstnce = ((ref_val[0]-test_val[0])**2 + (ref_val[1]-test_val[1])**2)**0.5
            if dstnce < 10:
                lost = True
                
    score = len(snake)-1
    fps = 120 + (score)*3

    pygame.draw.rect(screen,(0,0,0),(0,0,600,600))
    screen.blit(side_img, (600,0))
    if lost:
        t_loss = font.render(" You Lose!",False,(255,30,30))
        screen.blit(t_loss, (602,400))
        running = False
    pygame.draw.rect(screen,(100,200,255),bit_crd + [10,10])
    for crd in snake:
        pygame.draw.circle(screen,(255,255,0),crd[0],10)
        score_text = " Score: " + str(score)
    t_score = font.render(score_text,False,(255,255,255))
    screen.blit(t_score, (602,100))
    screen.blit(hm_img, (750,10))
    pygame.display.flip()
    clock.tick(fps)
    for i in range(10):
        for j in range(10):
            clr = screen.get_at((bit_crd[0] + i,bit_crd[1] + j))
            if clr == (255,255,0,255):
                bit_update = True
                update = True

if not(end):
    pygame.time.delay(3000)
                
