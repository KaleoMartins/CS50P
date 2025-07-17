import random

def main():
    pontos = 0
    for _ in range(10):
        x, y = random.randint(1, 9), random.randint(1, 9)
        for tentativa in range(3):
            try:
                resp = int(input(f"{x} + {y} = "))
                if resp == x + y:
                    pontos += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"Resposta correta: {x + y}")
    print("Pontuação:", pontos)

main()