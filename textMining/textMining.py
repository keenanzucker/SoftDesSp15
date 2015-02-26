"""Quentin Tarantino Film Analysis! This program examines six of Tarantino's most famous films. The language in his films has
changed over the years, so I examined three catagories of his sripts: the use of profanity, the use of academic words, and the 
average word lengths. I then plotted this infomration to give a visual representation."""

from pattern.web import *
from pattern.en import *
from pattern.web import *
from pattern.en.wordlist import *
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def getScripts():
	"""This function was first used to parse online scripts from HTML code and turn it into seperate text files. 
	That code has been commented out. The rest of the fuction returns a list of the scripts of six Tarantino films
	as plain words."""


	"""scriptText = URL('http://www.weeklyscript.com/Reservoir+Dogs.html').download()

	scriptText = plaintext(scriptText)
	print scriptText

	file = open('reservoirdogs', 'w')
	file.write(scriptText)"""


	scripts = [open('reservoirdogs.txt').read(), open('pulpfiction.txt').read(), open('jackiebrown.txt').read(), open('killbill.txt').read(), open('inglouriousbasterds.txt').read(), open('djangounchained.txt').read() ]

	return scripts

def ProfaneWords():
	"""This funciton loops through all of the films, searching for profane words. It returns a list with the count of swear words in each film"""

	swearCount = [0,0,0,0,0,0]
	scripts = getScripts()

	for i in range(0,len(scripts)):
		for word in scripts[i].split():
			if word in PROFANITY:
				swearCount[i] +=  1
		
	return swearCount

def AcademicWords():
	"""This funciton loops through all of the scripts, searching for academic words. It returns a list with the count of academic words in each film"""

	smartCount = [0,0,0,0,0,0]
	scripts = getScripts()

	for i in range(0,len(scripts)):
		for word in scripts[i].split():
			if word in ACADEMIC:
				smartCount[i] += 1
		
	return smartCount


def wordLen():
	"""This functions loops through all the scripts as well, but it counts the number of letters in each word, and then divides by the total number
	of words in each script to give an average word length."""

	wordLengths = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	scripts = getScripts()

	for i in range(0,len(scripts)):
		for word in scripts[i].split():
			
			wordLengths[i] += len(word)
		wordLengths[i] = wordLengths[i] / len(scripts[i].split())
		

	return wordLengths

def plotter():
	"""This function plots the number of academic and profane words together on one plot, to give a sense of how Tarantino's films have changed
	over time with regards to language. It also plots a bar graph of the average number of letters per word in each of the films."""

	titles = ['reservoirdogs', 'pulpfiction','jackiebrown', 'killbill', 'inglouriousbasterds', 'djangounchained']
	years = [1992, 1994, 1997, 2003, 2009, 2012]

	X = linspace(0, len(getScripts()))
	P = ProfaneWords()
	A = AcademicWords()
	WL = wordLen()

	plt.plot(years, P, label = 'PROFANITY', marker = 'o')
	plt.plot(years, A, label = 'ACADEMIC', marker = 'o')
	ylabel('Number of Word Instances')
	xlabel('Reservoir Dogs | Pulp Fiction | Jackie Brown | Kill Bill | Ingourious Basterds | Django Unchained')
	title('Quentin Tarantino Film Word Rating')
	legend(loc = 'upper left')

	fig = plt.figure()
	width = .75
	ind = np.arange(len(titles))
	plt.bar(ind, WL, width = 0.5, color = 'red')
	ylabel('Average Word Length in Letters')
	title('Average Word Lengths of Tarantino Films')
	plt.xticks(ind + width / 2, titles)

	fig.autofmt_xdate()

	plt.show()

#plotter()
print ProfaneWords()