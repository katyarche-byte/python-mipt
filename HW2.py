import pygame
pygame.init()

screen = pygame.display.set_mode((1152, 768))
pygame.display.set_caption("Панда")

# Создаем шрифт для отображения координат
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255,175,128))  #фон
   
    mx, my = pygame.mouse.get_pos()
    text = font.render(f"x: {mx}, y: {my}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

   #бамбук слева
    pygame.draw.rect(screen, (0, 104, 55), (350, 450, 15, 120))  
    
    pygame.draw.rect(screen, (0, 104, 55), (345, 325, 15, 130))  
    
    pygame.draw.rect(screen, (0, 104, 55), (340, 200, 15, 130))  
    
    pygame.draw.rect(screen, (0, 104, 55), (335, 80, 15, 130))   
   
    # 4 изогнутые ветки от левого бамбука
    pygame.draw.arc(screen, (0, 104, 55), (345, 300, 50, 80), 0, 1.57, 2)  # Ветка 1
    pygame.draw.arc(screen, (0, 104, 55), (320, 350, 60, 50), 3.14, 4.71, 2)  # Ветка 2
    
    # Ветки от третьего сегмента
    pygame.draw.arc(screen, (0, 104, 55), (340, 180, 70, 60), 0, 1.57, 2)  # Ветка 3
    pygame.draw.arc(screen, (0, 104, 55), (300, 220, 80, 40), 3.14, 4.71, 2)  # Ветка 4
    
    # Листья на ветках левого бамбука
    pygame.draw.ellipse(screen, (0, 140, 70), (395, 300, 40, 18))  # На ветке 1
    pygame.draw.ellipse(screen, (0, 140, 70), (290, 370, 35, 15))  # На ветке 2
    pygame.draw.ellipse(screen, (0, 140, 70), (410, 190, 45, 20))  # На ветке 3
    pygame.draw.ellipse(screen, (0, 140, 70), (250, 230, 38, 16))  # На ветке 4
    
    # Вторая ветка бамбука (толще, правая) 
    pygame.draw.rect(screen, (0, 104, 55), (570, 450, 25, 120)) 
    
    pygame.draw.rect(screen, (0, 104, 55), (575, 325, 25, 130))  
    
    pygame.draw.rect(screen, (0, 104, 55), (580, 200, 25, 130)) 
    
    pygame.draw.rect(screen, (0, 104, 55), (585, 80, 25, 130))  
    
    # 3 изогнутые ветки от правого бамбука (от 2 и 3 сегментов)
    # Ветки от второго сегмента
    pygame.draw.arc(screen, (0, 104, 55), (575, 300, 60, 70), 1.57, 3.14, 2)  # Ветка 1
    pygame.draw.arc(screen, (0, 104, 55), (600, 350, 50, 60), 4.71, 6.28, 2)  # Ветка 2
    
    # Ветка от третьего сегмента
    pygame.draw.arc(screen, (0, 104, 55), (580, 170, 80, 80), 1.57, 3.14, 2)  # Ветка 3
    
    # Листья на ветках правого бамбука
    pygame.draw.ellipse(screen, (0, 140, 70), (550, 290, 42, 19))  # На ветке 1
    pygame.draw.ellipse(screen, (0, 140, 70), (640, 380, 38, 17))  # На ветке 2
    pygame.draw.ellipse(screen, (0, 140, 70), (540, 160, 46, 21))  # На ветке 3
 
    # Тело панды
    pygame.draw.ellipse(screen, (255, 255, 255), (500, 370, 350, 200))
    
    # Голова
    pygame.draw.circle(screen, (255, 255, 255), (675, 320), 120)
    
    # Уши
    pygame.draw.circle(screen, (0, 0, 0), (600, 240), 40)
    pygame.draw.circle(screen, (0, 0, 0), (750, 240), 40)
    
    # Глаза
    pygame.draw.ellipse(screen, (0, 0, 0), (620, 290, 50, 70))
    pygame.draw.ellipse(screen, (0, 0, 0), (700, 290, 50, 70))
    
    # Нос
    pygame.draw.ellipse(screen, (0, 0, 0), (660, 350, 30, 20))
    
    # Лапы
    pygame.draw.ellipse(screen, (0, 0, 0), (480, 420, 80, 120))  # Левая передняя
    pygame.draw.ellipse(screen, (0, 0, 0), (790, 420, 80, 120))  # Правая передняя
    pygame.draw.ellipse(screen, (0, 0, 0), (530, 550, 100, 80))  # Левая задняя
    pygame.draw.ellipse(screen, (0, 0, 0), (720, 550, 100, 80))  # Правая задняя
    
    pygame.draw.ellipse(screen, (0, 0, 0), (520, 390, 60, 80))
    pygame.draw.ellipse(screen, (0, 0, 0), (770, 390, 60, 80))

    pygame.display.flip()

pygame.quit()
