import re
import numpy.random as npr

class markovNode:
    def __init__(self,value):
        self.value = value
        self.edges = {}

class markovGraph:
    def __init__(self,fileName):
        self.nodes = {}

        # upon initialisation it uses the given file to create a graph
        self.convertFile(fileName)

    # main procedure used to convert a file into a graph
    def convertFile(self,fileName):

        # opens the text file and formats it correctly
        file = self.readFile(fileName)
        self.translateText(file)
        self.updateProbabilities()

    def readFile(self,fileName):
        # opens the text file and reads it
        with open(fileName,"r") as f:
            text = f.read()

        # formats the text given by splitting it based on words
        text = self.splitText(text)
        return(text)

    def splitText(self,text):

        # sets out the format for recognising words using regex
        wordFormat = r"(\W+)"

        # uses the format to split up the text
        parts = list(re.split(wordFormat,text))

        # block used to remove all of the empty strings in the list
        while "" in parts:
            parts.remove("")

        return(parts)

    # passes a pair of words at a time to translatePair
    def translateText(self,text):

        # goes through a shortened version of this list as it needs to grab pairs
        for count in range(len(text)-1):
            self.translatePair(text[count],text[count+1])

    # uses two words to create new connection in the graph
    def translatePair(self,word1,word2):

        # if the node for the first word already exists
        if(word1 in self.nodes.keys()):

            # it navigates to the node
            node = self.nodes[word1]
            nodeDict = node.edges

            # if the word already exists in the node's dictionary
            if(word2 in nodeDict.keys()):

                # it adds 1 to its frequency
                nodeDict[word2] += 1
            else:

                # otherwise it creates a new index with frequency 1
                nodeDict[word1] = 1

        else:
            # otherwise it creates a whole new node instance
            newNode = markovNode(word1)

            # assumes it doesn't have the second word already in its edges
            newNode.edges[word2] = 1

            # and adds the node instance to the dictionary of nodes
            self.nodes[word1] = newNode

    # edits all nodes to use probabilities instead of frequencies
    def updateProbabilities(self):
        for node in self.nodes.values():
            self.updateNode(node)

    # changes a single node to have probability instead of frequency
    def updateNode(self,node):
        D = node.edges
        total = sum(D.values())
        for K in D.keys():
            D[K] = round(D[K] / total,3)

    def getNodes(self):
        return(self.nodes)

    # the number of nodes in the graph represents the number of unique words in the text
    def noUniqueWords(self):
        return(len(self.nodes))

    def generateText(self,length):

        # this is commonly a character used before a new sentance
        startChar = ". "

        # finds the relevant node for the start character
        startNode = self.nodes[startChar]

    def chooseFrom(self,node):
        

newGraph = markovGraph("Input text")
newGraph.getNodes()
print(newGraph.noUniqueWords())


# allows for weighted choice on a list
# use npr.choice(values to pick, 1, p = probability distribution)[0]
