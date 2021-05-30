y={0:{'Jesse Leite',23,'Best computer Engineer'},1:{'Lana Rhoades',22,'Best pleasure professional'}}
with open('file.txt', 'w') as file:
	file.write("Python and Jesse built this file!")
with open('file.txt', 'a') as file:
	file.write('\nJesse\n'+str(y))
with open('file.txt', 'r') as file:
	print(file.read())
