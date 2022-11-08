print("TASK №1-2")
spisok = []
word = 0
ending = 0
last_word = 0

while True:
	word = input()
	if word == 'end':
		print("WORD LIST:", spisok, sep="")
		break
	else:
		spisok.append(word)