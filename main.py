import pyttsx3 #Se necesita insatal esta libreria para que sirva
from deep_translator import GoogleTranslator #Se nesecita para traducir texto

robot = pyttsx3.init() #Inicializar el motor pyttsx3 (Se encarga de 'hablar')

text = input("Escribe lo que quieras que diga el robot /") #Lo que respondan es lo que va adecir
voices = robot.getProperty('voices') #Trae una lista de todas las voces disponibles
# Recorremos la lista de voces y mostramos información
for index, voice in enumerate(voices):
    print(f"Voz {index}:")
    print(f" - ID: {voice.id}")            # Identificador interno de la voz
    print(f" - Nombre: {voice.name}")      # Nombre de la voz
    print(f" - Idioma: {voice.languages}") # Lenguajes que soporta
    print(f" - Género: {voice.gender}")    # Puede aparecer "VoiceGenderMale/Female"
    print("-----------------------")
numVoice =int(input("Escribe el numero de la voz que quieras poner /"))

#Se configura la voz
robot.setProperty('rate', 250) #La velocidad del robot al habalar (100 es "normal")
robot.setProperty('volume', 1) #El Volumen del robot al hablar (0.1 es vastante vajo,y 1 es "normal")
robot.setProperty('voice', voices[numVoice].id) #Se abre una lista de las voces o idiomas que tenemos disponibles

#Se prende el robot
robot.say(text)
robot.runAndWait()

preg =  input("¿Quieres traducir este texto? (Responde 'Si' o 'No') /") #Pregunta para traducir

if preg == "Si":
    preg2 = int(input("¿A que idioma lo quieres traducir? (Responde el numero de la voz que tenga el idioma) /")) #Pregunta para saber a que idioma lo quiere traducir
    if preg2 == 0:
        #Traducir el tecto a español
        traductor = GoogleTranslator(source= 'en' , target= 'es' )
        texto_traducido1 = traductor.translate(text)
        print(texto_traducido1)
      
        #Robot dice la traducción
        robot.say(texto_traducido1)
        robot.runAndWait()
      
    else:
        #Traducir el texto a español
        traductor = GoogleTranslator(source= 'es' , target= 'en' )
        texto_traducido2 = traductor.translate(text)
      
        #Robot dice la traducción
        robot.say(texto_traducido2)
        robot.runAndWait()

else: #Si no quiere traducir el texto
    print("Vale =)")
    robot.stop()
