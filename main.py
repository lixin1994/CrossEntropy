from shannonGame import shannonGame

vocabulary = 'qwertyuiopasdfghjklzxcvbnm 1234567890'
smoothLambda = 0.1
fileName = 'afp1k.txt'
testList = ['he somehow made this analogy sound exciting instead of hopeless',
            'no living humans had skeletal features remotely like these',
            'frequent internet and social media users do not have higher stress levels',
            'the sand the two women were sweeping into their dustpans was transferred into plastic bags']

print 'Start'
print '-------------------------------------------------------------------------'
print 'Setting:'
newShannon = shannonGame(vocabulary, smoothLambda)
newShannon.readFile(fileName)
print '    Vocabulary:', newShannon.vocabulary
print '    Lambda:', newShannon.l
print '    Tranning Data:', fileName
print '-------------------------------------------------------------------------'
print 'Analyzing.....'
newShannon.startCounting()
newShannon.calculateProb()
print '-------------------------------------------------------------------------'
print 'Result:'
newShannon.analyseCrossEntropy(testList)
newShannon.analyseCrossEntropy(testList)
