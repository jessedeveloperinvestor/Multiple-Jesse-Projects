#pip install translate
from translate import Translator
text='Hello World'
i='english'
o='pt-br'
set = Translator(from_lang=i, to_lang=o)
y=set.translate(text)
print(y)
