import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Uso: python bitcoin.py <quantidade>")

try:
    qtd = float(sys.argv[1])
    resposta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dados = resposta.json()
    preco = float(dados["bpi"]["USD"]["rate"].replace(",", ""))
    total = qtd * preco
    print(f"${total:,.4f}")
except ValueError:
    sys.exit("Quantidade inválida")
except requests.RequestException:
    sys.exit("Erro ao acessar a API")