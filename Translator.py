#pip install translate
from translate import Translator
print('Hello, write something in English and hit enter to get it translated')
z=0
while z<1:
    text=input()
    i='english'
    o='pt-br'
    set = Translator(from_lang=i, to_lang=o)
    y=set.translate(text)
    print(y)
    z=z-1
