import speech_recognition as sr

def get_audio():
     r = sr.Recognizer()
     with sr.Microphone() as mic:
         r.energy_threshold = 4000
         audio = r.listen(mic)
         said = ""
         said2 = ""
         print("Diga algo:")
         try:
             said = r.recognize_google(audio,language="es-MX")
             print(said)
         except Exception as e:
             print("Exception " + str(e))
     return said

