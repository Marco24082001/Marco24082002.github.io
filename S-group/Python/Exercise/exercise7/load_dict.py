import os
import pandas as pd
file_path = "./dataset/csv/khoa_hoc.csv"
special_chars = """' … " + - _ . ’ , ; & : “ ” • [ ] { } ? ( ) ~ @ # $ % ^ * < > / \\ !  0 1 2 3 4 5 6 7 8 9"""
special_chars = special_chars.split()

VOCAB = dict()
WORD_SET = set()
SENTENCE_LIST = []
NUM_SENTENCE = 0
NUM_WORD = 0

def preprocess_dataframe(text_arr):
    processed_data = []
    for row in text_arr:
        preprocess_row(row)
    return processed_data

def preprocess_row(text):
    text = str(text).split('\n')
    data = [para.replace('\r', '').split('.') for para in text]
    #--> sentences of row
    
    for sen in data:
        if sen != '':
            preprocess_sentence(sen)
        

def preprocess_sentence(text):
    global VOCAB
    global SENTENCE_LIST
    global WORD_SET
    global NUM_SENTENCE

    NUM_SENTENCE += 1
    text = str(text).strip().lower()
    
    for c in special_chars:
        if c in text:
            text = text.replace(c, '') 
    
    SENTENCE_LIST.append(text)
    list_words = text.split(' ')

    for word in list_words:
        WORD_SET.add(word)
        if word in VOCAB:
            VOCAB[word] += 1
        else:
            VOCAB[word] = 1 

if __name__ == "__main__":
    print("special_chars : ", special_chars)
    df = pd.read_csv(file_path)
    data = df.values[:,1]
    data = preprocess_dataframe(data)
    print(VOCAB)
    
