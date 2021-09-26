from _typeshed import Self


class Person():
    def __init__(self):
        pass

    def setName(self,name):
        self.name=name

    def setDataOfBirth(self,dataOfBirth):
        self.dataOfBirth=dataOfBirth
    
    def getName(self):
        return  self.name
    
    def getDataOfBirth(self):
        return self.dataOfBirth


class Employer(Person):
    super.__init__()
    
    def setName(self,name):
         self.name=name

    def setDataOfBirth(self,dataOfBirth):
        self.dataOfBirth=dataOfBirth  
    
    def setSalary(self,salary):
        self.salary=salary

    def setProfession(self,profession):
        self.profession=profession  


    def getSalary(self):
        return self.salary
    
    def getProfession(self):
        return self.profession 


class Castomer(Person):
    def __init__(self):
         super().__init__() 

    def setEmail(self,email):
        self.email=email   

    def getEmail(self):
        return self.email      







      




