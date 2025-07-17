compras = {}
try:
    while True:
        item = input().strip().upper()
        if item in compras:
            compras[item] += 1
        else:
            compras[item] = 1
except EOFError:
    for item in sorted(compras):
        print(f"{compras[item]} {item}")