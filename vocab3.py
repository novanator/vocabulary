"""
Author: Novanator 2012
Program: Vocabulary2
"""

import time

# Binary search
def exists_bin(word, words):
	'''
	Function takes:
		word: a string you are looking for in the wordlist
		words: a list of strings that you are searching for
	Returns:
		True if word exists in words
		False if not
	'''
	l = 0 #left index
	r=len(words)-1 #right index
	while l <= r :
    		m=(l+r)//2
    		if word < words[m]:
        			r=m-1
    		elif word > words[m]:
        			l=m+1
    		else:
        			return True


def remake (w, start, end):
	'''
	The function takes the word the user adds and remakes it. The first parameter is the string word, the second is the number of letters in the beginning of the word, the third is the number of letters at the end of the word. These letters then switch places.
	'''
	end = len(w)-end 
	begin = w[:start] 
	caboose = w[end:] 
	middle = w[start:end]

	return caboose+middle+begin

# Open the file and see if it has content (words)
file = open ("wordlist.txt", "r")
contents = file.read ()

if contents:
	print ("The file was read!")
words = contents.split ()

word = input ("Your word: ")

if exists_bin(word, words):
       print (word,"exists")
else:
       print (word,"does not exist")

original_words, cropped_words = [], []

for x in words:
	cropped_word = remake(x,2,3)
	if cropped_word in words:
		original_words.append(x)
		cropped_words.append(cropped_word)

a = ' '.join(original_words)
b = ' '.join(cropped_words)
print (a, '\n', b)

start = time.clock()
for i in range(100000):
    exists_bin(word, words)
end = time.clock()
print (end-start)

file.close()
