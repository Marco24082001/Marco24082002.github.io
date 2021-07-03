import load_dict as ld
import pandas as pd
import math

file_path = "./dataset/csv/khoa_hoc.csv"

# suppose a sentence = a doc
# vectorize sentences

# wordDicts = []
idfDict = {}
def set_wordDicts(docList):
    global wordDicts
    for sen in ld.SENTENCE_LIST:
        wordDict = dict.fromkeys(ld.WORD_SET,0)
        for word in sen:
            if word in ld.WORD_SET:
                wordDict[word] += 1
        wordDicts.append(wordDict)


    
def computeTF(wordDict, words):
    tfDict = {}
    wordsCount = len(words)
    for word, count in wordDict.items():
        tfDict[word] = count/float(wordsCount)
    return tfDict

def computeIDF(wordDict, docList):
    global idfDict
    if not idfDict:
        N = len(docList)
        idfDict = dict.fromkeys(ld.WORD_SET, 0)
        for doc in docList:
            words = set(doc.split(' '))
            for word in ld.WORD_SET:
                if word in words:
                    idfDict[word] += 1
        for word, val in idfDict.items():
                idfDict[word] = math.log10(N / float(val))
    return idfDict

def computeTFIDF(tfDocs, idfs):
    tfidf = {}
    for word, val in tfDocs.items():
        tfidf[word] = val*idfs[word]
    return tfidf

def vectorize_sen(sentence, docList):
    wordDict = dict.fromkeys(ld.WORD_SET,0)
    words = sentence.split(' ')
    for word in words:
        if word in ld.WORD_SET:
            wordDict[word] += 1
    return computeTFIDF(computeTF(wordDict, words), computeIDF(wordDict, docList))

if __name__ == '__main__':
    df = pd.read_csv(file_path)
    data = df.values[:, 1]
    data = ld.preprocess_dataframe(data)
    # tfidfDocA = vectorize_sen(ld.SENTENCE_LIST[0], ld.SENTENCE_LIST)
    # df = pd.DataFrame([tfidfDocA])
    # print(df)
    vectorize = []
    for i in range(10):
        vectorize.append(vectorize_sen(ld.SENTENCE_LIST[i], ld.SENTENCE_LIST))
    df = pd.DataFrame(vectorize)
    print(df)
    