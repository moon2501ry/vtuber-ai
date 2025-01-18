from vtuber_ai import VtuberAI

vtuber = VtuberAI(); #Colocar api-key dps
# espressões = VtuberAI(); #Expressões da Vtuber

vtuber.conversa.append({"role": "system", "content": "Você é uma Vtuber AI, que faz videos e lives para a Twitch e Youtube. Seu nome é Yamato. Fale em Português a menos que peçam."});
while True:
    _input = input("Fale com a Vtuber: ");
    vtuber.conversa.append({"role": "user", "content": str(_input)});
    response = vtuber.response();
    vtuber.conversa.append(response);
    print("Yamato:", response.content);
    # vtuber.text_to_speech(text=response.content);
    # vtuber.save_audio();