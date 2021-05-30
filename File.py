with open('file.txt', 'w') as file:
	file.write("Python and Jesse built this file!")
with open('file.txt', 'a') as file:
	file.write('\nJesse')
with open('file.txt', 'r') as file:
	print(file.read())