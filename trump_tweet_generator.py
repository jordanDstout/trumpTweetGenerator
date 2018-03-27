import csv
import nltk
import random

#remember how ugly it is taking stuff from the csv file?
#ya this deals with that...ish. Still a lot of leftover unicode that doesnt
#look good but thats a problem for future Jordan
def getTokens(tweet):
    mylist = tweet.split(',')
    wordList = []
    for possibleWord in mylist:
        if not any(c.isdigit() for c in possibleWord) and '/' not in possibleWord:
            wordList = wordList + [possibleWord]
    return " ".join(wordList)


#N is the N in N-grams. Unigrams ==1, Bi==2,Tri==3 so on.
def generateNgrams(N, tokens):

    #lol this function
    def generateUnigrams():
        unigramDict = {}
        numTokens = len(tokens)

        for token in tokens:
            if token in unigramDict.keys() and token != '*':
                unigramDict[token] = unigramDict[token] + 1
            elif token != '*':
                unigramDict[token] = 1

        for key in unigramDict.keys():
            unigramDict[key] = unigramDict[key]/float(numTokens)

        return unigramDict


    def generateBigrams():
        numTokens = len(tokens)
        bigramDict = {}
        acc = 0
        while acc < len(tokens)-1:
            token1 = tokens[acc]
            token2 = tokens[acc+1]

            if token1 == '*':
                acc += 1
                continue
            if token2 == '*':
                acc += 2
                continue

            if token1 in bigramDict.keys():
                if token2 in bigramDict[token1].keys():
                    bigramDict[token1][token2] += 1

                else:
                    bigramDict[token1][token2] = 1
            else:
                bigramDict[token1] = {token2 : 1}


            acc +=1

        for key in bigramDict.keys():
            for key2 in bigramDict[key].keys():
                bigramDict[key][key2] = bigramDict[key][key2]/float(len(bigramDict[key]))

        return bigramDict




    #placeholder for trigram function. goal is to get to 5-grams.
    def generateTrigrams():
        return

    if N == 1:
        return generateUnigrams()
    if N == 2:
        return generateBigrams()




#brute force right now. not a huge deal but theres better ways
def generateSeedWords(seedWords):
    seedDict = {}
    numTokens = len(seedWords)
    for word in seedWords:
        if word in seedDict.keys():
            seedDict[word] += 1

        else:
            seedDict[word] = 1 
            
    for key in seedDict.keys():
        seedDict[key] = seedDict[key]/float(numTokens)


    return seedDict

#included N so that I can make different functions for generating unigram sentence
#vs making a trigram sentence and such
def generateSentence(seedDict, N, sequenceDict):
    return


def main():
    reader = csv.reader(open('@realDonaldTrump_tweets.csv',), delimiter = ' ', quotechar = '|')

    accTokens = []
    accSeedTokens = []

    counter = 0
    for row in reader:
        counter+=1
        if counter >50:
            break
        x=', '.join(row)
        sentence = getTokens(x)
        sentence=sentence.decode('utf-8')

        tokens = nltk.word_tokenize(sentence)
        if tokens != []:
            accSeedTokens += tokens[0]
            accTokens += tokens[1:]
            accTokens += "*"
    #print len(generateNgrams(2, accTokens))
    #print len(generateSeedWords(accSeedTokens))
    print generateNgrams(2,accTokens)
main()



