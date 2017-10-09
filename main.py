from stdlib import *
import ply.lex as lex

reserved = {
    'struct' : 'STRUCT'
}

tokens = [
    'number_decimal',
    'number_binary',
    'number_hexadecimal',
    'number_sm',
    'decimal',
    'binary',
    'hexadecimal',
    'sm',
    'plus',
    'minus',
    'times',
    'divide'
] + list(reserved.values())

#Tokens

t_decimal        = r'decimal'
t_binary         = r'binary'
t_hexadecimal    = r'hexadecimal'
t_sm             = r'sm'
t_plus           = r'\+'
t_minus          = r'-'
t_times          = r'\*'
t_divide         = r'/'

#Ignored characters
t_ignore = " \t"

def t_number_binary(t):
    r'(0|1)+'
    t.type = reserved.get(t.value, 'number_decimal')
    return t

def t_number_decimal(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_number_hexadecimal(t):
    r'[0-9ABCDEF]+'
    t.type = reserved.get(t.value,'number_hexadecimal')
    return t

def t_number_sm (t):
    r'(0|1)+'
    t.type = reserved.get(t.value, 'number_sm')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    # Build the lexer
    lexer = lex.lex()

    #Test Input

    #decimal + decimal
    data = '''
    decimal 10 + binary 10100'''

    #hexadecimal + decimal
    data2 = '''
    1010 + B3C1'''


    #Give the lexer some input
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

