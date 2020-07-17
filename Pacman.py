import time, random
pygame.display.set_caption("Pacman")
font = pygame.font.SysFont("ComicSans",35)
win = font.render("  YOU WIN", False, (0, 200, 90))
loss = font.render("  YOU LOSE", False, (200, 10, 10))

def draw_mp():
    screen.fill((0,0,0,0))
    for icrd in points:
        pygame.draw.rect(screen, (255,100,100), icrd + (4,4))
    for icrd in pellets:
        pygame.draw.rect(screen, (255,180,180), icrd + (8,8))
    for icrd in mp:
        pygame.draw.rect(screen, (0,0,0,0), icrd)
        pygame.draw.rect(screen, (0, 51, 252, 255), icrd, 2)
    for x in (0,550):
        pygame.draw.rect(screen, (0,0,0,0), (x,271,20,39))
    pygame.draw.rect(screen, (255,20,20), (260,270,40,4))

def ghost_mv(g):
    global g_crd, g_drn, g_turn
    while True:
        g_turn[g] = random.choice([[0,1],[0,-1],[1,0],[-1,0]])
        if (g_turn[g][0] + g_drn[g][0] != 0)or (g_turn[g][1] + g_drn[g][1] != 0):
            break
    if g_drn[g] != g_turn[g]:
        g_test_crd = tuple([g_crd[g][0] + g_turn[g][0]*38, g_crd[g][1] + g_turn[g][1]*38])
        for blocks in mp:
            if (g_test_crd[0] + 38 >= blocks[0] and g_test_crd[0] <= blocks[0] + blocks[2]) and (g_test_crd[1] + 38 >= blocks[1] and g_test_crd[1] <= blocks[1] + blocks[3]):
                g_drn[g] = list(g_prev_drn[g])
                break
            else:
                g_drn[g] = list(g_turn[g])

    g_crd[g] = tuple([g_crd[g][0] + g_drn[g][0], g_crd[g][1] + g_drn[g][1]])

    for blocks in mp:
        if (g_crd[g][0] + 38 >= blocks[0] and g_crd[g][0] <= blocks[0] + blocks[2]) and (g_crd[g][1] + 38 >= blocks[1] and g_crd[g][1] <= blocks[1] + blocks[3]):
            if g_turn[g] == g_prev_drn[g]:
                g_crd[g] = list(g_prev[g])
                g_drn[g] = [0,0]
            else:
                g_crd[g] = list(g_prev[g])

    g_crd[g] = list(g_crd[g])

def test_crds(crds):
    status = True
    for i in range(active_ghosts):
        if (crds[0] in range(g_crd[i][0],g_crd[i][0]+37)) and (crds[1] in range(g_crd[i][1],g_crd[i][1]+37)):
            status = False
    if pellet and (crds[0] in range(crd[0],crd[0]+37)) and (crds[1] in range(crd[1],crd[1]+37)):
        status = True
    return status

mp = ((0,0,560,10),(0,590,560,10),(0,0,10,600),
      (550,0,10,600),(50,50,60,60),(150,50,80,60),
      (50,150,60,20),(150,150,20,120),(0,210,110,60),
      (150,210,80,20),(0,310,110,60),(150,310,20,60),
      (50,410,60,20),(150,410,80,20),(50,530,180,20),
      (90,410,20,80),(0,470,50,20),(150,470,20,80),
      (270,0,20,110),(330,50,80,60),(450,50,60,60),
      (210,150,140,20),(390,150,20,120),(450,150,60,20),
      (330,210,80,20),(450,210,110,60),(450,310,110,60),
      (390,310,20,60),(330,410,80,20),(450,410,60,20),
      (450,410,20,80),(330,530,180,20),(390,470,20,80),
      (510,470,50,20),(270,150,20,80),(270,470,20,80),
      (210,470,140,20),(270,350,20,80),(210,350,140,20),
      (210,270,140,40))

