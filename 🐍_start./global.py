x= 6
f="aftermath bitch"
def hello():
	global x 
	print(x)
	x+=7
	print("Tom",x)
def no_body():
	print(f)
	global x
	
	print(x)
	x=-9
	print(x)
hello()
no_body()
hello()