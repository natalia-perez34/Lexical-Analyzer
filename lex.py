# Created by: Natalia Perez Montalvo
# 09-17-2024

from ply import lex

# Tokens. Keywords start from 'IF' to 'WRITE', Delimiters start from 'LPAREN' to 'COMMA' and Operators start from 'EQUALS' to 'MOD'.

tokens = ('IDENTIFIER', 'NUMBER', 'IF', 'ELSE', 'WHILE', 'LET', 'LOOP', 'FN', 'MUT', 'PUB', 'REF', 'IN', 'STRUCT', 'TYPE', 'RETURN'
          , 'TRUE', 'FALSE', 'WHERE', 'WRITE', 'LPAREN', 'RPAREN', 'LCURLY', 'RCURLY', 'LSQR', 'RSQR', 'SEMICOLON', 'COMMA',
          'EQUALS', 'NEQ', 'LEQ', 'GEQ', 'LT', 'GT', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'MOD')

# In this Lexical Analyzer, whitespace and comments are irrelevant to the syntactic specification, therefore, they will be ignored.

# Ignore the whitespaces, which are tab '\t', newline '\n', return '\r' and space ' '.

t_ignore = ' \t\r\n'


# Regular Expresions for each token

# IDENTIFIER: A string beginning with at least one or more consecutive letters (a to z or A to Z) 
# Or underscores in a given string followed by letters (a to z or A to Z) or underscores or digits (0 to 9)

# IDENTIFIER token with keyword check
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Check if identifier is a keyword, like IF ELSE. 
    return t

# NUMBER: : a string consisting of one or more consecutive digits in the range 0-9. We want to convert this string to an integer

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Ignore comments

def t_COMMENT(t):
    r'//.*\n'
    pass

# Tokens, Create MAP to associate 'IF'='if', bcs every token down here is being classified as a IDENTIFIER
keywords = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'let': 'LET', 'loop': 'LOOP', 'fn': 'FN',
    'mut': 'MUT', 'pub': 'PUB', 'ref': 'REF', 'in': 'IN', 'struct': 'STRUCT', 'type': 'TYPE',
    'return': 'RETURN', 'true': 'TRUE', 'false': 'FALSE', 'where': 'WHERE', 'write': 'WRITE'
}

# Delimiters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LSQR = r'\['
t_RSQR = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

# Operators
t_EQUALS = r'='
t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_LT = r'<'
t_GT = r'>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_MOD = r'%'

# Error Handiling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' on line {t.lineno}")
    t.lexer.skip(1)

# Lexer creation
lexer = lex.lex()

# Function to read and process the test file
def process_test_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    
    # Tokenize the input from the file
    lexer.input(data)
    
    # Print tokens
    for tok in lexer:
        print(tok)

# Path to the test file
test_file_path = 'C:/Users/andad/OneDrive/Desktop/Programming Languages/Lexical Analyzer/Program_Test.txt'

# Process the test file
process_test_file(test_file_path)
