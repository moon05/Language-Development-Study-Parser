import os
import nltk
from collections import Counter

def readFile(filepath):
	if not os.path.exists(filepath):
		return "Incorrect filepath"
	foo = open(filepath,"r")
	print "Name of file: " + filepath
	sentenceCount = 0
	sentences = list()	
	while True:
		line = foo.readline()		
		if "#####" in line:
			break		
		if line.startswith('Dominic'):
			sentenceCount = sentenceCount + 1
			newSentence = line.lstrip("Dominic: ").rstrip("\n").replace("\xe2\x80\x99","'").lower()
			sentences.append(newSentence)

	return sentenceCount, sentences

def wordCount(sentenceList):
	totalWords = 0
	unknown = 0
	for n in sentenceList:
		temp = n.split()
		if "[...]" in temp:
			occur = temp.count("[...]")
			unknown = unknown + occur
		totalWords = totalWords + len(temp)
	return totalWords, unknown

def partsCount(sentenceList):
	verbs = 0
	nouns = 0
	adjectives = 0
	conjunctions = 0
	determiners = 0
	adverbs = 0
	pronouns = 0
	numerals = 0
	for n in sentenceList:
		tokens = nltk.word_tokenize(n)
		tagged = nltk.pos_tag(tokens)
		counts = Counter(tag for word, tag in tagged)
		if "CC" in counts:
			conjunctions = conjunctions + counts["CC"]
		if "DT" in counts:
			determiners = determiners + counts["DT"]
		if "JJ" in counts:
			adjectives = adjectives + counts["JJ"]
		if "JJR" in counts:
			adjectives = adjectives + counts["JJR"]
		if "JJS" in counts:
			adjectives = adjectives + counts["JJS"]
		if "NN" in counts:
			nouns = nouns + counts["NN"]
		if "NNP" in counts:
			nouns = nouns + counts["NNP"]
		if "NN" or "NNP" or "NNPS" or "NNS" in counts:
			nouns = nouns + counts["NNPS"]
		if "NNS" in counts:
			nouns = nouns + counts["NNS"]
		if "RB" in counts:
			adverbs = adverbs + counts["RB"]
		if "RBR" in counts:
			adverbs = adverbs + counts["RBR"]
		if "RBS" in counts:
			adverbs = adverbs + counts["RBS"]
		if "WRB" in counts:
			pronouns = pronouns + counts["WRB"]
		if "VB" in counts:
			verbs = verbs + counts["VB"]
		if "VBD" in counts:
			verbs = verbs + counts["VBD"]
		if "VBG" in counts:
			verbs = verbs + counts["VBG"]
		if "VBN" in counts:
			verbs = verbs + counts["VBN"]
		if "VBZ" in counts:
			verbs = verbs + counts["VBZ"]
		if "PRP" in counts:
			pronouns = pronouns + counts["PRP"]
		if "PRP$" in counts:
			pronouns = pronouns + counts["PRP$"]
		if "WP" in counts:
			pronouns = pronouns + counts["WP"]
		if "WP$" in counts:
			pronouns = pronouns + counts["WP$"]
		if "CD" in counts:
			numerals = numerals + counts["CD"]
	total = pronouns + numerals + verbs + nouns + adjectives \
			+ adverbs + conjunctions + determiners
	return ("pronouns %d, numerals %d, verbs %d, nouns %d, adjectives %d, adverbs %d, conjunctions %d, determiner %d, TOTAL %d" % \
			(pronouns, numerals, verbs, nouns, adjectives, adverbs, conjunctions, determiners, total))


sentenceCount, sentences = readFile("./Kyle's video subtitle.txt")
total, unknown = wordCount(sentences)
speech = partsCount(sentences)
a = int(speech[-3:])
print "The total number of sentences is: " + str(len(sentences))
print "The total word count is: " + str(total)
print "Number of words that couldn't be understood: " + str(unknown)
print "Number of filler words: " + str(total - unknown - a)
print speech
