def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            return s[i:].isdigit()
    return True

teste = input("Plate: ")
print("Valid" if is_valid(teste) else "Invalid")