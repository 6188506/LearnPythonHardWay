def mysum(*args):
	if isinstance(args[0], (int,float)):
		return sum(args)
	if isinstance(args[0], str):
		return ''.join(args)
	if isinstance(args[0], list):
		return [i for arg in args for i in arg]
	if isinstance(args[0], tuple):
		return (i for arg in args for i in arg)