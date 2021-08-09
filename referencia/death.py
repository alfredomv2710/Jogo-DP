import pygame
import random
from os import path
WIDTH = 480
HEIGHT = 600
from config import GAME, QUIT, INIT, IMG_DIR, FNT_DIR


def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    pygame.mixer.init()
    background = pygame.image.load(path. join(IMG_DIR , 'starfield - Copia.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    score_font = pygame.font.Font(path. join(FNT_DIR, 'PressStart2P.ttf'), 14)

    with open(path.join(path.dirname(__file__) , 'score.txt'), 'r') as arquivo:
        score = arquivo.read() # Obtem a pontuação que o jogo obteve, está que ficou salva no arquivo indicado
        score = int(score)
        running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(60)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:  #Verifica se o jogador decidio jogar novamente
                    state = INIT
                    running = False

        
        #=================== desenha a pontuação que o jogador obteve e o resto da tela =========================
        text_surface = score_font.render("Your score:{:08d}".format(score), True, (50, 100, 50))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  (HEIGHT/2) - 10)
        screen.blit(background, background_rect)
        screen.blit(text_surface, text_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state