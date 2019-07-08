from disc import dict
def test_discounter():
	percentage=dict(10,100)
	assert percentage == 10
	a="10"
	b="0"
	percentage=dict(a,b)
	assert percentage=="invalid arguments"
	percentage=dict(10,0)
	assert percentage == "zero error"


