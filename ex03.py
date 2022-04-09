#!/usr/bin/env python3

import re

id = '''
Ned Simpson
Ned Flanders
Homer Simpson
Homer Flanders
Bart Simpson
Bart Flanders
'''

'''
Expressão regular que pesquisa e retorna somente o sobrenome na string id 
Simpson seguido do nome Homer e armazena o resultado em um objeto lista.
a re (?>=) é conhecido como Positive lookbehind
'''

exemplo = re.findall(r'.*(?<=Homer\s)Simpson',id)

print('Nossa string contem os seguintes ids:')
print(id)

''' Loop for para imprimir cada elemento da lista exemplo '''
print('Aplicado re para achar somente o nome Homer que precede o sobrenome Simpson:')
print('Positive Lookbehind: re.findall(r\'.*\(?<=Homer\s\)Simpson\',id)\n')
tam = len(exemplo)

for m in exemplo:
    print(m)

print(f"\n{tam} elementos encontrados")

