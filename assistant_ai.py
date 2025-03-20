from elevenlabs import save
from elevenlabs.client import ElevenLabs
from g4f.client import Client
from history_chat import History

class AssistAI:
    def __init__(self, api_key: str|None = None, prompt: str|None = None):
        '''If *api_key* of ElevenLabs is None, *text_to_speech* can't is usabled'''
        self.client_gpt = Client();
        if api_key is not None:
            self.client_voice = ElevenLabs(api_key=api_key);
        self.conversation = History(prompt);

    def response(self, msg:str):
        '''Start conversation with AI; Return response message'''
        self.conversation.add(msg);
        response = self.client_gpt.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.conversation.chat
        );
        self.conversation.add_response(response);
        return response.choices[0].message;

    def text_to_speech(self, voice_id: str, text: str, model_id: str|None = "eleven_multilingual_v2"):
        '''Transform text to speech; Return speech'''
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

if __name__ == "__main__":
    print("U can't use this python file like main");