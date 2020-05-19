import re

pascal_keys=""
pascal_code=""

with open("pascal-keys.txt","r") as pkeys:
    pascal_keys = pkeys.read().split()

with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower().split()

print(pascal_keys)
print(pascal_code)

# 1. ler arquivo
# 2. quebrar em tokens
# 3. usar regexp para verificar o tipo de token

# palavras reservadas - keywords
# float
# int
# variáveis -> regexp
# operações (+, -, *, ^, =, :=)

# Lex - Parser >>> WEB Scraping