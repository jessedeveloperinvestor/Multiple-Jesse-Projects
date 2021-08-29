import os
import time
print('Iterate over dirs and files:')
path = './'
for root, dirs, files in os.walk(path):
	print(root)
	for _dir in dirs:
		print(_dir)
	for _file in files:
		print(_file)
time.sleep(1000)
