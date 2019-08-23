from googletrans import Translator
translator = Translator()
a = translator.translate('안녕하세요.')
print(a.text)