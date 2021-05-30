y={0:{'Jesse Leite',23,'Best computer Engineer'},1:{'Lana Rhoades',22,'Best pleasure professional'}}
with open('file.txt', 'w') as file:
	file.write("Python and Jesse built this file!")
with open('file.txt', 'a') as file:
	file.write('\nJesse\n'+str(y)+'\n'+str(y))
inf=[]
with open('file.data', 'r') as file:
	for row in file.readlines():
		inf.append(row.split(','))

data=[]
with open('file.txt', 'r') as file:
		a=file.read()+'\n'
with open('file.data', 'w') as file:
	file.write(str(y))
with open('file.data', 'r') as file:
	for row in file.readlines():
		data.append(row.split(','))

aa=inf[0][0]+inf[0][1]+inf[0][2]
ab=str(aa)

a0=data[0][0]+data[0][1]+data[0][2]
a1='       Data from .TXT file:\n\n'+str(a0)+'\n\n----------------------------------------------------------\n       Data from .DATA file:\n\n'+ab
a2=a1.translate({ord(i): None for i in "["})
a3=a2.translate({ord(i): None for i in "]"})
a4=a3.translate({ord(i): None for i in ","})
a5=a4.translate({ord(i): None for i in "{"})
a6=a5.translate({ord(i): None for i in "}"})
a7=a6.translate({ord(i): None for i in ":"})
a8=a7.translate({ord(i): '\n' for i in "'"})
print(a8)
