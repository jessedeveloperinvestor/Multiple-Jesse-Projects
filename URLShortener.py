import pyshorteners
while True:
	try:
		url=input()
	except:
		url='https://app.simplegoods.co/i/LESTCGJK'
	s=pyshorteners.Shortener()
	print('Your shortened URL is: ', s.tinyurl.short(url), "Type 'exit' to exit")
	if url == 'exit':
		break