#Jesse's Decriptor
#demo version

import time
print("Input single encrypted characters multiple times, then type 'ok' and hit enter")
#Decription
o = list()
while True:
    z = input('Enter the message:\n')
    if z=='a876':
        o.append(' ')
    if z=='242j':
        o.append('a')
    if z=='d03k' in z:
        o.append('b')
    if z=='1k6d' in z:
        o.append('8')
    if z=='p16x' in z:
        o.append('9')
    if z=='ok':
        print(o)
        time.sleep(30)
        quit()
