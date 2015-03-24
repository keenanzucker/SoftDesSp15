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

	storyEdit = []

	#Reads the file starting after the beginning	
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]


	#Loops through each row, making everything lowercase and replacing all punctuation
	for row in lines:
	 	row = row.lower()
	 	row = row.translate(string.maketrans("",""), string.punctuation)
	 	storyEdit += row.split()


	#Returns the final list as 
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
	

	wordCount = Counter(word_list)
	topWords = []

	orderedByFrequency = sorted(wordCount, key=wordCount.get, reverse=True)

	for i in range (0 , n):
		topWords.append(orderedByFrequency[i])

	return topWords


print get_top_n_words(get_word_list('pg32325.txt'), 100)

