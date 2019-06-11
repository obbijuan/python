l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
	for word in words:
		print(func(word))

<<<<<<< HEAD
# def sample_func(word):
# 	return word.capitalize()


# sample_func = lambda word: word.capitalize()
# change_words(l, sample_func)

# Con lambda se reduce la cantidad de codigo a escribir
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())
=======
def sample_func(word):
	return word.capitalize()


change_words(l, sample_func)

	# asdfasdfadfa
>>>>>>> 08e9e44b74cc18c4b077d4abc4f4384c8625006c
