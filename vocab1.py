"""
Author: Novanator 2012
Program: Vocabulary1
"""

def exists(word, words):
	if word in words:
		return True
	else:
		return False
		
file = open("wordlist.txt", "r")
contents = file.read()
words = contents.split()

if file != "" :
	print ("The file was read!")

word = input("Your word: ")

if exists(word, words):
	print (word,"exists")
else:
        print (word,"does not exist")

#remaking words
w = input ("Another word: ")
start = int(input ("Choose a number of letters before the word:"))
end = int(input ("Choose a number of letters after the word:"))

def remake (start, end, w):
	begin=""
	middle=""
	begin+=w[:start-1]
	backword=w[::-1]
	caboose=backword[:end-1]
	middle+=w[start:end]
	
	return caboose+middle+begin

print()

file.close()

