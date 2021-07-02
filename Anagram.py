def is_anagram(s,s1):
	if len(s)!=len(s1):
		return False
	else:
		for i, j in zip(s, s1):
			if i!=j:
				return False
		return True
s=input('Type in the first word\n')
s1=input('Type in the second word\n')
s=sorted(s.lower())
s1=sorted(s1.lower())
res=is_anagram(s, s1)
if res==True:
	print('Anagram')
else:
	print('Not anagram')