
reserved = {
    'struct' :'STRUCT'
}

tokens = [
    'decimal',
    'binary',
    'hexadecimal',
    'S/M',
    'number_decimal',
    'number_binary',
    'number_hexadecimal',
    'number_S/M'
    'plus',
    'minus',
    'times',
    'divide'
] + list(reserved.values())

#Tokens

t_decimal        = r'\decimal'
t_binary         = r'\binary'
t_hexadecimal    = r'\hexadecimal'
t_S/M            = r'\S/M'
t_number_decimal = r'\d+'
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

def t_number_hexadecimal(t):
    r''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

#Build the lexer

import ply.lex as lex
lexer = lex.lex()

names = []
f = open('output.py','w')







