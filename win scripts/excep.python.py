#_*_coding:utf-8_*_

class schoolmember:
    def __init__(self,name,gender,nationality='CN'):
        self.name = name
        self.gender = gender
        self.nation = nationality
    def tell(self):
        print 'hi,my name is %s,i am from %s' %(self.name,self.nation)

class student(schoolmember):
    def __init__(self,Name,Gender,Class,Score,Nation='US'):
        schoolmember.__init__(self,Name,Gender,Nation)
        self.Class = Class
        self.Score = Score

    def paytuition(self,amount):
        if amount < 6499 :
            print 'get fuck off...'
        else:
            print'Welcom onboard'
class teacher(schoolmember):
    def __init__(self,Name,Gender,Course,Salary,Nation):
        schoolmember.__init__(self,Name,Gender,Nation)
        self.Course = Course
        self.Salary = Salary

    def teaching(self):
        print 'i am teaching %s, i am making %s per month' %(self.Course,self.Salary)


S1 = student('rita','male','python','C+','JP')
S1.tell()
S1.paytuition(5000)

S2 = student('hehe','female','linux','C+')
S2.tell()
S2.paytuition(7000)


T1=teacher('alex','male','Python','5000','CN')
T1.tell()
T1.teaching()

