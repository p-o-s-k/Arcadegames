import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,600))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Arcade")
clock = pygame.time.Clock()
pygame.time.delay(1000)
games = {"snake":"Snake.py",
         "flappybird":"FlappyBird.py",
         "pong":"Pong.py",
         "pacman":"Pacman.py"}
s_img = pygame.image.load("snake-img.png")
s_img = pygame.transform.smoothscale(s_img,(150,150))
fb_img = pygame.image.load("flappybird-img.png")
fb_img = pygame.transform.smoothscale(fb_img,(150,150))
pn_img = pygame.image.load("pong-img.png")
pn_img = pygame.transform.smoothscale(pn_img,(150,150))
pn1_img = pygame.image.load("pong1-img.png")
pn1_img = pygame.transform.smoothscale(pn1_img,(150,150))
pc_img = pygame.image.load("pacman-img.png")
pc_img = pygame.transform.smoothscale(pc_img, (120,120))
hm_img = pygame.image.load("home.png")
hm_img = pygame.transform.smoothscale(hm_img,(40,40))
bg_img = pygame.image.load("bg.png")
bg_img = pygame.transform.smoothscale(bg_img,(800,600))
side_img = pygame.image.load("sidepanel.jpg")
side_img = pygame.transform.flip(side_img,False,True)
chosen = False

while True:
    screen.blit(bg_img,(0,0))
    screen.blit(s_img,(50,50))
    screen.blit(fb_img,(320,50))
    screen.blit(pc_img,(645,70))
    screen.blit(pn_img, (180,400))
    screen.blit(pn1_img, (470,400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] in range(50,201):
                if pos[0] in range(50,201):
                    chosen = True
                    game = "snake"
                if pos[0] in range(320,471):
                    chosen = True
                    game = "flappybird"
                if pos[0] in range(630,781):
                    chosen = True
                    game = "pacman"
            elif pos[1] in range(400,551):
                if pos[0] in range(200,351):
                    chosen = True
                    two_player = False
                    game = "pong"
                if pos[0] in range(470,621):
                    chosen = True
                    two_player = True
                    game = "pong"
    
    if chosen:
        chosen = False
        f = open(games[game])
        exec(f.read())
        f.close()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Arcade")
    pygame.display.flip()