points = [(30,30),(50,30),(70,30),(90,30),(110,30),(130,30),(150,30),(170,30),
          (190,30),(210,30),(230,30),(250,30),(310,30),(330,30),(350,30),(370,30),
          (390,30),(410,30),(430,30),(450,30),(470,30),(490,30),(510,30),(530,30),
          (130,50),(250,50),(310,50),(430,50),(30,70),(130,70),
          (250,70),(310,70),(430,70),(530,70),(30,90),(130,90),(250,90),(310,90),
          (430,90),(530,90),(30,110),(130,110),(250,110),(310,110),(430,110),
          (530,110),(30,130),(50,130),(70,130),(90,130),(110,130),(130,130),(150,130),
          (170,130),(190,130),(210,130),(230,130),(250,130),(270,130),(290,130),
          (310,130),(330,130),(350,130),(370,130),(390,130),(410,130),(430,130),(450,130),
          (470,130),(490,130),(510,130),(530,130),(30,150),(130,150),(190,150),(370,150),
          (430,150),(530,150),(30,170),(130,170),(190,170),(370,170),(430,170),(530,170),
          (30,190),(50,190),(70,190),(90,190),(110,190),(130,190),(190,190),(210,190),
          (230,190),(250,190),(270,290),(290,290),(310,190),(330,190),(350,190),(370,190),
          (430,190),(450,190),(470,190),(490,190),(510,190),(530,190),(130,210),(430,210),
          (130,230),(430,230),(130,250),(430,250),(130,270),(430,270),(130,290),(430,290),
          (130,310),(430,310),(130,330),(430,330),(130,350),(430,350),(130,370),(430,370),
          (30,390),(50,390),(70,390),(90,390),(110,390),(130,390),(150,390),(170,390),
          (190,390),(210,390),(230,390),(250,390),(310,390),(330,390),(350,390),(370,390),
          (390,390),(410,390),(430,390),(450,390),(470,390),(490,390),(510,390),(530,390),
          (30,410),(130,410),(250,410),(310,410),(430,410),(530,410),(30,430),(130,430),
          (250,430),(310,430),(430,430),(530,430),(30,450),(50,450),(70,450),(130,450),
          (150,450),(170,450),(190,450),(210,450),(230,450),(250,450),(270,450),(290,450),
          (310,450),(330,450),(350,450),(370,450),(390,450),(410,450),(430,450),(490,450),
          (510,450),(530,450),(70,470),(130,470),(190,470),(370,470),(430,470),(490,470),
          (70,490),(130,490),(190,490),(370,490),(430,490),(490,490),(30,510),(50,510),
          (70,510),(90,510),(110,510),(130,510),(190,510),(210,510),(230,510),(250,510),
          (310,510),(330,510),(350,510),(370,510),(430,510),(450,510),(470,510),(490,510),
          (510,510),(530,510),(30,530),(250,530),(310,530),(530,530),(250,550),
          (310,550),(30,570),(50,570),(70,570),(90,570),(110,570),(130,570),
          (150,570),(170,570),(190,570),(210,570),(230,570),(250,570),(270,570),(290,570),
          (310,570),(330,570),(350,570),(370,570),(390,570),(410,570),(430,570),(450,570),
          (470,570),(490,570),(510,570),(530,570)]

pellets = [(28,48),(528,48),(28,548),(528,548)]

fps = 120

