d = {
	480:'Alice',
	256:'Bob',
	546:'Tim'
	}
	
def greeting(userid):
	try:
	return 'Hi,{}'.format(d[userid])
	execpt ValueError:
	raise 'Hi there!'
	
	
def greeting(userid):
	if d[userid]:
		return 'Hi,{}'.format(d[userid])
	return 'Hi there!'
	
	
def greeting(userid):
	return 	'Hi',{
	480:'Alice',
	256:'Bob',
	546:'Tim'
	}.get(d[userid],'there!')
	
	