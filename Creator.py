import re
import numpy.random as npr

class markovNode:
    def __init__(self,value):
        self.value = value
        self.edges = {}

class markovGraph:
    def __init__(self,fileName):
        self.nodes = {}
        self.convertFile(fileName)

    def readFile(self,fileName):
        with open(fileName,"r") as f:
            text = f.read()
        text = self.splitText(text)
        return(text)

    def splitText(self,text):
        wordFormat = r"(\W+)"
        parts = list(re.split(wordFormat,text))
        while "" in parts:
            parts.remove("")
        return(parts)

    def convertFile(self,fileName):
        file = self.readFile(fileName)
        self.translateText(file)
        self.updateProbabilities()

    def translateText(self,text):
        for count in range(len(text)-1):
            self.translatePair(text[count],text[count+1])

    def translatePair(self,word1,word2):
        if(word1 in self.nodes.keys()):
            node = self.nodes[word1]
            nodeDict = node.edges
            if(word2 in nodeDict.keys()):
                nodeDict[word2] += 1
            else:
                nodeDict[word1] = 1
        else:
            newNode = markovNode(word1)
            newNode.edges[word2] = 1
            self.nodes[word1] = newNode

    def updateProbabilities(self):
        for node in self.nodes.values():
            self.updateNode(node)

    def updateNode(self,node):
        D = node.edges
        total = sum(D.values())
        for K in D.keys():
            D[K] = round(D[K] / total,3)

    def getNodes(self):
        return(self.nodes)

    def noUniqueWords(self):
        return(len(self.nodes))

    def generateText(self,length):


newGraph = markovGraph("Input text")
newGraph.getNodes()
print(newGraph.noUniqueWords())


# allows for weighted choice on a list
# use npr.choice(values to pick, 1, p = probability distribution)[0]
