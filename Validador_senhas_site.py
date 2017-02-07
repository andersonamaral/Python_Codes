
'''
Verificador de senhas de site
'''
import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        print("Senha nao tem entre 6 e 12 caracteres")
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        print("Senha caracteres entre a e z minusculos")
        continue
    elif not re.search("[0-9]",p):
        print("Senha nao tem numeros de 0 a 9")
        continue
    elif not re.search("[A-Z]",p):
        print("Senha caracteres entre A e Z maiusculos")
        continue
    elif not re.search("[$#@]",p):
        print("Senha nao tem os simbolos $#@")
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))
