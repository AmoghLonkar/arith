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
        self.expression = expression
        self.index = 0
        self.current = self.expression[self.index]

    def __getitem__(self, index):
        return self.index

    #To help in iterating through expression
    def nextChar(self):
        self.index += 1

        if(self.index) > len(self.expression):
            self.current = 'None'
        else:
            self.current = self.expression[self.index]

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
                return Token('Integer', self.intVal())
            elif self.current == '+':
                return Token('Add', self.current)
            elif self.current == '-':
                return Token('Sub', self.current)
            elif self.current == '*':
                return Token('Mul', self.current)

            #Removing white spaces
            elif self.current.isspace():
                self.nextChar()

        return Token('EOF', None)

class BinOP(object):
    def __init__(self, left, op, right):
        self.left = left
        self.token = op
        self.right = right

class Num(object):
    def __init__(self, token):
        self.token = token
        self.value = token.value


#Parser Class
#Parser reads procssed input string and builds an AST
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.exprToToken()

    # For terms not in our language
    def error(self):
        raise Exception('Invalid syntax')

    def verifyType(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.exprToToken()
        else:
            self.error()

    def factor(self):
        """factor grammar: INTEGER"""
        token = self.current_token
        if token.type == 'Integer':
            self.verifyType(token)
            return Num(token)

    def term(self):
        node = self.factor()# get left term

        while self.current_token.type in ('Mul', 'Div'):
            token = self.current_token #move to next tokens
            if token.type == 'Mul':
                self.verifyType('Mul')
            elif token.type == 'Div':
                self.verifyType('Div')

            node = BinOP(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in ('Plus','Minus'):
            token = self.current_token
            if token.type == 'Plus':
                self.verifyType('Plus')
            elif token.type == 'Minus':
                self.verifyType('Minus')

            node = BinOP(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

# Interpreter
# Converts AST into evaluated expression.
class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        if node.op.type == 'Plus':
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == 'Minus':
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == 'Mul':
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == 'Div':
            return self.visit(node.left) // self.visit(node.right)

    def visit_Num(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

def main():
    while True:
        expression = raw_input("")
        tokens = Lexer(expression)
        parser = Parser(tokens)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)

if __name__ == "__main__":
    main()
