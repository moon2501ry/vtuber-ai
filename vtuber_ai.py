from elevenlabs import save
from elevenlabs.client import ElevenLabs
from g4f.client import Client

class VtuberAI:
    def __init__(self, api_key: str|None = None):
        self.client_gpt = Client();
        if api_key is not None:
            self.client_voice = ElevenLabs(api_key=api_key);
        self.conversa = [];

    def response(self):
        response = self.client_gpt.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.conversa
        );
        self.conversa.append(response.choices[0].message);
        return response.choices[0].message;

    def text_to_speech(self, voice_id: str, text: str, model_id: str|None = "eleven_multilingual_v2"):
        if self.client_voice is not None:
            self.speech = self.client_voice.text_to_speech.convert(
                voice_id=voice_id,
                model_id=model_id,
                text=text
            );
            return self.speech;
        else:
            print('api_key was not defined, please define it when creating the object');

    def save_audio(self, audio: bytes|None = None, filename: str|None = 'audio.mp3'):
        if audio is None:
            audio = self.speech;
        save(
            audio=audio,
            filename=filename
        );