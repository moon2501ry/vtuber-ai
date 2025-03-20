from assistant_ai import AssistAI
import pygame
from s import c # Private keys

vtuber = AssistAI(c.get('API-KEY'), c.get('PROMPT-INITIAL'));

pygame.mixer.init();
while True:
    _input = input("Fale: ");
    pygame.mixer.music.unload();
    response = vtuber.response(str(_input));
    print("Resposta:", response.content);
    vtuber.text_to_speech(c.get('MAN-ID'), response.content);
    vtuber.save_audio();
    pygame.mixer.music.load('audio.mp3');
    pygame.mixer.music.play();