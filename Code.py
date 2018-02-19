import collections

file_1=open('98-0.txt')
file_1_read=file_1.read().lower().split()
#print("file_1_read=",file_1_read)

stopwords = set(line.strip() for line in open('stopwords'))
print("stopwords=",stopwords)
# create your data structure here.  F
wordcount={}

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

for word in file_1_read:
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.
#class collections.Counter([iterable-or-mapping])
#A Counter is a dict subclass for counting hashable objects. 
#It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
#Counts are allowed to be any integer value including zero or negative counts. 
#The Counter class is similar to bags or multisets in other languages.
d = collections.Counter(wordcount)

print(d.most_common(10))
#most_common([n])Return a list of the n most common elements and their counts from the most common to the least.
#If n is omitted or None, most_common() returns all elements in the counter. 
#Elements with equal counts are ordered arbitrarily:
#If you used an unordered data structure like a dictionary, you might need get the values out of it (into a list) to sort it.  
#You could also use "collections.Counter" to help with this step.
for word, count in d.most_common(10):
	print(word, ": ", count)
