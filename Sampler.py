from Creator import markovGraph
import os
import pickle

check = os.path.exists('store.pickle')

if(check):
    print("previous file found")
    with open("store.pickle","rb") as f:
        m = pickle.load(f)
    print("file loaded")
else:
    print("no previous file")
    m = markovGraph("Input text")
    with open("store.pickle","wb") as f:
        pickle.dump(m,f)
    print("stored")

print(m.generateText(5))
