""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string  
from collections import Counter

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	#storyFull = open(file_name).read()

	storyEdit = []
	word_list = []
	
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	for row in lines:
	 	row = row.lower()
	 	row = row.translate(string.maketrans("",""), string.punctuation)
	 	storyEdit += row.split()

	return storyEdit


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	

	c = Counter(word_list)
	topWords = []
	#for i in range(0,n - 1):
		#topWords[i] = c[i]
		#print c(i)

	#return topWords
	return c



#print get_word_list('test.txt')
#print get_word_list('pg32325.txt')
print get_top_n_words(get_word_list('pg32325.txt'), 10)

