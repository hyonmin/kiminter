def profile(name, age, main_lang):
	print("name: {0}\t age: {1}\t most skillful language: {2}" \
	.format(name, age, main_lang))
	
profile("Kim", 20, "Python")
profile("Lee", 25, "Java")

def profile2(name, age = 17, main_lang="Python"):
	print("name: {0}\t age: {1}\t most skillful language:{2}" \
	.format(name, age, main_lang))
	
profile2("Kim")
profile2("Lee")
profile2("Chu", 29)

def profile3(name, age, main_lang):
	print(name, age, main_lang)
	
profile3(name = "kim", main_lang="Python", age = 20)
profile3(main_lang = "Java", age=25, name = "Lee")


def profile4(name, age, *language):
	print("name: {0}\tage: {1} \t" .format(name, age), end = "")
	
	i = 0
	for lang in language:
		l = len(language)
		i += 1
		if i == l:
			print(lang)
		else:
			print(lang, end = ", ")

profile4("Yu", 29, "Python", "Java")
profile4("Lee", 28, "Java", "C++", "C#", "Python")

guns = 10

def checkpoint(guns, soldiers):
	guns -= soldiers
	print("Guns in the cabinet: {0}" .format(guns))
	return guns
	
print("Guns in the cabinet: {0}" .format(guns))
guns = checkpoint(guns, 2)
print("Guns in the cabinet: {0}" .format(guns))

'''
Q6) Make a code to calculate the standard weight.
* standard weight: It can be calculated by a height-weight combination.

male: height(m) * height(m) * 22
female: height(m) * height(m) * 21

condition 1:
	* name of the function = std_weight
	* values: height, gender
condition 2: The weight should be 2 places of decimals
'''

def std_weight(gender, height):
	if gender.upper() == "MALE":
		idx = 22
	elif gender.upper() == "FEMALE": 
		idx = 21
	else: return "Not a proper input"
	return round(idx*height**2, 2)

height = float(input("Your height?: "))
gender = input("Male or Female?: ")
print("Your standard weight: {0}" .format(std_weight(gender, height)))
