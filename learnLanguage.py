import googletrans
import speech_recognition as sr
import gtts
import playsound

input_lan = 'ar-ar'
output_lan = 'en'
recognizer = sr.Recognizer()
translator = googletrans.Translator()

try:
    with sr.Microphone() as  source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lan)
        print(text)

except:
    pass

translated = translator.translate(text, dest=output_lan)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lan)
converted_audio.save('romantic.mp3')
playsound.playsound('romantic.mp3')

#print(googletrans.LANGUAGES)
