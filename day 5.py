
def AlphaNumeric(option):
    if option == "num":
        print("0123456789")
    else:
        print("the alphabet")

def makerect(w,h,x,y):
    Width = w
    hieght = h
    x = x
    y = y
    color = getRandomColor();
    print "made rectangle"
    return (Width, hieght, x , y, color)

def getRandomColor():
    return "blue"

class Student():

    def __init__(self, n,a,g):
        self.name = n
        self.age = a
        self.grade = g

    def promoteGrade(self):
        self.grade = self.grade + 1

    def changeName(self, newName):
        self.name = newName

olly = Student("olly",12,7)
print olly.name

olly.promoteGrade()
print olly.grade

olly.promoteGrade()
print olly.grade

olly.changeName("Obama")
print olly.name