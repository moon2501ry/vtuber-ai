from elevenlabs import save
from elevenlabs.client import ElevenLabs
import pygame

client = ElevenLabs(
    api_key='''Your Api Key'''
);
voices = [
    'Normal', # WpGha869F6mWOt0gtKwb
    'Narrador', # poz8XrRMyzdPS6PBNzsP
    'Cute' # gAtZzIiYNgLCL9ad8dDp
];

def text_to_speech(txt, voice_id):
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        text=txt
    );
    return audio

while True:
    voice_choice = input('Escolha a Voz: ');
    match voice_choice:
        case 'normal':
            voice = "WpGha869F6mWOt0gtKwb";
            break;
        case 'narrador':
            voice = "poz8XrRMyzdPS6PBNzsP";
            break;
        case 'cute':
            voice = "gAtZzIiYNgLCL9ad8dDp";
            break;
        case _:
            print('Opções de vozes:');
            for i in voices:
                print(i);

pygame.mixer.init()
while True:
    text = input('Texto pra falar: ');
    pygame.mixer.music.unload();
    audio = text_to_speech(text, voice);
    save(
        audio=audio,
        filename='audio.mp3'
    );
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()