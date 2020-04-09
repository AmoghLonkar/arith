# arith
The code contains an interpreter for the language arith coded in Python version 3.6. The algorithm is split into a Lexer, a Parser and an Evaluator. The lexer divides the input expression(type string) into Tokens. The Parser then takes these tokens and converts them into an Abstract Syntax Tree, a binary tree which maintains the precedence of operations. The Evaluator then traverses this tree and computes the result.

## How to Run 
make  
./arith  
expression  

## Running the tests
Do ./test.sh

## References
https://ruslanspivak.com/lsbasi-part1/  
https://ruslanspivak.com/lsbasi-part7/ 

