valor = 0
with open('vendas_dia.txt', 'r') as arquivo:
    for n in arquivo:
        valor += float(n)  

print(f"O total é: {valor}")
