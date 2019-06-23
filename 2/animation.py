# Анимация
# Сиденко Анастасия, ИУ7-23Б

# x0, y0, n, k - начальные положения
# deltax, deltay, delta - приращения движения
# clock - таймер
# running, i - вспомогательные переменные в циклах

import pygame
from pygame import *
from math import *

# Инициализация модуля анимации
pygame.init()
size = (900, 640)
screen = pygame.display.set_mode(size)

# Начальные параметры
clock = pygame.time.Clock()
deltax = [0,0,0,0]
n = [0,43,86,120]
x0 = [0,430,860,430]
y0 = [0,215,-43,-315]
deltay = [0,0,0,0]
delta = 0
k = 0

# Запуск основного цикла
running = True    
while running:
    # Выход из программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем фон       
    screen.fill((175, 238, 238))
    pygame.draw.ellipse(screen, (0,128,0), [-50,30,950,630], 0)
    pygame.draw.ellipse(screen, (0,0,255), [98,158,648,378], 0)

    
    for i in range(0,4):
        # Рисуем неизменяемые части человека
        pygame.draw.line(screen, (0,0,0),
                         [10+deltax[i]+x0[i],340+deltay[i]+y0[i]],
                         [10+deltax[i]+x0[i],390+deltay[i]+y0[i]], 15)
        pygame.draw.circle(screen, (240,230,140),
                           [10+deltax[i]+x0[i],340+deltay[i]+y0[i]], 15)
        
        # Рисуем ноги и руки, при движении
        if n[i]%4 == 0:
            pygame.draw.line(screen, (0,0,0),
                             [10+deltax[i]+x0[i],360+deltay[i]+y0[i]],
                             [30+deltax[i]+x0[i],375+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (0,0,0),
                             [10+deltax[i]+x0[i],360+deltay[i]+y0[i]],
                             [-10+deltax[i]+x0[i],375+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (128,0,128),
                             [10+deltax[i]+x0[i],390+deltay[i]+y0[i]],
                             [30+deltax[i]+x0[i],410+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (128,0,128),
                             [10+deltax[i]+x0[i],390+deltay[i]+y0[i]],
                             [-10+deltax[i]+x0[i],410+deltay[i]+y0[i]], 5)
        if n[i]%4 == 1 or n[i]%4 == 3:
            pygame.draw.line(screen, (0,0,0),
                             [10+deltax[i]+x0[i],360+deltay[i]+y0[i]],
                             [0+deltax[i]+x0[i],380+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (0,0,0),
                             [10+deltax[i]+x0[i],360+deltay[i]+y0[i]],
                             [20+deltax[i]+x0[i],380+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (128,0,128),
                             [10+deltax[i]+x0[i],390+deltay[i]+y0[i]],
                             [0+deltax[i]+x0[i],415+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (128,0,128),
                             [10+deltax[i]+x0[i],390+deltay[i]+y0[i]],
                             [20+deltax[i]+x0[i],415+deltay[i]+y0[i]], 5)
        elif n[i]%4 == 2:
            pygame.draw.line(screen, (0,0,0),
                             [10+deltax[i]+x0[i],360+deltay[i]+y0[i]],
                             [10+deltax[i]+x0[i],385+deltay[i]+y0[i]], 5)
            pygame.draw.line(screen, (128,0,128),
                             [10+deltax[i]+x0[i],390+deltay[i]+y0[i]],
                             [10+deltax[i]+x0[i],420+deltay[i]+y0[i]], 5)
            
        # Меняем направление движения
        if n[i] < 43:
            deltax[i] = deltax[i] + 10
            deltay[i] = deltay[i] + 5
        elif n[i] < 86:
            deltax[i] = deltax[i] + 10
            deltay[i] = deltay[i] - 6
        elif n[i] < 120:
            if n[i] == 86:
                deltay[i] = deltay[i] - 10
            deltax[i] = deltax[i] - 10
            deltay[i] = deltay[i] - 8
        else:
            deltax[i] = deltax[i] - 10
            deltay[i] = deltay[i] + 3

        n[i] = n[i]+1

        # Выходим и заходим вновь на фон
        if n[i] > 180:
            x0[i] = 0
            y0[i] = 0
            n[i] = 0
            deltax[i] = 0
            deltay[i] = 0

    # Рисуем рыбок
    if k < 100:
        # Туловище, неизменяемая часть
        pygame.draw.ellipse(screen,(255,255,0),[130+delta,340,40,20],0)
        pygame.draw.ellipse(screen,(255,0,0),[630-delta,360,40,20],0)

        # Движение хвостом
        if k%2 == 0:
            pygame.draw.polygon(screen,(255,165,0),
                                [(130+delta,350),(115+delta,345),(125+delta,335)],0)
        else:
            pygame.draw.polygon(screen,(255,165,0),
                                [(130+delta,350),(115+delta,355),(125+delta,365)],0)
        if k%2 == 0:
            pygame.draw.polygon(screen,(0,255,255),
                                [(670-delta,370),(685-delta,365),(675-delta,355)],0)
        else:
            pygame.draw.polygon(screen,(0,255,255),
                                [(670-delta,370),(685-delta,375),(675-delta,385)],0)

        delta = delta + 5
    # Движение рыбок в обратную сторону   
    elif k < 200:
        if k == 100:
            delta = 0

        # Неизменяемое тело
        pygame.draw.ellipse(screen,(255,0,0),[130+delta,360,40,20],0)
        pygame.draw.ellipse(screen,(255,255,0),[630-delta,340,40,20],0)

        # Хвост
        if k%2 == 0:
            pygame.draw.polygon(screen,(0,255,255),
                                [(130+delta,370),(115+delta,365),(125+delta,355)],0)
        else:
            pygame.draw.polygon(screen,(0,255,255),
                                [(130+delta,370),(115+delta,375),(125+delta,385)],0)
        if k%2 == 0:
            pygame.draw.polygon(screen,(255,165,0),
                                [(670-delta,350),(685-delta,345),(675-delta,335)],0)
        else:
            pygame.draw.polygon(screen,(255,165,0),
                                [(670-delta,350),(685-delta,355),(675-delta,365)],0)

        delta = delta + 5
    else:
        k = 0
        delta = 0

    k = k+1
    
    # Рисуем и увеличиваем время    
    pygame.display.flip()
    clock.tick(5)
    
pygame.quit()
