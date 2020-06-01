import speech_recognition as sr
from googletrans import Translator
import pocketsphinx as ps
from pocketsphinx import sphinxbase, get_model_path

def main(): 

    sound = "prueba/nata3.wav"

    r = sr.Recognizer()
    translator = Translator()

    model_path = get_model_path()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        r.listen(source)
        print("Convirtiendo Audio File...")

        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='es-ES')
            print("Converted Audio is: \n" + texto)
            aux = translator.detect(texto)
            print(aux)
            traducido = translator.translate(texto)
            print(traducido)
            print("Tu audio: " + traducido.text)
        except Exception as e:
            print(e)

    with sr.Microphone() as source:
        while texto != "salir":
            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)

            try:
                texto = r.recognize_google(audio, language='es-ES')
                print("Tu Audio: \n" + texto)
                aux = translator.detect(texto)
                traducido = translator.translate(texto)
                print("Converted Audio is: " + traducido.text)
            except Exception as e:
                print(e)
            
    #with sr.Microphone() as source:
    #    while True:
    #        audio = r.listen(source)

            # recognize speech using Sphinx
    #        try:
    #            # Just pass a language parameter
    #            print("Sphinx thinks you said: " + r.recognize_sphinx(audio, language="es-ES"))
    #        except sr.UnknownValueError:
    #            print("Sphinx could not understand audio")
    #        except sr.RequestError as e:
    #            print("Sphinx error; {0}".format(e))

        # print(r.recognize_sphinx(audio))

if __name__ == "__main__":
    main()


    # https://www.youtube.com/watch?v=q-N6IcgCqCE
    # https://programacionpython80889555.wordpress.com/2019/12/03/obteniendo-texto-de-un-archivo-de-audio-en-python-con-speechrecognition/
    # https://www.youtube.com/watch?v=hMg9KZG6iSI 
    # https://pypi.org/project/translate/
    # https://pypi.org/project/googletrans/
    # https://audio.online-convert.com/es/convertir-a-wav 

    #https://www.ibm.com/co-es/cloud/watson-speech-to-text
    #https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
    #https://stackoverrun.com/es/q/6847093
    #https://realpython.com/playing-and-recording-sound-python/#python-sounddevice_1
    #https://stackoverflow.com/questions/892199/detect-record-audio-in-python
    #https://www.youtube.com/watch?v=jFw28yFO_SQ
    #https://swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/
    #https://pypi.org/project/AudioConverter/
    #https://pypi.org/project/ftransc/
    #https://stackoverflow.com/questions/57761964/how-can-take-file-id-voice-in-python-telegram-bot
    #https://python-telegram-bot.readthedocs.io/en/stable/telegram.voice.html


    #https://www.youtube.com/watch?v=T-l2OIJAy8Q
    #https://blog.eonidi.com/index.php/2018/01/24/reconocimiento-de-voz-tiempo-real-en-idioma-espanol-con-pocketsphinx/
    #https://github.com/richiprieto/SpeechRecognition/blob/master/simpleSpeech.py
    #https://www.youtube.com/watch?v=1zf_-GuMboA
    #https://www.youtube.com/watch?v=uU0N1uowVig
    