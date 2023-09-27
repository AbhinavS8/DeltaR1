from googletrans import Translator

text=input('Enter your sentence: ')
lang=input('Enter the language code of preferred language: ')
translator=Translator()
translated=translator.translate(text,dest=lang)

print('Your sentence is in language code:',translated.src)
print('This sentence translates to:',translated.text)
