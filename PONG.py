import pygame
import sys
from pygame.locals import *

player1 = raw_input("Player on the left please enter your name : ")
player2 = raw_input("Player on the right please enter your name : ")
print
print player1, "use W for UP and S for DOWN"
print player2, "use P for UP and L for DOWN"
print
print "The player who gets a SCORE of 5 first wins"
print
print "ALL THE BEST!!"

FPS = 250

LineThickness = 10
size = 100

Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
Orange = (255, 165, 0)
White = (255, 255, 255)

score1 = 0
score2 = 0
pygame.time.wait(3000)


def Game(score1, score2):
    pygame.init()
    global DISPLAYSURF
    global nfont, fontsize
    fontsize = 20
    nfont = pygame.font.Font('freesansbold.ttf', fontsize)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('PONG')
    ballX = 600 - (LineThickness / 2)
    ballY = 300 - (LineThickness / 2)
    p1 = (600 - size) / 2
    p2 = (600 - size) / 2
    ballxdir = -1
    ballydir = -1
    paddle1 = pygame.Rect(30, p1, 15, size)
    paddle2 = pygame.Rect(1160, p2, 15, size)
    ball = pygame.Rect(ballX, ballY, 12, 12)
    Arena()
    Paddle_Draw(paddle1)
    Paddle_Draw(paddle2)
    Ball_Draw(ball)
    pygame.time.wait(1000)

    while True:
        pressing = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pressing[pygame.K_p]:
            paddle2.move_ip(0, -1)
        elif pressing[pygame.K_l]:
            paddle2.move_ip(0, 1)
        elif pressing[pygame.K_w]:
            paddle1.move_ip(0, -1)
        elif pressing[pygame.K_s]:
            paddle1.move_ip(0, 1)

        Arena()
        Paddle_Draw(paddle1)
        Paddle_Draw(paddle2)
        Ball_Draw(ball)
        scoredisplay(score1, score2)
        ball = Moveball(ball, ballxdir, ballydir)
        ballxdir, ballydir = Edgecollision(ball, ballxdir, ballydir)
        ballxdir = paddlecollision(ball, ballxdir, paddle1, paddle2)
        calscore(ball, score1, score2, player1, player2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def Moveball(ball, ballx, bally):
    ball.x += ballx
    ball.y += bally
    return ball


def Edgecollision(ball, ballxdir, ballydir):
    if ball.top == 10 or ball.bottom == 590:
        ballydir = ballydir * (-1)
    return ballxdir, ballydir


def paddlecollision(ball, ballxdir, paddle1, paddle2):
    if ballxdir == -1 and ball.left == paddle1.right and ball.bottom > paddle1.top and ball.top < paddle1.bottom:
        ballxdir *= -1
    elif ballxdir == 1 and ball.right == paddle2.left and ball.bottom > paddle2.top and ball.top < paddle2.bottom:
        ballxdir *= -1
    return ballxdir


def scoredisplay(score1, score2):
    score1disp = nfont.render('Score = %s' % (score1), True, White)
    score1rect = score1disp.get_rect()
    score1rect.topleft = (100, 25)
    DISPLAYSURF.blit(score1disp, score1rect)

    score2disp = nfont.render('Score = %s' % (score2), True, White)
    score2rect = score1disp.get_rect()
    score2rect.topleft = (700, 25)
    DISPLAYSURF.blit(score2disp, score2rect)


def calscore(ball, score1, score2, player1, player2):
    if ball.left == 10:
        score2 += 1
        if score2 == 5:
            print player2, "WINS"
            print player1, "LOSES"
            print
            print "GAME OVER"
            scoredisplay(score1, score2)
            pygame.quit()
            sys.exit()
        else:
            Game(score1, score2)
    elif ball.right == 1190:
        score1 += 1
        if score1 == 5:
            print player1, "WINS"
            print player2, "LOSES"
            print
            print "GAME OVER"
            scoredisplay(score1, score2)
            pygame.quit()
            sys.exit()
        else:
            Game(score1, score2)


def Arena():
    DISPLAYSURF.fill((0, 0, 0))
    pygame.draw.rect(DISPLAYSURF, Orange,
                     ((0, 0), (600, 600)), LineThickness / 4)
    pygame.draw.rect(DISPLAYSURF, Orange, ((600, 0),
                                           (600, 600)), LineThickness / 4)
    pygame.draw.rect(DISPLAYSURF, Blue,
                     ((0, 0), (1200, 600)), LineThickness * 2)


def Ball_Draw(ball):
    pygame.draw.rect(DISPLAYSURF, Green, ball)


def Paddle_Draw(paddle):
    if paddle.bottom > 600 - LineThickness:
        paddle.bottom = 600 - LineThickness
    elif paddle.top < LineThickness:
        paddle.top = LineThickness
    pygame.draw.rect(DISPLAYSURF, Red, paddle)


Game(score1, score2)
