import re
text='Today it is a a sunny day in in Spain'
print(re.findall(r'(\b\w+)\s+\1', text))