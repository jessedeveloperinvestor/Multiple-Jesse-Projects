#pip install hashlib
from hashlib import sha256
import time
max_nounce=1000000
def SHA256(text):
	return sha256(text.encode('ascii')).hexdigest()
def mine(block_number, transactions, previous_hash, prefix_zeros):
	prefix_str='0'*prefix_zeros
	nonce=1
	while nonce <=max_nounce:
		text=str(block_number) + transactions + previous_hash + str(nonce)
		new_hash=SHA256(text)
		return new_hash
		if new_hash.startswith(prefix_str):
			print('Successfully mined bitcoins with '+nonce+' attempts')
			return new_hash
	raise BaseException('Bitcoins were not mined after '+nonce+' attempts')
if __name__=='__main__':
	transactions='''
	World->Jesse->100
	a->b->1
	'''
	difficulty=10000000000
	start=time.time()
	print('Mining got started')
	new_hash=mine(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
	total_time=str((time.time()-start))

	print('Mining ended. It took '+total_time+' seconds')
	print(new_hash)