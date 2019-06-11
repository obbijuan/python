l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
	for word in words:
		print(func(word))

# def sample_func(word):
# 	return word.capitalize()


# sample_func = lambda word: word.capitalize()
# change_words(l, sample_func)

# Con lambda se reduce la cantidad de codigo a escribir
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
