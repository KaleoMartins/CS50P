while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split("/")
        x, y = int(x), int(y)
        if x > y:
            continue
        perc = round((x / y) * 100)
        if perc <= 1:
            print("E")
        elif perc >= 99:
            print("F")
        else:
            print(f"{perc}%")
        break
    except (ValueError, ZeroDivisionError):
        pass