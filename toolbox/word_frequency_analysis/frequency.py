""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	#storyFull = open(file_name).read()

	storyEdit = []
	
	#for word in storyFull.split():
	#	storyEdit.append(word.lower())
		#for character in word:
			#if character != string.punctuation:
			#	storyEdit.append(character)

#	return storyEdit

	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
		lines = lines[curr_line+1:]
		for words in lines:
			print words

		if lines[curr_line].find('THE END') == curr_line:
			break
			#storyEdit.append(words.lower())

	#return storyEdit


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	pass


print get_word_list('pg32325.txt')

