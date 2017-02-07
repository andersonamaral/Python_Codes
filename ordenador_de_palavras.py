'''
Recebe palavras separadas por virgulas e as imprime em
ordem alfabetica

'''

items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
