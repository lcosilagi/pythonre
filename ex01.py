#!/usr/bin/env python3

import re

id = '''
Homer Cage
Homer Scorpion
Homer Simpson
Homer Flanders
'''

'''
Expressão regular que pesquisa e retorna todos os nomes na string id 
com o nome Homer seguido pelo sobrenome Simpson.
a re (?=) é conhecida como positive lookahead
'''

exemplo = re.findall(r'Homer(?=\sSimpson).*',id)

print('Nossa string contem os seguintes ids:')
print(id)

''' Loop for para imprimir cada elemento da lista exemplo '''
print('Aplicado re para achar somente o nome Homer seguido pelo sobrenome Simpson:')
print('Positive Lookahead: re.findall\(r\'Homer(?=\sSimpson).*\',id\'\)\n')
tam = len(exemplo)

for m in exemplo:
    print(m)

print(f"\n{tam} elemento encontrado")

