'''prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)'''
#using flags
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
#Using break to Exit a Loop
#Using continue in a Loop