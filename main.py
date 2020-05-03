# Erlina Rohmawati	    175150201111045
# Tania Malik Iryana	175150201111053
# Alvina Eka Damayanti	175150201111056
# Jeowandha Ria Wiyani	175150207111029

import time
import booleanFix as BRM

awal = time.time()  

# #membaca file korpus
corpus = open('C:/Users/Asus/Downloads/corpusg.txt','rt', encoding="utf-8")
readCorpus = corpus.read()
corpus.close()

corpusTanpaTag = BRM.cleaningTag(readCorpus)
corpusToken = BRM.cleaningTokenisasi(corpusTanpaTag)
corpusTanpaStopword = BRM.stopwordRemoval(corpusToken)

print(str(corpusTanpaStopword)+"\n")

# for corpus in corpusTanpaStopword:
#     print(str(corpus)+"\n")

terms = BRM.cariTerm(corpusTanpaStopword)
value,inMatrix = BRM.kemunculanKata(terms, corpusTanpaStopword) 

query = input("Masukan kata yang ingin dicari: ")
# query = "( ( full literary genius or beauty wound ) and family ) and not french"

postfixList = BRM.infixToPostfix(query, terms)
hasil = BRM.hasilPostfix(postfixList, corpusTanpaStopword, terms, inMatrix)

print("****************************************************************")
# print(query)
# print(postfixList)
# print(hasil)

hasil_str = ""
for i in range(len(hasil)):
    if hasil[i] == 1:
        hasil_str = hasil_str + '\n'+ '- Dokumen '+ str(i+1)

print("Document yang mengandung kata '" + str(query) + "' yaitu di: " + str(hasil_str))


akhir = time.time()
print("----------------------------------------------------------------")
print ("Total Waktu Proses " + str(akhir-awal) + " Detik." )