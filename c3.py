# Gambiarra!!
with open("p1.pas","r") as pkeys:
    pascal_code = pkeys.read().lower()  \
    .replace("\n"," ") \
    .replace(";"," ; ") \
    .replace(")"," ) ") \
    .replace("("," ( ") \ 
    .split(' ') \

print(pascal_code)