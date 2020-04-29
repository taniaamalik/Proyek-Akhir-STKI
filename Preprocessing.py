# Erlina Rohmawati	    175150201111045
# Tania Malik Iryana	175150201111053
# Alvina Eka Damayanti	175150201111056
# Jeowandha Ria Wiyani	175150207111029

import re, time
import matplotlib.pyplot as plt
import pandas as pd

awal = time.time()  
################proses cleaning, tokenization, case folding###############################
def cleaningTag(readCorpus) :
    #membersihkan tag
    regex = r"(<\w{3,}>|</\w{3,}>)|((<(/?)\w+>)(.?)+)"
    corpusTanpaTag = re.sub(regex,"",readCorpus)
    return corpusTanpaTag

def cleaningPunc(corpusTanpaTag) :
    #membersihkan tanda baca
    corpusBersih = re.sub(r"[^a-zA-Z]", " ", corpusTanpaTag)
    return corpusBersih

def tokenisasi(corpus): #melakukan tokenisasi
    corpusToken = re.split(r"[\s]+", corpus)
    corpusToken.remove("")
    corpusToken.remove("")
    return corpusToken

def caseFold(corpusToken) :
    for indexCorpus in range(0, len(corpusToken)) :
        corpusToken[indexCorpus] = corpusToken[indexCorpus].lower()
    return corpusToken

########################proses menghilangkan stopword############################
def stopwordRemoval(corpusToken) :
    stopwordTeks = open('E:/College/Project/6th Semester/Information Retrieval/Projek Akhir/Stopword.txt', 'r')
    stopwordRead = stopwordTeks.read().split('\n')
    stopwordTeks.close()

    for kata in stopwordRead :
        for word in corpusToken :
            if kata == word :
                corpusToken.remove(word)

    return corpusToken

# #######################################################################################

#membaca file korpus
corpus = open('E:/College/Project/6th Semester/Information Retrieval/Projek Akhir/corpusgoodread.txt', 'rt', encoding="ANSI")
readCorpus = corpus.read()
corpus.close()

corpusTanpaTag = cleaningTag(readCorpus)
corpusCleaning = cleaningPunc(corpusTanpaTag)
corpusToken = tokenisasi(corpusCleaning)
corpusKecil = caseFold(corpusToken)
corpusTanpaStopword = stopwordRemoval(corpusKecil)

for token in corpusTanpaStopword :
    print(str(token))

pd.DataFrame(corpusTanpaStopword).to_excel('output.xlsx', header=False, index=False)