
from pattern.web import *
from pattern.en import *
from pattern.web import *
from pattern.en.wordlist import *
from pickle import *
from pattern.web import URL, PDF
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

"""g = Google()

words = open('pulpfiction.txt').read().split()
words = [w for w in words if w not in ACADEMIC]
print words"""




"""scriptText = URL('http://www.weeklyscript.com/Reservoir+Dogs.html').download()

scriptText = plaintext(scriptText)
print scriptText

file = open('reservoirdogs', 'w')
file.write(scriptText)"""

scripts = [open('reservoirdogs.txt').read(), open('pulpfiction.txt').read(), open('jackiebrown.txt').read(), open('killbill.txt').read(), open('inglouriousbasterds.txt').read(), open('djangounchained.txt').read() ]

swearCount = [0,0,0,0,0,0]
smartCount = [0,0,0,0,0,0]
sentimentCount = [0,0,0,0,0,0]
count = 0
SC = [0]

counter = {'rd' : 0, 'pf' : 0, 'jb' : 0, 'kb' : 0, 'ib': 0, 'du' : 0 }
titles = ['reservoirdogs', 'pulpfiction','jackiebrown', 'killbill', 'inglouriousbasterds', 'djangounchained']
years = [1992, 1994, 1997, 2003, 2009, 2012]

for i in range(0,len(scripts)):
	for word in scripts[i].split():
		if word in PROFANITY:
			swearCount[i] +=  1
		if word in ACADEMIC:
			smartCount[i] += 1
		#sentimentCount[i] = sentiment(plaintext(scripts[i]))

print smartCount
print swearCount

X = linspace(0, len(scripts))
P = swearCount
A = smartCount

plt.plot(years, swearCount, label = 'PROFANITY')
plt.plot(years, smartCount, label = 'ACADEMIC')
ylabel('Number of Instances')
xlabel('film year')
title('Quentin Tarantino Films')
legend(loc = 'upper left')

plt.show()

for j in range (0, len(scripts)):
	sentimentCount[j] =  sentiment(plaintext(scripts[j]))


#print sentimentCount

