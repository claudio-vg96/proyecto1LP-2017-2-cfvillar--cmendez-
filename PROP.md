Lenguaje que tiene como objetivo realizar la operacion entregada por el usuario (en decimal,
binario, hexadecimal o S/M), y el resultado entregarlo en una tabla, en decimal,
 binario, complemento 2, hexadecimal y S/M

statement ::= type number1 operation type number2

type ::= 'decimal' | 'binary' | 'hexadecimal' | 'S/M'

number1 ::= decimal | binary | hexadecimal | S/M

decimal ::= '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'

binary ::= '0'|'1'

hexadecimal ::= '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'|'A'|'B'|'C'|'D'|'E'|'F'

S/M ::= '0'|'1'

operation ::= '+'|'-'|'*'|'/'

number2 ::= decimal | binary | hexadecimal | S/M