pc = pygame.image.load("Games\\sprites\\pc.png")
pc = pygame.transform.smoothscale(pc,(36,36))
pc1 = pygame.transform.flip(pc, True, False)
pc2 = pygame.transform.rotate(pc, 90)
pc3 = pc
pc4 = pygame.transform.flip(pc2, False, True)
g0 = pygame.image.load("Games\\sprites\\ghost0.jpg")
g0 = pygame.transform.smoothscale(g0,(36,36))
g1 = pygame.image.load("Games\\sprites\\ghost1.png")
g1 = pygame.transform.smoothscale(g1,(36,36))
g2 = pygame.image.load("Games\\sprites\\ghost2.png")
g2 = pygame.transform.smoothscale(g2,(36,36))
g3 = pygame.image.load("Games\\sprites\\ghost3.png")
g3 = pygame.transform.smoothscale(g3,(36,36))
g_crd = [[215,273],[265,273],[310,273]]
g_drn = [[1,0],[1,0],[1,0]]
g_turn = [[0,0],[0,0],[0,0]]
mx_ghosts = 3
ghost_states = [-1,-1,-1]
active_ghosts = 0
clr = (0, 51, 252, 255)
draw_mp()
crd = [11,11]
screen.blit(pc,crd)
pygame.display.flip()
running = True
drn = [0,0]
turn = [0,0]
pellet = False
wait = False
start = time.time()
rx = time.time() - 1000
check = True
while running:
    draw_mp()
    pygame.draw.rect(screen, (255,255,255), (561,0,239,600))
    screen.blit(side_img,(600,0))
    if check and int(time.time()-start)%5 == 0 and int(time.time()-start) != 0 and int(time.time()-rx) >= 5:
        active_ghosts += 1
        g_crd[active_ghosts-1][1] = 231
        ghost_states[active_ghosts-1] = 1
        rx = time.time()
        if active_ghosts == mx_ghosts:
            check = False

    g_prev = list(g_crd)
    g_prev_drn = list(g_drn)
    prev = list(crd)
    prev_drn = list(drn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                turn = [1,0]
            if event.key == pygame.K_LEFT:
                turn = [-1,0]
            if event.key == pygame.K_UP:
                turn = [0,-1]
            if event.key == pygame.K_DOWN:
                turn = [0,1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(740,790) and pos[1] in range(10,60):
                    running = False

    if drn != turn:
        test_crd = tuple([crd[0] + turn[0]*38, crd[1] + turn[1]*38])
        for blocks in mp:
            if (test_crd[0] + 38 >= blocks[0] and test_crd[0] <= blocks[0] + blocks[2]) and (test_crd[1] + 38 >= blocks[1] and test_crd[1] <= blocks[1] + blocks[3]):
                drn = list(prev_drn)
                break
            else:
                drn = list(turn)

    crd = tuple([crd[0] + drn[0], crd[1] + drn[1]])

    for blocks in mp:
        if (crd[0] + 38 >= blocks[0] and crd[0] <= blocks[0] + blocks[2]) and (crd[1] + 38 >= blocks[1] and crd[1] <= blocks[1] + blocks[3]):
            if turn == prev_drn:
                crd = list(prev)
                drn = [0,0]
            else:
                crd = list(prev)

    for g in range(active_ghosts):
        if ghost_states[g] == 1:   
            ghost_mv(g)
            if (crd[0] in range(g_crd[g][0],g_crd[g][0] + 40)) and (crd[1] in range(g_crd[g][1],g_crd[g][1] + 40)):
                if pellet:
                    ghost_states[g] = 0
                else:
                    screen.blit(loss,(610,400))
                    running = False
                    
    if len(points) == 0:
        screen.blit(win,(610,400))
        running = False

    if drn == [0,0] or drn == [1,0]:
        pac = pc1
    if drn == [0,1]:
        pac = pc2
    if drn == [-1,0]:
        pac = pc3
    if drn == [0,-1]:
        pac = pc4


    screen.blit(pac,crd)
    for i in range(3):
        if ghost_states[i] != 0:
            ghst = eval("g"+str(i+1))
            if pellet:
                ghst = g0
            screen.blit(ghst, g_crd[i])
    

    screen.blit(hm_img,(750,10))
    pygame.display.flip()
    clock.tick(fps)

    del_lst = []
    for i in points:
        clr = screen.get_at(i)
        if clr != (255,100,100,255) and test_crds(i):
            del_lst.append(i)

    for i in pellets:
        clr = screen.get_at(i)
        if clr != (255,180,180,255) and test_crds(i):
            del pellets[pellets.index(i)]
            pellet = True
            
    if pellet == True and wait == False:
        wait = True
        tm = time.time()

    if wait:
        if int(time.time()-tm) == 10:
            pellet = False
            wait = False
        
    while len(del_lst) > 0:
        del points[points.index(del_lst[0])]
        del del_lst[0]

pygame.time.delay(3000)


            
