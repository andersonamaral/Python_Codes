'''
   Question:

getString: obtain o string
printString: imprime o string em uppercase


 __init__ method : constroi parametros
'''
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
