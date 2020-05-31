import pygame
from random import randrange


def texto(msg, cor, tamanho, x, y):
    font = pygame.font.SysFont(None, tamanho)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, (x, y))


def cobra(Cobra_xy, cor):
    for xy in Cobra_xy:
        pygame.draw.rect(window, cor, (xy[0], xy[1], tam, tam))


def maca(pos_x, pos_y):
    pygame.draw.rect(window, red, (pos_x, pos_y, tam, tam))


def jogo():
    sair = True
    fim_de_jogo = False
    pos_x1 = randrange(0, (width - tam), 10)
    pos_y1 = randrange(0, (height - tam - placar), 10)
    pos_x2 = randrange(0, (width - tam), 10)
    pos_y2 = randrange(0, (height - tam - placar), 10)
    maca_x = randrange(0, (width - tam), 10)
    maca_y = randrange(0, (height - tam - placar), 10)
    velocidade_x = 0
    velocidade_y = 0
    velocidade_y2 = 0
    velocidade_x2 = 0
    relogio = pygame.time.Clock()
    Cobra_xy = []
    Cobra2_xy = []
    maximo = 1
    maximo2 = 1

    while sair:
        while fim_de_jogo:
            window.fill(white)
            texto('Fim de jogo', red, 50, 65, 30)
            texto(f'O jogador {ganhou} ganhou o jogo!', black, 30, 20, 80)
            pygame.draw.rect(window, black, (45, 120, 135, 27))
            texto('Continuar(c)', white, 30, 50, 125)
            pygame.draw.rect(window, black, (190, 120, 75, 27))
            texto('Sair(s)', white, 30, 195, 125)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fim_de_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fim_de_jogo = False
                        pos_x1 = randrange(0, (width - tam), 10)
                        pos_y1 = randrange(0, (height - tam - placar), 10)
                        pos_x2 = randrange(0, (width - tam), 10)
                        pos_y2 = randrange(0, (height - tam - placar), 10)
                        maca_x = randrange(0, (width - tam), 10)
                        maca_y = randrange(0, (height - tam - placar), 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        velocidade_y2 = 0
                        velocidade_x2 = 0
                        relogio = pygame.time.Clock()
                        Cobra_xy = []
                        Cobra2_xy = []
                        maximo = 1
                        maximo2 = 1
                    if event.key == pygame.K_s:
                        sair = False
                        fim_de_jogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if 180 > x > 45 and 147 > y > 120:
                        sair = True
                        fim_de_jogo = False
                        pos_x1 = randrange(0, (width - tam - placar), 10)
                        pos_y1 = randrange(0, (height - tam), 10)
                        maca_x = randrange(0, (width - tam), 10)
                        maca_y = randrange(0, (height - tam - placar), 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        relogio = pygame.time.Clock()
                        Cobra_xy = []
                        maximo = 1
                    elif 265 > x > 190 and 147 > y > 120:
                        sair = False
                        fim_de_jogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tam:
                    velocidade_y = 0
                    velocidade_x = -tam
                if event.key == pygame.K_RIGHT and velocidade_x != -tam:
                    velocidade_y = 0
                    velocidade_x = tam
                if event.key == pygame.K_UP and velocidade_y != tam:
                    velocidade_x = 0
                    velocidade_y = -tam
                if event.key == pygame.K_DOWN and velocidade_y != -tam:
                    velocidade_x = 0
                    velocidade_y = tam
                if event.key == pygame.K_a and velocidade_x2 != tam2:
                    velocidade_y2 = 0
                    velocidade_x2 = -tam2
                if event.key == pygame.K_d and velocidade_x2 != -tam2:
                    velocidade_y2 = 0
                    velocidade_x2 = tam2
                if event.key == pygame.K_w and velocidade_y2 != tam2:
                    velocidade_y2 = -tam2
                    velocidade_x2 = 0
                if event.key == pygame.K_s and velocidade_y2 != -tam2:
                    velocidade_y2 = tam2
                    velocidade_x2 = 0
        window.fill(white)
        pos_x1 += velocidade_x
        pos_y1 += velocidade_y
        pos_x2 += velocidade_x2
        pos_y2 += velocidade_y2

        if pos_x1 == maca_x and pos_y1 == maca_y:
            maca_x = randrange(0, (width - tam), 10)
            maca_y = randrange(0, (height - tam - placar), 10)
            maximo += 1

        if pos_x2 == maca_x and pos_y2 == maca_y:
            maca_x = randrange(0, (width - tam), 10)
            maca_y = randrange(0, (height - tam - placar), 10)
            maximo2 += 1

        if pos_x1 + tam > width:
            pos_x1 = 0
        if pos_x1 < 0:
            pos_x1 = width - tam
        if pos_y1 + tam > height - placar:
            pos_y1 = 0
        if pos_y1 < 0:
            pos_y1 = height - tam - placar

        if pos_x2 + tam2 > width:
            pos_x2 = 0
        if pos_x2 < 0:
            pos_x2 = width - tam2
        if pos_y2 + tam2 > height - placar:
            pos_y2 = 0
        if pos_y2 < 0:
            pos_y2 = height - tam2 - placar

        cobraInicio = []
        cobraInicio.append(pos_x1)
        cobraInicio.append(pos_y1)
        Cobra_xy.append(cobraInicio)

        cobraInicio2 = []
        cobraInicio2.append(pos_x2)
        cobraInicio2.append(pos_y2)
        Cobra2_xy.append(cobraInicio2)

        while True:
            if len(Cobra_xy) > maximo:
                del Cobra_xy[0]
            else:
                break

        while True:
            if len(Cobra2_xy) > maximo2:
                del Cobra2_xy[0]
            else:
                break

        if any(Bloco == cobraInicio for Bloco in Cobra_xy[:-1]):
            fim_de_jogo = True

        if any(Bloco == cobraInicio2 for Bloco in Cobra2_xy[:-1]):
            fim_de_jogo = True

        for Bloco in Cobra2_xy:
            if maximo == 0:
                ganhou = 2
                fim_de_jogo = True

            elif Cobra_xy[-1] == Bloco:
                maximo -= 1

        for Bloco in Cobra_xy:
            if maximo2 == 0:
                ganhou = 1
                fim_de_jogo = True

            if Cobra2_xy[-1] == Bloco:
                maximo2 -= 1


        pygame.draw.rect(window, black, (0, height - placar, width, placar))
        cobra(Cobra_xy, blue)
        cobra(Cobra2_xy, green)
        texto(f'Pontuação P1: {maximo}', white, 20, 10, height - 20)
        texto(f'Pontuação P2: {maximo2}', white, 20, 150, height - 20)
        maca(maca_x, maca_y)
        relogio.tick(15)
        pygame.display.update()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

width = 320
height = 280
tam = 10
tam2 = 10
placar = 40

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

jogo()

pygame.quit()
