import pygame
from random import randint
from random import choice as rnd

touch_mode = False
scale = (600/720)

fps = 60
size = {"pipe" : [int(73*scale), int(450*scale)],            
    "bird" : [int(48*scale), int(34*scale)],
    "window" : [int(405*scale), int(720*scale)],
    "num" : [int(34*scale), int(51*scale)],
    "start" : [int(259*scale), int(375*scale)],
    "gameover" : [int(270*scale), int(59*scale)],
    "base" : [int(473*scale), int(158*scale)]}

load_cmd = " = pygame.image.load(file)"
resize_cmd = " = pygame.transform.smoothscale(eval(var), size[category])"
_fps = fps

category = "num"
for i in range(10):
    file = str(i) + ".png"
    var = category + "_" + str(i)
    exec(var + load_cmd)
    exec(var + resize_cmd)

category = "bird"
for color in ["blue", "red", "yellow"]:
    for state in ["down", "mid", "up"]:
        file = color + "-" + state + ".png"
        var = "bird_" + color + "_" + state
        exec(var + load_cmd)
        exec(var + resize_cmd)

bg1 = pygame.image.load("day.png")
bg2 = pygame.image.load("night.png")
pipe_green_btm = pygame.image.load("pipe-green.png")
pipe_red_btm = pygame.image.load("pipe-red.png")
start = pygame.image.load("start.png")
gameover = pygame.image.load("gameover.png")
base = pygame.image.load("base.png")
bg1 = pygame.transform.smoothscale(bg1, size["window"])
bg2 = pygame.transform.smoothscale(bg2, size["window"])
start = pygame.transform.smoothscale(start, size["start"])
gameover = pygame.transform.smoothscale(gameover, size["gameover"])
base = pygame.transform.smoothscale(base, size["base"])
pipe_green_btm = pygame.transform.smoothscale(pipe_green_btm, size["pipe"])
pipe_red_btm = pygame.transform.smoothscale(pipe_red_btm, size["pipe"])
pipe_green_top = pygame.transform.flip(pipe_green_btm, False, True)
pipe_red_top = pygame.transform.flip(pipe_red_btm, False, True)

initial = True
running = False
start_crd = ((size["window"][0]-size["start"][0])//2, (size["window"][1]-size["start"][1])//2)
gameover_crd = ((size["window"][0]-size["gameover"][0])//2, (size["window"][1]-size["gameover"][1])//2)
score_crd = (size["window"][0]-size["num"][0]-(10*scale), 10*scale)
pipe_height = size["pipe"][1]
pipe_gap_x = 4*size["pipe"][0]
pipe_gap_y = 3*size["bird"][1]
end = False
games_played = 0
pygame.draw.rect(screen, (0,0,0), (size["window"][0], 0, 800-size["window"][0], 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if not(touch_mode) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = True
                initial = True
        if touch_mode and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                running = True
                initial = True
    
    if initial:
        initial = False
        bg = eval("bg" + rnd(["1", "2"]))
        bird_color = rnd(["blue", "red", "yellow"])
        bird_up = eval("bird_" + bird_color + "_" + "up")
        bird_mid = eval("bird_" + bird_color + "_" + "mid")
        bird_down = eval("bird_" + bird_color + "_" + "down")
        pipe_color = rnd(["green", "red"])
        pipe_btm = eval("pipe_" + pipe_color + "_btm")
        pipe_top = eval("pipe_" + pipe_color + "_top")
        screen.blit(bg, (0, 0))
        screen.blit(start, start_crd)
        pygame.display.flip()
        pipe_x = size["window"][0]
        pipes = []
        for x in range(size["window"][0]//pipe_gap_x + 1):
            pipe_y = randint(0, size["window"][1]-size["base"][1]-pipe_gap_y)
            crd = [pipe_x, pipe_y]
            pipes.append(crd)
            pipe_x += pipe_gap_x
            
        base_crd = [0, size["window"][1]-size["base"][1]]
        bird_crd = [(size["window"][0])//5, (size["window"][1]-size["base"][1]-size["bird"][1])//2]
        cycle = 0
        score = 0
        lost = False
        pygame.draw.rect(screen, (0,0,0), (size["window"][0], 0, 800-size["window"][0], 600))
        
    while running:
        screen.blit(bg, (0, 0))
        pressed = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                pygame.quit()
            if not(touch_mode) and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pressed = True
            if touch_mode and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True
        if end:
            break

        if cycle == 2:
            cycle = 0
            for i in range(len(pipes)):
                pipes[i][0] -= 1

        if pipes[-1][0] <= size["window"][0]:
            pipe_x = pipes[-1][0]+pipe_gap_x
            pipe_y = randint(0, size["window"][1]-size["base"][1]-pipe_gap_y)
            crd = [pipe_x, pipe_y]
            pipes.append(crd)

        if pipes[0][0] <= -size["pipe"][0]:
            del pipes[0]

        for crd in pipes:
            if bird_crd[0] < crd[0] + size["pipe"][0] + 2:
                value = crd[1]
                break

        if pressed:
            bird = bird_up
            bird_crd[1] -= size["bird"][1]
        else:
            bird = bird_down
            bird_crd[1] += 1.4

        for crd in pipes:
            screen.blit(pipe_btm, (crd[0], crd[1]-(2*pipe_height)))
            screen.blit(pipe_top, (crd[0], crd[1]-pipe_height))
            screen.blit(pipe_btm, (crd[0], crd[1]+pipe_gap_y))
            screen.blit(pipe_top, (crd[0], crd[1]+pipe_gap_y+pipe_height))

        scr = list(str(score))[::-1]
        for i in range(len(scr)):
            img = eval("num_" + scr[i])
            crd = (int(score_crd[0] - i*(size["num"][0]+(10*scale))), score_crd[1])
            screen.blit(img, crd)

        if bird_crd[1] <= 0:
            bird_crd[1] = 0 
                        
        screen.blit(bird, bird_crd)
        screen.blit(base, base_crd)
        pygame.draw.rect(screen, (0,0,0), (size["window"][0], 0, 800-size["window"][0], 600))
        pygame.display.flip()
        clock.tick(_fps)
        cycle += 1
        _fps = fps + 3*(score//5)
        base_crd[0] -= 1
        if base_crd[0] + size["base"][0] == size["window"][0]:
            base_crd[0] = 0

        if bird_crd[1]+size["bird"][1] >= size["window"][1]-size["base"][1]:
            pygame.time.delay(1000)
            lost = True
            running = False
            games_played += 1
            break

        for crd in pipes:
            if crd[0] <= bird_crd[0] + size["bird"][0] and crd[0] + size["pipe"][0] > bird_crd[0]:
                if bird_crd[1] <= crd[1] or bird_crd[1] + size["bird"][1] >= crd[1]+pipe_gap_y+1:
                    pygame.time.delay(1000)
                    lost = True
                    running = False
                    break

            elif crd[0] + size["pipe"][0] == bird_crd[0] and cycle//2 == 0:
                score += 1
                
    if end:
        break

    if lost:
        screen.blit(gameover, gameover_crd)
        pygame.display.flip()

    if games_played >=3:
        break
