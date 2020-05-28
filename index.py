import speech_recognition as sr
import time
from googletrans import Translator

def main(): 

    sound = "prueba4.wav"

    r = sr.Recognizer()
    translator = Translator()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("Convirtiendo Audio File...")

        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='es-ES')
            time.sleep(1.5)
            print("Converted Audio is: \n" + texto)
            aux = translator.detect(texto)
            print(aux)
            traducido = translator.translate(texto)
            print(traducido)
            print("Tu audio: " + traducido.text)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()


    # https://www.youtube.com/watch?v=q-N6IcgCqCE
    # https://programacionpython80889555.wordpress.com/2019/12/03/obteniendo-texto-de-un-archivo-de-audio-en-python-con-speechrecognition/
    # https://www.youtube.com/watch?v=hMg9KZG6iSI 
    # https://pypi.org/project/translate/
    # https://pypi.org/project/googletrans/
    # https://www.online-convert.com/es/resultado/b3f77994-1990-4460-9c94-704ff4f663a9 