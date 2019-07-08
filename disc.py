def dict(amount,total):
	if type(total)!=int and type(amount)!=int:
		return "invalid arguments"
	elif total<=0:
		return "zero error"
	else:
		return (amount/total)*100


