#ЗАДАНИЕ 2
print("ЗАДАНИЕ №2")
spisok = []
word = 0
ending = 0
last_word = 0

while True:
	word = input()
	if word == 'end':
		print("СПИСОК СЛОВ:", spisok, sep="")
		break
	else:
		spisok.append(word)