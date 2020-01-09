country = input('哪國人啊:')
age = input('幾歲呢:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('去考照吧!')
	else:
		print('再等等吧!')