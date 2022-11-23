import pygame, random, os, sys
from pygame.locals import *


pygame.init()
def run_main():
    import MainGitHub

volume = 1
size = (900, 506)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Run to live')

font = pygame.font.SysFont('Constantia', 30)
fonte_principal = pygame.font.SysFont("LITHOGRAPH", 100)

folder = "imagens"

cenarios = ("cenario1.jpg", "cenario2.png", "cenario3.jpg")
cenario_random = random.randint(0, len(cenarios) - 1)
cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

preto = [0, 0, 0]

texto_principal = fonte_principal.render(("Run To Live"), True, preto)
screen.blit(texto_principal, [255, 125])

# define cor
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (169,169,169)

# define variavel global 
clicked = False
counter = 0

musica = {}
musica["despause"] = pygame.mixer.music.load('Sons/Lines of Code.mp3')
pygame.mixer.music.play(-1)

som = {}
som["despause"] = pygame.mixer.Sound('Sons/swoosh.wav')

class menu():
    # cores para botão e texto
    button_col = (white)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # obter a posição do mouse
        pos = pygame.mouse.get_pos()

        #criar um objeto pygame Rect para o botão
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # clicar botao
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # contorno do botão
        pygame.draw.line(screen, grey, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, grey, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # adicionar texto ao botão
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

def como_jogar():
    import sys, pygame, os, random

    pygame.init()

    size = (900, 506)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Run To Live")

    folder = "imagens"

    cenarios = ("cenario1.jpg", "cenario2.png", "cenario3.jpg")
    cenario_random = random.randint(0, len(cenarios) - 1)
    cenario = pygame.image.load(os.path.join(folder, cenarios[cenario_random]))

    branco = [0, 0, 0]

    fonte_texto = pygame.font.SysFont("LITHOGRAPH", 30)
    titulo = pygame.font.SysFont("LITHOGRAPH", 50)

    msg_titulo = titulo.render(("Como jogar:"), True, branco)
    texto = fonte_texto.render(("Utilizando as setas do teclado para controlar seu personagem, guie ele"), True, branco)
    texto2 = fonte_texto.render(("para capturar as comidas saudáveis e sobreviver o maximo de tempo que conseguir."), True, branco)

    msg_dificuldade1 = fonte_texto.render(("A dificuldade irá aumentar a cada 15 segundos."), True, branco)

    while True:

        screen.blit(cenario, (0, 0))

        if jogar.draw_button():
            run_main()
            pygame.display.update()
        if voltar.draw_button():
            menu(240, 240, 'Jogar')
            menu(470, 240, 'Instruções')
            menu(470, 240, 'Voltar')
            menu(240, 340, 'Tirar som')
            menu(470, 340, 'Colocar som')
            pygame.display.update()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x > 190 and x < 270) and (y > 380 and y < 500):
                    if (volume == 1):
                        som["despause"].play()
                    menu()


        screen.blit(msg_titulo, [3, 3])
        screen.blit(texto, [3, 70])
        screen.blit(texto2, [3, 90])
        screen.blit(msg_dificuldade1, [3, 130])

        pygame.display.flip()

jogar = menu(240, 240, 'Jogar')
instrucao = menu(470, 240, 'Instruções')
voltar = menu(470, 240, 'Voltar')
tirar_som = menu(240, 340, 'Tirar som')
colocar_som = menu(470, 340, 'Colocar som')

while True:

    screen.blit(cenario, (0, 0))
    screen.blit(texto_principal, [255, 125])

    if jogar.draw_button():
        run_main()
    if instrucao.draw_button():
        como_jogar()
    if tirar_som.draw_button():
        if(volume == 1):
            pygame.mixer.music.pause()
    if colocar_som.draw_button():
        pygame.mixer.music.unpause()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
