"""
Author: Novanator 2012
Program: Vocabulary2
"""

import time

def remake (w, start, end):
	
	end = len(w)-end 
	begin = w[:start] 
	caboose = w[end:] 
	middle = w[start:end]

	return caboose+middle+begin

#binary search
def exists_bin(word, words):
	l = 0
	r=len(words)-1
	while l <= r :
    		m=(l+r)//2
    		if word < words[m]:
        		r=m-1
    		elif word > words[m]:
        		l=m+1
    		else:
        		return True	
	
file = open("wordlist.txt", "r")
contents = file.read()
words = contents.split()

if file != "" :
	print ("The file was read!")

word = input("Your word: ")

if exists_bin(word, words):

	print (word,"exists")
else:
        print (word,"does not exist")

a="" 
b="" 
for x in words: 
    if x[::-1] in words: 
        a+=x+" " 
        b+=x[::-1]+ " "

def split_list(listan):
    half = len(listan)//2
    return listan[:half]

c = split_list(a)
d = split_list(b)
 
print(" "+c,"\n",d)

start = time.clock()
for i in range(100000):
    exists_bin(word, words)
end = time.clock()
time = (end-start)

print (time)

file.close()
