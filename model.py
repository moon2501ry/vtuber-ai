import pygame

pygame.init();
display = pygame.display.set_mode((1280, 720));
pygame.display.set_caption("Vtuber Model");
clock = pygame.time.Clock();
dt = 0;

pygame.mixer.init();
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit();

    display.fill("green");
    vtuber_image = pygame.image.load('vtuber.png');
    vtuber_vec = pygame.Vector2(display.get_width()/2-vtuber_image.get_width()/2, display.get_height()/2-vtuber_image.get_height()/2);
    display.blit(vtuber_image, vtuber_vec);

    pygame.display.flip();
    dt = clock.tick(60);