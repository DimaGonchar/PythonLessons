"""def writeToFile(file,txt):
 with open(file+".txt",'w') as fileWrite:
     fileWrite.write(txt)

print("Enter file name:")
fileName=input()
print("Enter text:")
text=input()

writeToFile(fileName,text)"""

class Cat:
  def __init__(self) -> None:
      self.name=None
      self.color=None
      self.weight=None
  def meow(self):
      print("meow", self.name, self.color,self.weight)

cat=Cat()  
cat.name="barsik"
cat.color="Red"
cat.weight="50"
cat.meow()



