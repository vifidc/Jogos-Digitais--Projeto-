import turtle
import random
import time
import pygame
from pygame.locals import *

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('sons/Lines of Code.mp3')

audio_colisaoalimentosaudavel = pygame.mixer.Sound('sons/smw_coin.wav')
audio_colisaoalimentosnaosaudavel = pygame.mixer.Sound('sons/explosao.wav')

pygame.mixer.music.play(-1)

tela = turtle.Screen()
tela.title("Run to Live")
tela.bgcolor("black")
tela.bgpic("cenario.gif")
tela.setup(width=900, height=506)
tela.tracer(0)
tela.register_shape("personagem_left.gif")
tela.register_shape("personagem_right.gif")
tela.register_shape("Alimentos Naosaudavel/naosaudavel0.gif")
tela.register_shape("Alimentos Naosaudavel/naosaudavel1.gif")
tela.register_shape("Alimentos Naosaudavel/naosaudavel2.gif")
tela.register_shape("Alimentos Saudave/alimento0.gif")
tela.register_shape("Alimentos Saudave/alimento1.gif")
tela.register_shape("Alimentos Saudave/alimento2.gif")
tela.register_shape("Alimentos Saudave/alimento3.gif")

score = 0
lives = 3

player = turtle.Turtle()
player.speed(0)
player.shape("personagem_left.gif")
player.color("white")
player.penup()
player.goto(0, -140)
player.diection = "stop"

saudaveis = []
for x in range(1,4):
    saudavel = turtle.Turtle()
    saudavel.shape("Alimentos Saudave/alimento"+str(x)+".gif")
    saudavel.color("green")
    saudavel.penup()
    saudavel.goto(-100, 250)
    saudavel.speed =  1 #random.randint(1, 2) 
    saudaveis.append(saudavel)

nao_saudaveis = []
for y in range(1,2):
    naosaudavel = turtle.Turtle()
    naosaudavel.shape("Alimentos Naosaudavel/naosaudavel"+str(y)+".gif")
    naosaudavel.color("green")
    naosaudavel.penup()
    naosaudavel.goto(100, 250)
    naosaudavel.speed = 1 #random.randint(1, 2)
    nao_saudaveis.append(naosaudavel)

quadro = turtle.Turtle()
quadro.speed(0)
quadro.shape("square")
quadro.color("white")
quadro.penup()
quadro.hideturtle()
quadro.goto(0, 200)
quadro.write("Pontuação: 0  Vidas: 3", align="center", font=("Courier", 24, "normal"))

def go_left():
    x, y = player.position()
    player.goto(x=x-20, y=y)
    player.shape("personagem_right.gif")

def go_right():
    x, y = player.position()
    player.goto(x=x+20, y=y)
    player.shape("personagem_left.gif")

tela.listen()
tela.onkeypress(go_left, "Left")
tela.onkeypress(go_right, "Right")

# Loop do jogo (Main )
sair = True
while sair:
    tela.update()
    tela.listen()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                go_left()
            if event.key == pygame.K_RIGHT:
                go_right()

    for saudavel in saudaveis:
        # Movendo os alimentos saudável
        saudavel.sety(saudavel.ycor() - saudavel.speed)

        # Verificando se os alimentos não estão fora da tela
        if saudavel.ycor() < -300:
            saudavel.goto(random.randint(-300, 300), random.randint(400, 800))

        # Verificando se ha colisões
        if player.distance(saudavel) < 40:
            score += 10
            audio_colisaoalimentosaudavel.play()
            quadro.clear()
            quadro.write("Pontuação: {}  Vidas: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            # Movendo os alimentos saudável ao topo
            saudavel.goto(random.randint(-300, 300), random.randint(400, 800))

    for naosaudavel in nao_saudaveis:
        # Movendo alimentos não saudável
        naosaudavel.sety(naosaudavel.ycor() - naosaudavel.speed)

        if naosaudavel.ycor() < -300:
            naosaudavel.goto(random.randint(-300, 300), random.randint(400, 800))

        if player.distance(naosaudavel) < 40:
            # Pontuação aumenta
            score -= 10
            lives -= 1

            audio_colisaoalimentosnaosaudavel.play()

            # Mostrando a pontuação
            quadro.clear()
            quadro.write("Pontuação: {}  Vidas: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

            time.sleep(1)
            # Movendo os alimentos não saudável ao topo
            for naosaudavel in nao_saudaveis:
                naosaudavel.goto(random.randint(-300, 300), random.randint(400, 800))

    # Verificando se o jogo acabou
    if lives == 0:
        quadro.clear()
        quadro.write("Game Over! Pontuação: {}".format(score), align="center", font=("Courier", 35, "normal"))
        quadro.clear()
        time.sleep(5)
        quadro.write("\nAguarde uns instantes para jogar novamente ou feche o programa para sair! ".format(), align="center", font=("Courier", 15, "normal"))
        time.sleep(5)
        tela.update()
        score = 0
        lives = 3
        quadro.clear()
        quadro.write("Pontuação: {}  Vidas: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
