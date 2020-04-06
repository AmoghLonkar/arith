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

#Lexer Class
#Lexer reads input string and splits into tokens
#class Lexer:

    #Lexer "constructor"
    def __init__(self, expression):
        self.expression = self
        self.index = 0
        self.current = self.expression[index]

    def nextChar(self):
        self.index += 1

        if(self.index) > len(self.expression):
            self.current = 'None'
        else
            self.current = self.expression[index]
    
    def removeSpace(self):
        while self.current is not None and self.current.isspace():
            self.nextChar

    def multipleDigits(self):
        operand = ''
        while self.current.isdigit() and self.current is not None:
            operand += self.current
            self.nextChar

        return int(operand)


def main():
    while True:
        expression = raw_input("")

if __name__ == "__main__":
    main()




