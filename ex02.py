#!/usr/bin/env python3

import re

id = '''
Homer Van Damme
Homer Simpson
Homer Stallone
Homer Willys
Homer Pacino
'''

'''
Expressão regular que pesquisa e retorna somente o nome na string id 
Homer seguido de qualquer sobrenome diferente de Simpson e 
armazena o resultado em um objeto lista.
a re (?!) é conhecido como negative lookahead
'''

exemplo = re.findall(r'Homer(?!\sSimpson).*',id)

print('Nossa string contem os seguintes ids:')
print(id)

''' Loop for para imprimir cada elemento da lista exemplo '''
print('Aplicado re para achar somente os nomes Homer que não possuem o sobrenome Simpson:')
print('Negative Lookahead: re.findall\(r\'Homer(?!\sSimpson).*\',id\'\)\n')
tam = len(exemplo)

for m in exemplo:
    print(m)

print(f"\n{tam} elementos encontrados")

