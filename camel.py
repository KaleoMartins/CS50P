nome = input("Nome em camelCase: ")
for c in nome:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()