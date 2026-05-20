from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source='en', target='es')

# Texto que deseas traducir
texto_ingles = "Hello, how are you today?"

# Configuramos el traductor de inglés ('en') a español ('es')
traductor = GoogleTranslator(source='en', target='es')

# Traducimos el texto
texto_espanol = traductor.translate(texto_ingles)

print(f"Texto original: {texto_ingles}")
print(f"Texto traducido: {texto_espanol}")



