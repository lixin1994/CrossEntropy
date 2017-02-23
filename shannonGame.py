import re, string
import itertools
import math

class shannonGame:
    def __init__(self, vocabulary, l):
        self.content = ''
        self.counter = dict()
        self.probability = dict()
        self.vocabulary = vocabulary
        self.l = l
        self.initialCounter()

    '''
    This function is to initial the counter
    The counter will be structured like this:
    |'a': | 'ab': 0
    |     | 'bc': 1
    |     | 'cd': 2
    |     | 'aa': 5
    |     | ...
    |'b': | 'cd': 4
    |     | 'sv': 1
    |...  | ...
    '''

    def initialCounter(self):
        allCombines = list()
        for c in self.vocabulary:
            for d in self.vocabulary:
                allCombines.append(c+d)
        for c in allCombines:
            self.counter[c] = dict()
        for p in self.counter:
            for c in self.vocabulary:
                self.counter[p][c] = 0.0


    '''
    read the file and extract the useful characters
    '''
    def readFile(self, file):
        trainFile = open('afp1k.txt', 'r')
        lines = trainFile.readlines()
        content = ''
        for i in lines[0::]:
            content = content + i
        self.content = re.sub(r'[^\w\s]', '',content).lower().replace(' \n', ' ').replace('\n', ' ')
        # using redular expression to do extraction

    '''
    Counting the characters and the combinations of the characters.
    '''
    def startCounting(self):
        for i in range(2, len(self.content)):
            self.counter[self.content[(i-2):i]][self.content[i]] += 1.0

    '''
    Using lambda-smoothing to calculate the conditional probabilities:
    P = (C(x1,x2,x3) + lambda * v)/C(x2,x3) + v)
    '''
    def calculateProb(self):
        def calculateOneProb(dct, v, l = 0.1):
            result = dict()
            total = sum(dct.values())

            for d in dct:
                result[d] = (dct[d] + self.l)/(total + self.l * len(self.vocabulary))
                # using the lambda-smoothing!
            return result

        for p in self.counter:
            self.probability[p] = calculateOneProb(self.counter[p], len(self.vocabulary))

    '''
    Analyzing the crossEntropy using
    H = -sum(log(P[0...i]))/N
    '''
    def analyseCrossEntropy(self, lines):
        for words in lines:
            N = len(words) - 2
            H = 0.0
            for i in range(2, len(words)):
                H += math.log(self.probability[words[(i-2):i]][words[i]], 2)
            crossEntropy = -H/N


            print '    Text:', '"' + words + '"'
            print '    Cross Entropy:', crossEntropy
            print '-------------------------------------------------------------'
