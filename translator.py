
import googletrans
from googletrans import Translator
trans=Translator()
t= trans.translate(input('Enter text to be translated:'))
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'Text: {t.origin}')
print(f'Translated Text: {t.text}')
