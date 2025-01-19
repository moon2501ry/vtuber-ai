from vtuber_ai import VtuberAI
import pygame
from s import c # Descarte

vtuber = VtuberAI(c.get('API-KEY'));
# espressões = VtuberAI(); #Expressões da Vtuber

vtuber.conversa.append({"role": "system", "content": c.get('PROMPT-INITIAL')});
pygame.mixer.init();
while True:
    _input = input("Fale com a Vtuber: ");
    if _input == 'quit':
        break;
    pygame.mixer.music.unload();
    vtuber.conversa.append({"role": "user", "content": str(_input)});
    response = vtuber.response();
    vtuber.conversa.append(response);
    print("Yamato:", response.content);
    vtuber.text_to_speech(voice_id=c.get('GIRL-ID'), text=response.content);
    vtuber.save_audio();
    pygame.mixer.music.load('audio.mp3');
    pygame.mixer.music.play();