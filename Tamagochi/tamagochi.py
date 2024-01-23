import pygame
import random

pygame.init()
pygame.display.set_caption("Tamagochi project")
win = pygame.display.set_mode((500, 500))
hunger = pygame.image.load("Hunger.png")
hunger1 = pygame.image.load("Hunger.png")
bg = pygame.image.load("background.png")
deathscreen = pygame.image.load("deathscreen.png")
player = pygame.image.load("player.png"), pygame.image.load("player2.png")
hunger = pygame.transform.scale(hunger, (50, 50))
hunger1 = pygame.transform.scale(hunger1, (50, 50))
walkcount = 0
bgx = 0
charx = 200


def bars():
    # health bars
    pygame.draw.rect(win, (255, 0, 0), (20, 100, 10, 100))
    pygame.draw.rect(win, (0, 255, 0), (20, healthbargreeny, 10, hpminus))


def drawbigguy():
    global walkcount
    global scorex
    win.blit(bg, (bgx, 0))
    # drawing tamogachi
    if walkcount + 1 >= 12:
        walkcount = 0
    win.blit(player[walkcount // 6], (charx, 100))
    walkcount += 1
    scorex = 300
    text = font.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (scorex, 10))


class hungery(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawfood(self):
        hungery1.x = random.randint(1, 450)
        hungery1.y = random.randint(300, 450)

    def addhealth(self):
        global healthbargreeny
        global hpminus
        global score
        if healthbargreeny > 100:
            healthbargreeny -= 10
            score += 1
        if hpminus < 100:
            hpminus += 10


def restart():
    global bgx
    global charx
    global healthbargreeny
    global hpminus
    global score
    bgx = 0
    charx = 200
    healthbargreeny = 100
    hpminus = 100
    hungery1.x = random.randint(1, 450)
    hungery1.y = random.randint(300, 450)
    score = 0


healthbargreeny = 100
hpminus = 100
time = 5
score = 0
timehungery = 0
font = pygame.font.SysFont("comicsans", 30, True)
hungery1 = hungery(random.randint(1, 450), random.randint(300, 450))
hungery2 = hungery(5, 200)
fast = 5
timer = False
run = True

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if healthbargreeny <= 150:
                    if hungery1.x < pos[0] < hungery1.x + 50:
                        if hungery1.y < pos[1] < hungery1.y + 50:
                            hungery1.x = 700
                            timer = True
                            hungery.addhealth(win)
                if healthbargreeny > 150:
                    if hungery1.x < pos[0] < hungery1.x + 50:
                        if hungery1.y < pos[1] < hungery1.y + 50:
                            hungery.drawfood(win)
                            hungery.addhealth(win)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        restart()
    if score == 5:
        fast = 10
    if score < 10:
        if time == random.randint(0, 20):
            if healthbargreeny < 200:
                healthbargreeny += fast
            if hpminus > 0:
                hpminus -= fast
    if score > 10:
        if time == random.randint(0, 13):
            if healthbargreeny < 200:
                healthbargreeny += fast
            if hpminus > 0:
                hpminus -= fast
    if healthbargreeny == 200:
        bgx = 1000
        charx = 1000
        hungery1.x = 1000
        win.blit(bg, (0, 0))
        win.blit(deathscreen, (0, 0))
    if timer is True:
        if timehungery != 50:
            timehungery += 1
        if timehungery == 50:
            hungery.drawfood(win)
            timehungery = 0

    drawbigguy()
    bars()
    win.blit(hunger, (hungery2.x, hungery2.y))
    win.blit(hunger1, (hungery1.x, hungery1.y))
    pygame.display.update()

pygame.quit()