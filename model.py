import pygame

pygame.init();
display = pygame.display.set_mode((1280, 720));
pygame.display.set_caption("Vtuber Model");
clock = pygame.time.Clock();
dt = 0;

vtuber_image = pygame.image.load('assets/neutral/vtuber.png');
vtuber_vec = pygame.Vector2(display.get_width()/2-vtuber_image.get_width()/2, display.get_height()/2-vtuber_image.get_height()/2);

pressed_e = False;
pressed_w = False;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit();
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_e:
                    pressed_e = True;
                case pygame.K_w:
                    pressed_w = True;
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_e:
                    pressed_e = False;
                case pygame.K_w:
                    pressed_w = False;

    display.fill("green");

    pressed = pressed_e+pressed_w;
    match pressed:
        case 0:
            vtuber_image = pygame.image.load('assets/neutral/vtuber.png');
        case 1:
            if pressed_w == True:
                vtuber_image = pygame.image.load('assets/neutral/vtuber_speak.png');
            if pressed_e == True:
                vtuber_image = pygame.image.load('assets/neutral/vtuber_closed.png');
        case 2:
            vtuber_image = pygame.image.load('assets/neutral/vtuber_closed_speak.png');
    
    display.blit(vtuber_image, vtuber_vec);

    pygame.display.flip();
    dt = clock.tick(60);