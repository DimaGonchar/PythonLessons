import requests
import json
#display of exchange rates
resp=requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
listRates=json.loads(resp.text)
for iterator in listRates:
    print(type(iterator["base_ccy"]))
    print(iterator["base_ccy"]+"/"+iterator["ccy"]+":"+iterator["buy"]+"/"+iterator["sale"])

string="""Given a phrase, count the occurrences of each word in that phrase.

For the purposes of this exercise you can expect that a word will always be one of:

A number composed of one or more ASCII digits (ie "0" or "1234") OR
A simple word composed of one or more ASCII letters (ie "a" or "they") OR
A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
When counting words you can assume the following rules:

The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
The count is unordered; the tests will ignore how words and counts are ordered
Other than the apostrophe in a contraction all forms of punctuation are ignored
The words can be separated by any form of whitespace (ie "\t", "\n", " ")
For example, for the phrase "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.”"""

"""letters={}
for i in string.split():
    letters[i]=letters.get(i,0)+1
for i, count in letters.items():
    print(i,count)"""
#exeptions
"""try:    
 print("Enter matrix size:")
 size=input()
 if(not size.isnumeric()):
   raise Exception("no correct value")
 else:
    size=int(size) 

 import random
 matrix=[[0]*size for i in range(size)]
 for i in range(size):
   for j in range(size):
     matrix[i][j]=random.randint(0,100)
 print(matrix)    

 print("Enter two index matrix:")
 index1, index2 =input().split()
 if(not index1.isnumeric() or not index2.isnumeric()):
    raise Exception ("one of the values ​​is not a number")
 else:
  index1=int(index1)
  index2=int(index2)     
 if(index1>size or index2>size):
     raise Exception("out of matrix range")   

 print(matrix[index1][index2])

except Exception as e:
    print(e)"""





     

    





