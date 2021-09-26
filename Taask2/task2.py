def parityCheck(number):
    if number%2==0:
       return  "Number is even"
    else:
       return "Number is add"  

def findWord(word):
    count=0
   # char =" "
    for i in range(len(word)):
        if word[i]==" " :
            count+=1
        if count>1 and count<3:
            print(word[i])

findWord("He was surprised that his immense laziness was inspirational to others")
            
           



