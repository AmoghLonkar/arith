#Referenced 'https://ruslanspivak.com/lsbasi-part1/'
#Referenced 'https://ruslanspivak.com/lsbasi-part7/'

#Token Class
#Token has type and value
#Token types: integer, add, sub, mul
class Token:

    #Token "constructor"
    def __init__(self, type,value):
        self.type = type
        self.value = value

    #Display string for debugging
    def printToken(self):
          print(Token({type}, {value}).format(type=self.type, value=repr(self.value)))

#Lexer Class
#Lexer reads input string and splits into tokens
class Lexer:

    #Lexer "constructor"
    def __init__(self, expression):
        self.expression = self
        self.index = 0
        self.current = self.expression[self.index]
        print(type(self.current))

    def __getitem__(self, index):
        return self.index
    
    #To help in iterating through expression
    def nextChar(self):
        self.index += 1

        if(self.index) > len(self.expression):
            self.current = 'None'
        else:
            self.current = self.expression[self.index]
        print(type(self.current))

    #Accounting for multi-digit operands
    def intVal(self):
        operand = ''
        while self.current.isdigit() and self.current is not None:
            operand += self.current
            self.nextChar()

        return int(operand)
    
    #Iterating through expression and converting into tokens
    def exprToToken(self):
        while self.current is not None:

            if self.current.isdigit():
                temp = Token('Integer', self.intVal())
                temp.printToken()
                return Token('Integer', self.intVal())
            elif self.current == '+':
                temp = Token('Add', self.current)
                temp.printToken()
                return Token('Add', self.current)
            elif self.current == '-':
                temp = Token('Sub', self.current)
                temp.printToken()
                return Token('Sub', self.current)
            elif self.current == '*':
                temp = Token('Mul', self.current)
                temp.printToken()
                return Token('Mul', self.current)
            
            #Removing white spaces
            elif self.current.isspace():
                self.nextChar

        temp = Token('EOF', None)
        temp.printToken()
        return Token('EOF', None)    

def main():
    while True:
        expression = raw_input("")
        string = Lexer(expression)
        token = string.exprToToken()

if __name__ == "__main__":
    main()

