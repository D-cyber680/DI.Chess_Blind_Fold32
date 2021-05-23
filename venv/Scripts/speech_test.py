import speech_recognition as sr

def get_audio():
     r = sr.Recognizer()
     with sr.Microphone() as mic:
         r.adjust_for_ambient_noise(mic)
         r.energy_threshold = 4000
         audio = r.listen(mic)
         said = ""
         print("Diga algo:")
         try:
             said = r.recognize_google(audio,language="es-MX")
             print(said)
         except Exception as e:
             print("Exception " + str(e))
     return said

get_audio()