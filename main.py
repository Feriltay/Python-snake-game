import pygame

# Oyun ekranının boyutunu belirleme
width = 500
height = 500

# Ekranı oluşturma
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yılan Oyunu")

# Yılanın başlangıç konumu
x = 250
y = 250

# Yılanın boyutu
snake_size = 10

# Yılanın görüntüsü
snake = pygame.Surface((snake_size, snake_size))
snake.fill((255, 255, 255))

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Klavyedeki tuşları işleme
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= snake_size
    if keys[pygame.K_RIGHT]:
        x += snake_size
    if keys[pygame.K_UP]:
        y -= snake_size
    if keys[pygame.K_DOWN]:
        y += snake_size
    
    # Sınırları belirleme
    if x < 0:
        x = 0
    if x > width - snake_size:
        x = width - snake_size
    if y < 0:
        y = 0
    if y > height - snake_size:
        y = height - snake_size
    
    # Yılanı ekrana çizme
    screen.fill((0, 0, 0))
    screen.blit(snake, (x, y))
    pygame.display.update()

pygame.quit()
