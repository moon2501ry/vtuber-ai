from elevenlabs import save
from elevenlabs.client import ElevenLabs
from g4f.client import Client
import pygame

client_gpt = Client();
client_voice = ElevenLabs(
    api_key='''Your api Key'''
);

conversa = [{"role": "system", "content": "Observação: Não digite emojis com ou sem texto."}];

def trancription():
    trans = (
        audio='iaudio.mp3',
        model='whisper-1'
    );
    return trans

def response_gpt(chat):
    response = client_gpt.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat
    );
    return response.choices[0].message

def text_to_speech(txt):
    audio = client_voice.text_to_speech.convert(
        voice_id="WpGha869F6mWOt0gtKwb",
        model_id="eleven_multilingual_v2",
        text=txt
    );
    return audio

pygame.mixer.init()
while True:
    text = input('Você: ');
    conversa.append({"role": "user", "content": text});
    gpt = response_gpt(conversa);
    conversa.append(gpt);
    print('AI: '+str(gpt.content));
    pygame.mixer.music.unload();
    audio = text_to_speech(gpt.content);
    save(
        audio=audio,
        filename='audio.mp3'
    );
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()