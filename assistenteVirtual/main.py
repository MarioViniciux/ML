import speech_recognition as sr
from gtts import gTTS
import tempfile
import os
import pygame
import time
import wikipedia
import webbrowser

def falar(texto):
    tts = gTTS(text = texto, lang = 'pt')
    
    with tempfile.NamedTemporaryFile(delete = False, suffix = '.mp3') as fp:
        caminho = fp.name
        tts.save(caminho)
    
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()
    os.remove(caminho)

def ouvir_microfone():
    recognizer = sr.Recognizer()

    index = 2 # Aqui tem que ser o index do dispositivo de entrada que esteja usando 

    with sr.Microphone(device_index = index) as source:
        print("DIGA ALGO...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language = 'pt-BR')
        print(f'Você disse: {comando}')
        return comando.lower()
    except sr.UnknownValueError:
        falar('Desculpe, não entendi o que você disse.')
        return ''
    except sr.RequestError:
        falar("Erro ao conectar com o serviço de voz.")
        return ''
    

def executar_comando(texto):
    wikipedia.set_lang('pt')

    if 'youtube' in texto:
        falar('Abrindo o YouTube.')
        webbrowser.open("https://www.youtube.com")

    elif 'pesquisar' in texto or 'wikipedia' in texto:
        assunto = texto.replace('pesquisar', '').replace('na wikipédia', '').strip()

        try:
            resumo = wikipedia.summary(assunto, sentences = 2)
            print(f'Resultado: {resumo}')
            falar(f'Aqui está o que encontrei sobre {assunto}: {resumo}')
        except wikipedia.exceptions.DisambiguationError:
            falar(f'Esse termo está muito vago. Pode ser mais específico?')
        except wikipedia.exceptions.PageError:
            falar('Não encontrei nada sobre esse assunto.')

    elif 'farmácia' in texto:
        falar('Procurando farmácias próximas')
        webbrowser.open('https://www.google.com/maps/search/farmácia+mais+próxima')
    
    elif 'sair' in texto or 'encerrar' in texto:
        falar('Encerrando o assistente. Nos vemos depois!')
        exit()

    else:
        falar('Desculpa, não reconheci o comando.')

def iniciar_assistente():
    print(sr.Microphone.list_microphone_names())
    falar('Olá! Eu sou uma intenção de assistente virtual. Pode falar um comando.')

    while True:
        comando = ouvir_microfone()

        if comando:
            executar_comando(comando)

if __name__ == '__main__':
    iniciar_assistente()
